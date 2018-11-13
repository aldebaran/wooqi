#!/bin/bash

declare -i result
result=0

va=$(wooqi --seq-config testing/uut2_feature/actions/uut2_different_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT2 feature | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT2 feature | Different actions --> ${RED}FAILED${NC}"
    result=1
fi


va=$(wooqi --seq-config testing/uut2_feature/actions/uut2_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT2 feature | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT2 feature | Same action --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/uut2_feature/tests/uut2_different_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT2 feature | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT2 feature | Different tests --> ${RED}FAILED${NC}"
    result=1
fi


va=$(wooqi --seq-config testing/uut2_feature/tests/uut2_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT2 feature | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT2 feature | Same test --> ${RED}FAILED${NC}"
    result=1
fi

exit $result
