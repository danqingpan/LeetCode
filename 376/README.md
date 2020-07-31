# Princple
This is another dynamic programming program. This problem is close to longest subsequence problem. However, this problem asked us to find the longest wiggle subsequence. I used two list to solve it.

## Solving steps
1. Create large dp list to hold the longest wiggle length at position i when nums[i] is the large number. It is always after a small value.
2. Create small dp list to hold the longest wiggle length at position i when nums[i] is the small number. It is always after a large value.
