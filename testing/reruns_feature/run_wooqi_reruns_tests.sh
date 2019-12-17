#!/bin/bash

source testing/source_wooqi_tests.sh

declare -i result
result=0

test_wooqi reruns_feature/actions/reruns_different_actions.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi reruns_feature/actions/reruns_same_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi reruns_feature/tests/reruns_different_tests.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi reruns_feature/tests/reruns_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

exit $result
