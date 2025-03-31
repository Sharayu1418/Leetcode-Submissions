class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        
        sharing = 0
        for day in range(2, n + 1):
            new_sharers = dp[day - delay] if day - delay > 0 else 0
            forgotten = dp[day - forget] if day - forget > 0 else 0
            
            sharing = (sharing + new_sharers - forgotten) % MOD
            dp[day] = sharing
        
        result = 0
        for i in range(n - forget + 1, n + 1):
            if i > 0:
                result = (result + dp[i]) % MOD
                
        return result