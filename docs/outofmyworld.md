# Some questions are meant to be practiced again and again.


## **Questions**

1. **Prefix Sum & Hash Map**:
    - [560 Subarray Sum Equals k](https://leetcode.com/problems/subarray-sum-equals-k/description/)
        - **Hint**: at some index `x`, subarray will start. So, subtract `k` from current prefix sum and check if that number occured in the past. You will find a subarray starting at `x`. Thank me later.

    - [974 Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/description/)
        - **Hint**: try to find modulas (prefix % k) from the prefix count map / dict.

    - [523 Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/description/)
        - **Hint**: check if remainder already exists, if exists means that from that index we have added the same sum as k to the prefix. Hurray! you got your answer.

    - [525 Contiguous Array](https://leetcode.com/problems/contiguous-array/description/)
        - **Hint**: add 1 if num is 1 else subtract 1. Now, figure out, think a little harder, why the hell these nubers are same sometimes, it means between these indexes, a subarray exists which has same number of 1s and 0s which cancel the sum.