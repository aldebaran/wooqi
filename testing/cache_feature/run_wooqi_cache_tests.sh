#!/bin/bash

declare -i result
result=0

va=$(wooqi --seq-config testing/cache_feature/tests/cache_standard_test.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_standard_test.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Standard tests --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Standard tests --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Standard tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/actions/cache_standard_action.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/actions/cache_standard_action.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Standard actions --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Standard actions --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Standard actions / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/tests/cache_uut_same_test.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_uut_same_test.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | uut same tests --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | uut same tests --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | uut same tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/actions/cache_uut_same_action.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/actions/cache_uut_same_action.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | uut same actions --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | uut same actions --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | uut same actions / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/tests/cache_uut_different_test.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_uut_different_test.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | uut different tests --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | uut different tests --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | uut different tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/actions/cache_uut_different_action.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/actions/cache_uut_different_action.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | uut different actions --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | uut different actions --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | uut different actions / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/tests/cache_required_test.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_required_test.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Test required --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Test required --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Standard tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/actions/cache_required_action.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/actions/cache_required_action.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Action required --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Action required --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Standard tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/tests/cache_required_test_with_uut.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_required_test_with_uut.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Test required with uut --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Test required with uut --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Standard tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/actions/cache_required_action_with_uut.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/actions/cache_required_action_with_uut.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Action required with uut --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Action required with uut --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Standard tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/tests/cache_loop_same_test.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_loop_same_test.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Restart loop on unique tests --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Restart loop on unique tests --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Restart loop on unique tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/actions/cache_loop_same_action.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/actions/cache_loop_same_action.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Restart loop same actions --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Restart loop same actions --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Restart loop same actions / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/tests/cache_loop_different_test.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_loop_different_test.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Restart loop different tests --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Restart loop different tests --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Restart loop different tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/actions/cache_loop_different_action.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/actions/cache_loop_different_action.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Restart loop different actions --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Restart loop different actions --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Restart loop different actions / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/tests/cache_loop_uut_same_test.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_loop_uut_same_test.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Restart loop with UUTS same tests--> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Restart loop with UUTS same tests --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Restart loop with UUTS same tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/cache_feature/tests/cache_loop_uut_different_test.ini --sn wooqi_tests -s)
echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    va=$(wooqi --seq-config testing/cache_feature/tests/cache_loop_uut_different_test.ini --sn wooqi_tests -s --ff)
    echo -e $va | grep --quiet "TEST PASSED"
    if [ $? = 0 ];then
        echo -e "- Cache feature | Restart loop with UUTS different tests --> ${GREEN}PASSED${NC}"
    else
        echo -e "- Cache feature | Restart loop with UUTS different tests --> ${RED}FAILED${NC}"
        result=1
    fi
else
    echo -e "- Cache feature | Restart loop with UUTS different tests / INITIALIZATION --> ${RED}FAILED${NC}"
    result=1
fi

exit $result
