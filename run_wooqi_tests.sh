#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'
export RED
export GREEN
export NC


testing/postfail_feature/./run_wooqi_postfail_tests.sh

testing/reruns_feature/./run_wooqi_reruns_tests.sh

testing/uut_feature/./run_wooqi_uut_tests.sh

testing/uut2_feature/./run_wooqi_uut2_tests.sh

testing/loop_feature/./run_wooqi_loop_tests.sh
