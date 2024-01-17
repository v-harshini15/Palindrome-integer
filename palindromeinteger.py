def isPalindrome(x):
    # Handle negative numbers and multiples of 10
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0

    # Reverse the second half of the number
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # If the number of digits is odd, remove the middle digit from reversed_half
    if x == reversed_half or x == reversed_half // 10:
        return True
    else:
        return False

# Example
print(isPalindrome(12121))  # Output: True
print(isPalindrome(123))    # Output: False
