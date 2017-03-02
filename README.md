# WOOQI test sequencer

## Introduction

*TBC*

## Installation

You can only install Wooqi if you have access to the local network of SBRE.

    pip install wooqi --find-links=http://10.0.2.107/pypi --index-url http://10.0.2.107/pypi --user --trusted-host 10.0.2.107 --upgrade

* **Dependencies:**
    * **pytest**  
        `pip install pytest --user --upgrade`
    * **pytest-rerunfailures**  
        `pip install pytest-rerunfailures --user --upgrade`
    * **pytest-timeout**  
        `pip install pytest-timeout --user --upgrade`
    * **pytest-spec**  
        `pip install pytest-spec --user --upgrade`

## Your wooqi project

Wooqi is only a test sequencer and does not contain some tests itself. It means that you must create
your own project containing your own tests, which will be read and executed by Wooqi.

### Create a new project

Create an empty directory with the name of your choice, for instance *my_wooqi_project*.
In this directory, create, at least, the following sub-directories:
* test_sequences
* test_steps
* fixtures
* misc_tools

And the following files:
* conftest.py *(can be empty at first)*

### Write tests

#### Write a test step

*TBC*

#### Write an action

*TBC*

#### Write a test sequence

##### Basics

 A test is described in a configuration file (.ini).
 As a result this file contains several sections with some attributes, like this:
```ini
[my_section]
attr1=value1
attr2=value2
```

There is one initial section that could be present in these configuration files: **[test_info]**
It contains information about the test itself. Following attributes can be present in this section:
* **loop_tests** : Used to make loops in the sequence.
  Please refer to the [dedicated section](#make-loops-in-the-test-sequence)
* **loop_iter** : Used to make loops in the sequence.
  Please refer to the [dedicated section](#make-loops-in-the-test-sequence)

Other sections are referring to test steps or actions. Any step or action can be picked from the
test_steps directory simply by writing its name as the section name.  
Example: `[test_battery_charge]`. Some attributes of this section are used to organize this step in
the test, and some others are given to the step function as parameters.

Here is a list of attributes that could be written in step/action sections:
* **test_order** : (mandatory) As step are called one after another, an order must be specified
  thanks to this argument. Warning the order is not defined by the order of definition in the .ini
* **post_fail** : *TBC*
* **uut** : *TBC*
* **uut2** : *TBC*
* *[...TBC...]*

##### Call the same step several times in a single sequence

If you need to call the same test step several times, there is a special syntax. You must add "\_X"
at the end of the test name, increasing the number "X from "0" as follow :
```ini
[test_foo_0] ; Start with 0
test_order=10
uut=dummy1

[test_foo_1] ; Continue with 1
test_order=20
uut=dummy2

[test_foo_X] ; and so on...
test_order=30
uut=dummy3
```

##### Make loops in the test sequence

You must add two attributes in the `[test_info]` section:

* **loop_tests=(a,b)** where a and b are the test_order numbers of the first and the last steps of the loop.
* **loop_iter=k** where k is the number of iterations of the loop.

In the following example, the sequence *test_b --> test_c --> test_d* will be repeated 2 times:
```ini
[test_info]
loop_tests=(20, 40)
loop_iter=2

[test_a]
test_order=10

[test_b]
test_order=20

[test_c]
test_order=30

[test_d]
test_order=40

[test_e]
test_order=50
```

### Run a test sequence

To launch a test, move to the depository root and launch the following command:

    wooqi --seq-config TEST_SEQUENCE_FILE --ip ROBOT_IP --sn ROBOT_SN [--comment COMMENT] [-s] [-k TEST_NAME] [--lf]

Where:
* **[--ip ROBOT_IP]** IP adress of the robot. Default is “127.0.0.1”.
* **[--seq-config TEST_SEQUENCE_FILE]** (required) Config file of the test sequence
* **[--sn ROBOT_SN]** (required) Sample Name. Used to name the logs.
* **[--comment COMMENT]** Add a comment to the run (will be saved in the report)
* **[-s]** Display logs and "print" output in the console.
* **[-k TEST_NAME]** Execute the specified tests only (name can be incomplete)
* **[-lf]** Execute the last failed test only.

Example:

    wooqi --seq-config test_sequences/head/sw_version.ini --ip 10.0.206.235 --sn myRobot --comment "My first run!"

### Advanced functionalities

*TBC*

#### Write tools

*TBC*

#### Configure wooqi

Copy the file `wooqi_conf_template.cfg` at the root of your project directory, and rename it `wooqi_conf.cfg`.

This file will be read by *wooqi* and allows you to customize several features of it.
All the available parameters and their use are explained in this template.

#### Write your own fixtures

*TBC*

#### Write your own pytest hooks

*TBC*
