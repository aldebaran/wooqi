#!/bin/bash

source testing/source_wooqi_tests.sh

declare -i result
result=0

test_wooqi loop_feature/tests/loop_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi loop_feature/tests/loop_different_tests.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi loop_feature/tests/loop_mixed_tests.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi loop_feature/actions/loop_same_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi loop_feature/actions/loop_different_actions.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi loop_feature/actions/loop_mixed_actions.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi loop_feature/tests/loop_different_tests_uut.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi loop_feature/tests/loop_same_test_uut.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi loop_feature/tests/loop_fail_second_iteration.ini
if [ $? -ne 0 ];then
    result=1
fi

exit $result
