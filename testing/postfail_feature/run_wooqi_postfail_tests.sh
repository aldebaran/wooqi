#!/bin/bash

declare -i result
result=0

va=$(wooqi --seq-config testing/postfail_feature/tests/postfail_skip_all_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail skip all | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail skip all | Different tests --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/tests/postfail_next_step.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail next step | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail next step | Different tests --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/tests/postfail_other_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail other test | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail other test | Different tests --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/tests/postfail_skip_all_test_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail skip all | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail skip all | Same test --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/tests/postfail_next_step_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail next step | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail next step | Same test --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/tests/postfail_other_test_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail other test| Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail other test | Same test --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/actions/postfail_skip_all_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail skip all | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail skip all | Different actions --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/actions/postfail_next_step.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail next step | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail next step | Different actions --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/actions/postfail_other_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail other actions | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail other actions | Different actions --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/actions/postfail_skip_all_action_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail skip all | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail skip all | Same action --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/actions/postfail_next_step_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail next step | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail next step | Same action --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/actions/postfail_other_action_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail other actions | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail other actions | Same action --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/tests/postfail_fixture_setup_fail.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail fixture setup fail | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail fixture setup fail | Same action --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/postfail_feature/tests/postfail_fixture_teardown_fail.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail fixture teardown fail | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail fixture teardown fail | Same action --> ${RED}FAILED${NC}"
    result=1
fi

exit $result
