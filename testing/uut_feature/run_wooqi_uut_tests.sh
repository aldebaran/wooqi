#!/bin/bash

declare -i result
result=0

va=$(wooqi --seq-config testing/uut_feature/actions/uut_different_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT feature | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT feature | Different actions --> ${RED}FAILED${NC}"
    result=1
fi


va=$(wooqi --seq-config testing/uut_feature/actions/uut_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT feature | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT feature | Same action --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/uut_feature/tests/uut_different_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT feature | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT feature | Different tests --> ${RED}FAILED${NC}"
    result=1
fi


va=$(wooqi --seq-config testing/uut_feature/tests/uut_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT feature | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT feature | Same test --> ${RED}FAILED${NC}"
    result=1
fi

exit $result
