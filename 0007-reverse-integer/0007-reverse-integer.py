class Solution:
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for overflow before actually updating rev
            if rev > (INT_MAX - digit) // 10:
                return 0
            
            rev = rev * 10 + digit
        
        rev *= sign
        
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        
        return rev


# ---- Test cases ----
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.reverse(123))          # Expected: 321
    print(sol.reverse(-123))         # Expected: -321
    print(sol.reverse(120))          # Expected: 21
    print(sol.reverse(0))            # Expected: 0
    print(sol.reverse(1534236469))   # Expected: 0 (overflow)
    print(sol.reverse(-2147483648)) # Expected: 0 (overflow)
    print(sol.reverse(1463847412))  # Expected: 2147483641

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna