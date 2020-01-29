#!/bin/bash

source testing/source_wooqi_tests.sh

declare -i result
result=0

test_wooqi cache_feature/tests/cache_standard_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/actions/cache_standard_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_uut_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/actions/cache_uut_same_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_uut_different_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/actions/cache_uut_different_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_required_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/actions/cache_required_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_required_test_with_uut.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/actions/cache_required_action_with_uut.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_loop_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/actions/cache_loop_same_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_loop_different_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/actions/cache_loop_different_action.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_loop_uut_same_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_loop_uut_different_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_mark_parametrize_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_mark_parametrize_with_uut_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_mark_parametrize_loop_test.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_test_required.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_test_required_with_uut.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi cache_feature/tests/cache_test_required_from_class.ini
if [ $? -ne 0 ];then
    result=1
fi

exit $result
