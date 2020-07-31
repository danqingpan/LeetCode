# Principle
This is a classic DP problem. The value in position dp[i] is the sum of previous accessible values.

## Sovling Steps
1. We have to create a DP. Since we have target and we want to ensure that dp[target] do exist, the length should be target+1.  
2. For each position i, we want to check all position i - nums[j] and sum the values.

## Conclusion
Take care of the boundary conditions.
