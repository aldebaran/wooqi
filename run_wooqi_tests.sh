#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
export RED
export GREEN
export NC


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

exit $result1 || $result2 || $result3 || $result4 || $result5 || $result6 || $result7
