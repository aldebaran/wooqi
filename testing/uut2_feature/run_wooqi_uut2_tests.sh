#!/bin/bash

source testing/source_wooqi_tests.sh

declare -i result
result=0

test_wooqi uut2_feature/actions/uut2_different_actions.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi uut2_feature/actions/uut2_same_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi uut2_feature/tests/uut2_different_tests.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi uut2_feature/tests/uut2_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

exit $result
