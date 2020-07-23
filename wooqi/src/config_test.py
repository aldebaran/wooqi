# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
TestConfig Class
"""
import os
import re
from sys import exit
from collections import OrderedDict
from configparser import SafeConfigParser


class MultiDict(OrderedDict):
    """
    To differentiate section with the same name in .ini file
    Add _X of sections name, with X depently the number of call
    """

    _keys_name_and_params = {}    # class variable

    def __setitem__(self, key, val):
        if isinstance(val, dict) and (key.startswith('test_') or key.startswith('action_')):
            if key.count('-') > 1:
                msg = '{} is not compatible name: too much -'.format(key)
                print(msg)
                raise Exception(msg)

            try:
                test_name, param = key.split('-')
                try:
                    param = int(param)
                except ValueError:
                    msg = '{} is not compatible name: Value after - must be integer'.format(key)
                    print(msg)
                    raise Exception(msg)
            # No param found
            except ValueError:
                test_name = key
                if test_name in self._keys_name_and_params.keys():
                    param = self._keys_name_and_params[key][-1] + 1
                else:
                    param = 0

            if test_name not in self._keys_name_and_params:
                self._keys_name_and_params[test_name] = [param]
            elif param not in self._keys_name_and_params[test_name]:
                self._keys_name_and_params[test_name].append(param)
            else:
                msg = '{} has multiple call unclear, please verify your configuration file'.format(
                    test_name)
                print(msg)
                raise Exception(msg)

            key = '{} {}'.format(test_name, param)
        OrderedDict.__setitem__(self, key, val)


class ConfigTest(object):
    """ Config Class """

    def __init__(self, config_path):
        # Create dictionary with all section are unique names
        config_file = config_path
        try:
            parser = SafeConfigParser(dict_type=MultiDict, strict=False)
            parser.optionxform = str
            file_parse = parser.read(config_file)
        except KeyError as error:
            msg = 'Problem while parsing configuration file {}: {}'.format(config_file, error)
            print(msg)
            raise Exception(msg)
        if len(file_parse):
            self.config_file_exists = True
        else:
            self.config_file_exists = False

        # Create ordered dictionary with final tests names
        test_number = 1
        file_config = OrderedDict()
        list_name = []
        for section in parser.sections():
            items = parser.items(section)
            # convert unicode to str for items values
            items_str = {}
            for key, value in list(dict(items).items()):
                items_str[key] = '{}'.format(value)
            if section.startswith('test_') or section.startswith('action_'):
                name, param = section.rsplit(' ', 1)
                if param == '0' and str(parser.sections()).count('{} '.format(name)) == 1:
                    section = name
                else:
                    section = '{}-{}'.format(name, param)

                list_name.append(name)
                file_config[section] = dict(items_str)
                file_config[section]['test_order'] = test_number
                test_number += 1
            else:
                file_config[section] = dict(items_str)

        # Check post_fail option
        file_config_temp = list(file_config)
        for test_name in file_config:
            file_config_temp.remove(test_name)
            if 'post_fail' in file_config[test_name]:
                post_fail = file_config[test_name]['post_fail']
                if post_fail.lower() != 'next_step' and post_fail not in file_config_temp:
                    msg = 'Problem with post_fail option, {} not found'.format(post_fail)
                    print(msg)
                    raise Exception(msg)

        # Check loop option
        try:
            loop_tests = file_config['test_info']['loop_tests']
        except KeyError:
            loop_tests = None
        if loop_tests:
            loop_tests = loop_tests.split('|')
            if len(loop_tests) != 2:
                msg = 'Problem with loop option, please verify format: ' \
                    'loop_tests=test_NAME1|test_NAME2'
                print(msg)
                raise Exception(msg)
            msg = ''
            if loop_tests[0] not in file_config.keys():
                msg += '{} '.format(loop_tests[0])
            if loop_tests[1] not in file_config.keys():
                msg += '{} '.format(loop_tests[1])
            if msg:
                msg += 'tests not found for loop option'
                print(msg)
                raise Exception(msg)
            try:
                loop_iter = int(file_config['test_info']['loop_iter'])
                file_config['test_info']['loop_iter'] = loop_iter
            except Exception:
                msg = 'Loop option is enable but loop_iter parameter is not correctly create'
                print(msg)
                raise Exception(msg)

            # Add the iteration number
            loop_start_order = file_config[loop_tests[0]]['test_order']
            loop_stop_order = file_config[loop_tests[1]]['test_order']
            for session in file_config:
                if 'test_order' in file_config[session]:
                    test_order = file_config[session]['test_order']
                    if loop_start_order <= test_order <= loop_stop_order:
                        file_config[session]['wooqi_loop_iter'] = loop_iter

        self.file_config = file_config

    @staticmethod
    def _get_paramater(param, uut, uut2, evaluate=True):
        """
        Get paramater
        """
        parameter = None
        try:
            if param == "Default":
                parameter = param
            elif "|" not in param and ":" not in param:
                if evaluate:
                    parameter = eval(param)
                else:
                    parameter = param
            else:
                dico = {}
                params = param.split("|")
                for each in params:
                    tab = each.split(":")
                    if evaluate:
                        dico[tab[0]] = eval(tab[1])
                    else:
                        dico[tab[0]] = tab[1]

                if uut is not None and uut2 is not None:
                    uuts_name = "{}-{}".format(uut, uut2)
                    if uuts_name in dico.keys():
                        parameter = dico[uuts_name]
                    elif "Default" in dico.keys():
                        parameter = dico["Default"]
                elif uut is not None:
                    if uut in dico.keys():
                        parameter = dico[uut]
                    elif "Default" in dico.keys():
                        parameter = dico["Default"]
                else:
                    parameter = dico

        except Exception as error:
            print(error)
        return parameter

    @staticmethod
    def _get_range(string):
        """
        Return range list
        """
        range_args = list(map(int, re.findall("([0-9]+)", string)))
        if len(range_args) == 2:
            range_args.append(1)
        return list(map(str, list(range(range_args[0], range_args[1], range_args[2]))))

    @staticmethod
    def _get_folders(string):
        """
        Return a list containing the names of the elements from the given dir.
        Directory must be given with absolute path
        Returned elements are given with absolute path.
        Please note that files in subdirectories are also returned!!
        Returned elements are files only, directories are 'walked' through.
        """
        index_1, index_2 = 0, 0
        for index, each in enumerate(string):
            if each == "(":
                index_1 = index
            elif each == ")":
                index_2 = index
        root_dir = string[index_1 + 1:index_2]
        if os.path.isdir(root_dir):
            elements = []
            for current_folder, subdirectories, files in os.walk(root_dir):
                for filename in files:
                    elements.append(os.path.join(current_folder, filename))
            return elements
        else:
            exit("Folders parameter in 'uut' is not a valid directory.")

    @staticmethod
    def _get_folder(string):
        """
        Return a list containing the names of the elements from the given dir.
        Directory must be given with absolute path
        Returned elements are given with absolute path.
        Returned elements can be directories as well as files.
        """
        index_1, index_2 = 0, 0
        for index, each in enumerate(string):
            if each == "(":
                index_1 = index
            elif each == ")":
                index_2 = index
        folder_path = string[index_1 + 1:index_2]
        if os.path.isdir(folder_path):
            elements = map(os.path.abspath, ['{}/{}'.format(folder_path, s)
                                             for s in os.listdir(folder_path)])
            return elements
        else:
            exit("Folder parameter in 'uut' is not a valid directory.")

    def loop_infos(self):
        """
        Get loop infos
        """
        if 'test_info' in self.file_config.keys() and \
                "loop_tests" in self.file_config['test_info']:
            loop_tests = self.file_config['test_info']['loop_tests'].split("|")
            loop_iter = self.file_config['test_info']['loop_iter']
            return loop_tests, loop_iter
        else:
            return None

    def misc_data(self, test_name, uut, uut2):
        """
        Misc data parameter
        """
        if "misc_data" in self.file_config[test_name]:
            misc_data = self.file_config[test_name]['misc_data']
            return self._get_paramater(misc_data, uut, uut2)
        else:
            return None

    def comparator(self, test_name, uut, uut2):
        """
        Comparator parameter
        """
        if "comparator" in self.file_config[test_name]:
            comparator = self.file_config[test_name]['comparator']
            return self._get_paramater(comparator, uut, uut2, evaluate=False)
        else:
            return "=="

    def limit(self, test_name, uut, uut2):
        """
        Limit parameter
        """
        if "limit" in self.file_config[test_name]:
            limit = self.file_config[test_name]['limit']
            return self._get_paramater(limit, uut, uut2)
        else:
            return None

    def time_test(self, test_name, uut, uut2):
        """
        Time parameter
        """
        if "time_test" in self.file_config[test_name]:
            time_test = self.file_config[test_name]['time_test']
            return self._get_paramater(time_test, uut, uut2)
        else:
            return None

    def nb_cycles(self, test_name, uut, uut2):
        """
        Cycles number parameter
        """
        if "nb_cycles" in self.file_config[test_name]:
            time_test = self.file_config[test_name]['nb_cycles']
            return self._get_paramater(time_test, uut, uut2)
        else:
            return None

    def exist(self, test_name):
        """
        Exist parameter
        """
        return test_name in self.file_config

    def order(self, test_name):
        """
        Order parameter
        """
        try:
            order = int(self.file_config[test_name]['test_order'])
        except Exception:
            order = 0
        return order

    def uut(self, test_name):
        """
        uut parameter
        """
        try:
            values = self.file_config[test_name]['uut']
            if "range" in values:
                return self._get_range(values)
            elif "recurse_folders" in values:
                return self._get_folders(values)
            elif "folder" in values:
                return self._get_folder(values)
            else:
                uuts = values.split("|")
                return uuts
        except Exception:
            return None

    def uut2(self, test_name):
        """
        uut2 parameter
        """
        try:
            values = self.file_config[test_name]['uut2']
            if "range" in values:
                return self._get_range(values)
            elif "recurse_folders" in values:
                return self._get_folders(values)
            elif "folder" in values:
                return self._get_folder(values)
            else:
                return values.split("|")
        except Exception:
            return None

    def post_fail(self, test_name):
        """
        Post fail parameter
        """
        try:
            if "post_fail" in self.file_config[test_name]:
                post_fail = str(self.file_config[test_name]['post_fail'])
                return post_fail
            else:
                return None
        except Exception:
            return None

    def reruns(self, test_name):
        """
        Rerun parameter
        """
        try:
            if "reruns" in self.file_config[test_name]:
                reruns = int(self.file_config[test_name]['reruns'])
                return reruns
            else:
                return None
        except Exception as error:
            print(error)

    def timeout(self, test_name):
        """
        Timeout parameter
        """
        try:
            if "timeout" in self.file_config[test_name]:
                timeout = int(self.file_config[test_name]['timeout'])
                return timeout
            else:
                return None
        except Exception as error:
            print(error)

    def sequence(self, test_name):
        """
        Get sequence name parameter
         Return None if test not is in sequence
        """
        try:
            sequence = self.file_config[test_name]['sequence']
            return sequence
        except Exception:
            return None
