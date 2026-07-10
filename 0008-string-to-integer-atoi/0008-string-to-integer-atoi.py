class Solution:
    def myAtoi(self, s):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        i = 0
        n = len(s)
        
        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: determine sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: read digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1
            
            # Early clamp to avoid huge number buildup (keeps it well within
            # int range at every step, no 64-bit storage needed)
            if sign == 1 and num > INT_MAX:
                num = INT_MAX
                break
            if sign == -1 and -num < INT_MIN:
                num = -INT_MIN  # will be negated below, clamped to INT_MIN
                break
        
        num *= sign
        
        # Step 4: clamp to range (safety net, in case loop exited without clamp)
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num


# ---- Test cases ----
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.myAtoi("42"))              # Expected: 42
    print(sol.myAtoi("   -042"))         # Expected: -42
    print(sol.myAtoi("1337c0d3"))        # Expected: 1337
    print(sol.myAtoi("0-1"))             # Expected: 0
    print(sol.myAtoi("words and 987"))   # Expected: 0
    print(sol.myAtoi(""))                # Expected: 0
    print(sol.myAtoi("   "))             # Expected: 0
    print(sol.myAtoi("+1"))              # Expected: 1
    print(sol.myAtoi("-91283472332"))    # Expected: -2147483648
    print(sol.myAtoi("91283472332"))     # Expected: 2147483647
    print(sol.myAtoi("3.14159"))         # Expected: 3
    print(sol.myAtoi("+-12"))            # Expected: 0
    print(sol.myAtoi("  +  413"))        # Expected: 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna