#!/bin/bash

declare -i result
result=0

va=$(wooqi --seq-config testing/range_feature/range_with_2_args.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Range feature | 2 args --> ${GREEN}PASSED${NC}"
else
    echo -e "- Range feature | 2 args --> ${RED}FAILED${NC}"
    result=1
fi

va=$(wooqi --seq-config testing/range_feature/range_with_3_args.ini --sn wooqi_tests -s)

echo -e $va | grep --quiet "TEST PASSED"
if [ $? = 0 ];then
    echo -e "- Range feature | 3 args --> ${GREEN}PASSED${NC}"
else
    echo -e "- Range feature | 3 args --> ${RED}FAILED${NC}"
    result=1
fi

exit $result
