#!/bin/bash

testing/postfail_feature/./run_wooqi_postfail_tests.sh
result1=$?

testing/reruns_feature/./run_wooqi_reruns_tests.sh
result2=$?

testing/uut_feature/./run_wooqi_uut_tests.sh
result3=$?

testing/uut2_feature/./run_wooqi_uut2_tests.sh
result4=$?

testing/loop_feature/./run_wooqi_loop_tests.sh
result5=$?

testing/cache_feature/./run_wooqi_cache_tests.sh
result6=$?

testing/range_feature/./run_wooqi_range_tests.sh
result7=$?

result=1
if [ $result1 -eq 0 ] && [ $result2 -eq 0 ] && [ $result3 -eq 0 ] && [ $result4 -eq 0 ] && [ $result5 -eq 0 ] && [ $result6 -eq 0 ] && [ $result7 -eq 0 ];then
    result=0
fi
exit $result
