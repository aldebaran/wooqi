#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

va=$(wooqi --seq_config testing/postfail_feature/tests/postfail_skip_all_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail skip all | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail skip all | Different tests --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/tests/postfail_next_step.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail next step | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail next step | Different tests --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/tests/postfail_other_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail other test | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail other test | Different tests --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/tests/postfail_skip_all_test_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail skip all | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail skip all | Same test --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/tests/postfail_next_step_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail next step | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail next step | Same test --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/tests/postfail_other_test_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail other test| Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail other test | Same test --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/actions/postfail_skip_all_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail skip all | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail skip all | Different actions --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/actions/postfail_next_step.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail next step | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail next step | Different actions --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/actions/postfail_other_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail other actions | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail other actions | Different actions --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/actions/postfail_skip_all_action_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail skip all | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail skip all | Same action --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/actions/postfail_next_step_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail next step | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail next step | Same action --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/postfail_feature/actions/postfail_other_action_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Postfail other actions | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Postfail other actions | Same action --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/reruns_feature/actions/reruns_different_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Reruns feature | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Reruns feature | Different actions --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/reruns_feature/actions/reruns_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Reruns feature | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Reruns feature | Same action --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/reruns_feature/tests/reruns_different_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Reruns feature | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Reruns feature | Different tests --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/reruns_feature/tests/reruns_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Reruns feature | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Reruns feature | Same test --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/uut_feature/actions/uut_different_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT feature | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT feature | Different actions --> ${RED}FAILED${NC}"
fi


va=$(wooqi --seq_config testing/uut_feature/actions/uut_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT feature | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT feature | Same action --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/uut_feature/tests/uut_different_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT feature | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT feature | Different tests --> ${RED}FAILED${NC}"
fi


va=$(wooqi --seq_config testing/uut_feature/tests/uut_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT feature | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT feature | Same test --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/uut2_feature/actions/uut2_different_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT2 feature | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT2 feature | Different actions --> ${RED}FAILED${NC}"
fi


va=$(wooqi --seq_config testing/uut2_feature/actions/uut2_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT2 feature | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT2 feature | Same action --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/uut2_feature/tests/uut2_different_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT2 feature | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT2 feature | Different tests --> ${RED}FAILED${NC}"
fi


va=$(wooqi --seq_config testing/uut2_feature/tests/uut2_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- UUT2 feature | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- UUT2 feature | Same test --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/loop_feature/tests/loop_same_test.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Same test --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Same test --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/loop_feature/tests/loop_different_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Different tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Different tests --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/loop_feature/tests/loop_mixed_tests.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Mixed tests --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Mixed tests --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/loop_feature/actions/loop_same_action.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Same action --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Same action --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/loop_feature/actions/loop_different_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Different actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Different actions --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/loop_feature/actions/loop_mixed_actions.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Mixed actions --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Mixed actions --> ${RED}FAILED${NC}"
fi

va=$(wooqi --seq_config testing/loop_feature/tests/loop_different_tests_uut.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Looping feature | Different tests with UUTs --> ${GREEN}PASSED${NC}"
else
    echo -e "- Looping feature | Different tests with UUTs --> ${RED}FAILED${NC}"
fi
