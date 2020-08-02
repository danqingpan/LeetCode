# Principle
This problem require us to divide a set of numbers into two of which the sum are the same. Another form is whether we can find a subset which sums to half of the total sum.  
Specifically, for each number in the list, we mark which sum number it can access.

# Solving Steps
1. Calculate the total sum of the number list.  
2. Use dynamic programming to find where there exists a subset add to half the total sum.

# Conclusion
Since each number in the list can only be used once, we should firstly visit these numbers.
