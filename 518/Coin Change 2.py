class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = (amount+1)*[0]
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                if coin <= i:
                    dp[i] += dp[i-coin]
            
        return dp[-1]
    