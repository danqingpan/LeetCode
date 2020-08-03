# Principle
This problem requires brute force method to search every possibilities.

# Sovling step:
1. Turn bank into a set to make search faster
2. Use a set to restore seen patterens
3. Check every possible variation of the current gene. There are 8x4 choices.
4. If a choice is in bank but not seen, we that test it.

# Conclusion
Heavily rely on set.
