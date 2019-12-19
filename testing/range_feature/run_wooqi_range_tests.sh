#!/bin/bash

source testing/source_wooqi_tests.sh

declare -i result
result=0

test_wooqi range_feature/range_with_2_args.ini
if [ $? -ne 0 ];then
    result=1
fi

test_wooqi range_feature/range_with_3_args.ini
if [ $? -ne 0 ];then
    result=1
fi
