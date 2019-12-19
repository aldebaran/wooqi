#!/bin/bash

source testing/source_wooqi_tests.sh

declare -i result
result=0

test_wooqi postfail_feature/tests/postfail_skip_all_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/tests/postfail_next_step.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/tests/postfail_other_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/tests/postfail_skip_all_test_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/tests/postfail_next_step_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/tests/postfail_other_test_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/actions/postfail_skip_all_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/actions/postfail_next_step.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/actions/postfail_other_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/actions/postfail_skip_all_action_same_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/actions/postfail_next_step_same_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/actions/postfail_other_action_same_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/tests/postfail_fixture_setup_fail.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi postfail_feature/tests/postfail_fixture_teardown_fail.ini
if [ $? -ne 0 ];then
    result=1
fi

exit $result
