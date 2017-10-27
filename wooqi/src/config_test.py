# -*- coding: utf-8 -*-

# Copyright (c) 2017 SoftBank Robotics Europe. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
TestConfig Class
"""
import os
from sys import exit
import collections
from ConfigParser import SafeConfigParser


class ConfigTest(object):
    """ Config Class """

    def __init__(self, config_path):
        config_file = config_path
        try:
            parser = SafeConfigParser()
            parser.optionxform = str
            file_parse = parser.read(config_file)
        except Exception, error:
            msg = 'Problem while parsing configuration file %s (%s)' % (
                config_file, error)
            print msg
            raise
        if len(file_parse) == 0:
            self.config_file_exists = False
        else:
            self.config_file_exists = True

        file_config = collections.OrderedDict()
        for section in parser.sections():
            dict_tmp = {}
            for option in parser.options(section):
                dict_tmp[option] = parser.get(section, option)
            file_config[section] = dict_tmp
            file_config[section]["test_order"] = file_config.keys().index(section) + 1

        self.file_config = file_config
        self.current_test = None

    @staticmethod
    def _get_paramater(param, uut, uut2, evaluate=True):
        """
        Get paramater
        """
        try:
            if param == "Default":
                return param
            elif "|" not in param and ":" not in param:
                if evaluate:
                    return eval(param)
                else:
                    return param

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
                    uuts_name = "%s-%s" % (uut, uut2)
                    if uuts_name in dico.keys():
                        return dico[uuts_name]
                    elif "Default" in dico.keys():
                        return dico["Default"]
                    else:
                        return None
                elif uut is not None:
                    if uut in dico.keys():
                        return dico[uut]
                    elif "Default" in dico.keys():
                        return dico["Default"]
                    else:
                        return None
                else:
                    return dico

        except BaseException as error:
            print error
            return None

    @staticmethod
    def _get_range(string):
        """
        Return range list
        """
        index_1, index_2, index_3 = 0, 0, 0
        for index, each in enumerate(string):
            if each == "(":
                index_1 = index
            elif each == ",":
                index_2 = index
            elif each == ")":
                index_3 = index
        first_int = int(string[index_1 + 1:index_2])
        second_int = int(string[index_2 + 1:index_3])
        return range(first_int, second_int)

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
            elements = map(os.path.abspath, [folder_path + "/" + s
                                             for s in os.listdir(folder_path)])
            return elements
        else:
            exit("Folder parameter in 'uut' is not a valid directory.")

    def loop_infos(self):
        """
        Get loop infos
        """
        if 'test_info' not in self.file_config.keys():
            return None
        elif "loop_tests" in self.file_config['test_info']:
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
        except BaseException:
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
        except BaseException:
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
        except BaseException:
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
        except BaseException:
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
        except BaseException as error:
            print error
            return None

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
        except BaseException as error:
            print error

    def sequence(self, test_name):
        """
        Get sequence name parameter
         Return None if test not is in sequence
        """
        try:
            sequence = self.file_config[test_name]['sequence']
            return sequence
        except:
            return None
