#!/bin/bash

declare -i result
result=0

va=$(wooqi --seq-config testing/loop_feature/tests/loop_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Same test --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/loop_feature/tests/loop_different_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Different tests --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/loop_feature/tests/loop_mixed_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Mixed tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Mixed tests --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/loop_feature/actions/loop_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Same action --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/loop_feature/actions/loop_different_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Different actions --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/loop_feature/actions/loop_mixed_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Mixed actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Mixed actions --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/loop_feature/tests/loop_different_tests_uut.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Different tests with UUTs --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Different tests with UUTs --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/loop_feature/tests/loop_same_test_uut.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Same test with UUTs --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Same test with UUTs --> ${RED}FAILED${NC}"
    result=1
fi

exit $result
