#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

test_wooqi()
{
    # The wooqi sequence is launched with configuration file path give by the first parameter
    # If the second parameter exists, rerun with --failed-first option to execute the sequence from the first failure
    config_file=testing/$1
    va=$(pytest --seq-config ${config_file} --sn wooqi_tests -s --spec --wooqi)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? -eq 0 ];then
        if [ -z "$2" ]; then
            echo -e "- $config_file --> ${GREEN}PASSED${NC}"
            return 0
        else
            va=$(pytest --seq-config ${config_file} --sn wooqi_tests -s --ff --wooqi --spec)
            echo -e $va | grep --quiet "TEST PASSED"
            if [ $? -eq 0 ];then
                echo -e "- $config_file --> ${GREEN}PASSED${NC}"
                return 0
            else
                echo -e "- $config_file --> ${RED}FAILED${NC}"
            fi
        fi
    else
        echo -e "- $config_file / INITIALIZATION --> ${RED}FAILED${NC}"
    fi
    return 1
}
