# Wooqi test sequencer

[![PyPI version fury.io](https://img.shields.io/pypi/v/wooqi.png)](https://pypi.python.org/pypi/wooqi/)
[![PyPI license](https://img.shields.io/pypi/l/wooqi.svg)](https://pypi.python.org/pypi/wooqi/)
[![Build Status](https://travis-ci.org/aldebaran/wooqi.svg?branch=master)](https://travis-ci.org/aldebaran/wooqi)

## Introduction

**Wooqi** is a fork of the [Python](https://www.python.org) module named
[pytest](http://pytest.org). It allows to code tests in a very special way. It is a usefull tool to
manage a big database of tests, as it simplifies their creation, their maintenance, and their
execution.

Wooqi hacks the standard use of pytest to introduce new mechanics, in order to apply a precise
testing methodology which can be described by the following key points:

* There is a *test steps* database.
* There is a *test sequences* database, where each sequence is
composed of one or several test steps picked from the *test steps* database.
* There are some *common tools* (custom python classes or functions)
and *fixtures* which all can be used by any test step.
* Users can execute a single test sequence with a single command line.
* All reports and logs of test sequences are saved in a common *reports* database.

Creation of logs, parametrization of tests, report reading, and tests scheduling are some examples
of the things which are simplified with wooqi. Moreover, the generic aspect of this tool allows to
use it for any kind of target under test, as long as you can respect its methodology.

Finally, it is important to note that **Wooqi** does not contain any test itself. It is a just a
tool to execute tests which are written in what we call a **Wooqi project**. In this way, you can
have several **Wooqi projects** on your machine, each one having its own specific features, while
using only one tool (the **Wooqi** plugin) to execute any test in any project.

For the reasons listed above, Wooqi can be considered as an independant tool instead of a simple
pytest plugin.

## Installation

You can install wooqi as a pip package.

    pip install wooqi --user

Or you can clone the depository, and manually build and install the package:

    python setup.py bdist
    pip install dist/<package_name>

Where `<package_name>` is the name of the wooqi package with its version

## Your wooqi project

Wooqi is only a test sequencer and does not contain some tests itself. It means that you must create
your own project containing your own tests, which will be read and executed by Wooqi.

### Create a new project

To automatically initialize a new Wooqi project, use the following command line:

    wooqi --init-project MY_PROJECT

Replace MY_PROJECT by the path of your project directory (can be relative or absolute).  This
creates the necessary sub-directories and files for your project. Most of the files are empty, as
they are just some examples.

The tree view of the created project is just a suggestion and is not mandatory for Wooqi to work.
You can customize your Wooqi project as you like, as long as you respect the following rules (please
read the next sections to fully understand these rules):

1. Fixtures must be imported in *conftest.py* at the root of the project.
2. *setup.cfg* must be at
the root of the project. (Please see **Advanced functionalities** section)
3. Test steps, actions, and sequences must respect the rules that are given in their dedicated section.

### Write tests

#### Write a test step

A test step is simply a python function with an **assertion** in it. The following rules must be
observed:

* One test step is represented by one function.
* A test step can be written in a file in any directory (default directory is *test_steps*).
* The name of this file must start with "*test_*".
* A test step name must start with "*test_*" Assertions in a test step must observe the [guidelines
of the pytest module](https://docs.pytest.org/en/latest/assert.html).
* Arguments of a test step must be picked from [existing fixtures](#write-your-own-fixtures) and the **Wooqi** special
arguments given below.
  For more information about these special arguments, please see the "*test sequences*" section of
  this documentation.
  * uut
  * uut2
  * test_info
* A test step can use any python function from any other file as long as it is
imported. It is standard python !

#### Write an action

An action is almost the same than a test step, except it does not necessarily have an assertion.
The following rules must be observed:

* One action is represented by one function.
* An action can be written in a file in any directory (default directory is *actions_step*).
* The name of this file must start with "*actions_*".
* An action name must start with "*action_*".
* An action can contain an assertion like a test step but this is not mandatory.
* Arguments of an action follow the same rule than for a test step.
* An action can use any python function from any other file as long as it is imported.
It is standard python !

#### Write a test sequence

##### Basics

 A test is described in a configuration file (*.ini*). This file can be in any directory (default is
 *sequences*). As a result this file contains several sections with some attributes, like this:

```ini
[my_section]
attr1=value1
attr2=value2
```

There is one initial section that could be present in these configuration files:

* **[test_info]** It contains information about the sequence itself.
    Following attributes can be present in this section:
    * **loop_tests**: Used to make loops in the sequence.
      Please refer to the [dedicated section](#make-loops-in-the-test-sequence)
    * **loop_iter**: Used to make loops in the sequence.
      Please refer to the [dedicated section](#make-loops-in-the-test-sequence)

Other sections are referring to test steps or actions. Any step or action can be picked from the
test_steps directory simply by writing its name as the section name.

**Example:**
`[test_battery_charge]`. Some attributes of this section are used to organize this step in the test,
and some others are given to the step function as parameters.  The step order is defined by the
order of definition in the .ini

Here is a list of attributes that could be written in step/action sections:

* **post_fail**: *TBC*
* **reruns**: *TBC*
* **uut**: *TBC*
* **uut2**: *TBC*
* *[...TBC...]*

##### Call the same step several times in a single sequence

If you need to call the same test step several times, there is a special syntax. You must add "\_X"
at the end of the test name, increasing the number "X from "0" as follow :

```ini
[test_foo_0] ; Start with 0
uut=dummy1

[test_foo_1] ; Continue with 1
uut=dummy2

[test_foo_X] ; and so on...
uut=dummy3
```

##### Make loops in the test sequence

You must add two attributes in the `[test_info]` section:

* **loop_tests=a|b** where a and b are the names of the first and the last steps of the loop.
* **loop_iter=k** where k is the number of iterations of the loop.

In the following example, the sequence *test_b --> test_c --> test_d* will be repeated 2 times:

```ini
[test_info]
loop_tests=test_b|test_d
loop_iter=2

[test_a]

[test_b]

[test_c]

[test_d]

[test_e]
```

### Run a test sequence

To launch a test, move to the root of your project depository and run the following command:

    wooqi --seq-config TEST_SEQUENCE_FILE --sn SAMPLE_NAME [-s] [-k TEST_NAME] [--lf]

Where:

* **[--seq-config TEST_SEQUENCE_FILE]** (required) relative path to the .ini file of the test sequence.
* **[--sn SAMPLE_NAME]** (required) Sample Name. Used to name the logs.
* **[-s]** Display logs and print output in the console.
* **[-k TEST_NAME]** Execute the specified tests only (name can be incomplete).
* **[-lf]** Execute the last failed test only.

Example:

    wooqi --seq-config test_sequences/folder1/seq1.ini --sn mySample

### Rerun a test sequence since the first fail

To rerun sequence since the first test failed, use the same command and add --ff option
(--failed-first):

    wooqi --seq-config TEST_SEQUENCE_FILE --sn SAMPLE_NAME --ff

If sequence fail in loop, all test of the loop are rerun.

You can defined a previous test or action required.  If the test failed has a requirement, the
sequence rerun since the test defined to the .ini file.

```ini
[test_a]

[test_b]

[test_c]
test_required='test_b'

[test_d]
test_required='test_b'

[test_e]
```

### Advanced functionalities


#### Write tools

Steps may need external functions that are useful for several of them. These functions, that we call
"tools" can be written in any python files. Afterwards they can be imported in python files which
contain steps and/or fixtures, and called within the steps. The only rule that is mandatory not to
confuse wooqi is to avoid naming these functions with a name that starts with "test_" or "action_",
as these names are only used for steps and actions.

#### Configure wooqi

Copy the file `wooqi_conf_template.cfg` at the root of your project directory, and rename it
`wooqi_conf.cfg`.

This file will be read by *wooqi* and allows you to customize several features of it.  All the
available parameters and their use are explained in this template.

#### Write your own fixtures

The concept of fixtures is a nice feature provided by Py.test. To get more information about it,
please read the official [documentation](https://docs.pytest.org/en/latest/fixture.html).
The only difference with Wooqi, it's just that you have to import the custom pytest module included in Wooqi:

```python
import wooqi_pytest

@wooqi_pytest.fixture()
def my_fixture():
    """Example of wooqi fixture."""
    pass
```


You can add your own fixtures to your project in any file you want. Then, each one of your steps can
call a fixture as one of its arguments. These fixtures will be called before and/or after the
execution of the step in the sequence.

#### Write your own wooqi hooks

Wooqi offers all the pytest hooks that allow to insert custom code in the middle of the
execution of wooqi. To get more information about these, please read the official
[documentation](https://docs.pytest.org/en/latest/writing_plugins.html#writinghooks).

You can add your own custom hooks in your wooqi project.
