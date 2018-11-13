#!/bin/bash

declare -i result
result=0

va=$(wooqi --seq-config testing/reruns_feature/actions/reruns_different_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Reruns feature | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Reruns feature | Different actions --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/reruns_feature/actions/reruns_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Reruns feature | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Reruns feature | Same action --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/reruns_feature/tests/reruns_different_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Reruns feature | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Reruns feature | Different tests --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/reruns_feature/tests/reruns_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Reruns feature | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Reruns feature | Same test --> ${RED}FAILED${NC}"
    result=1
fi

exit $result
