import re 
def is_palindrome(s):
    if not s:
        return None
    cleaned_S = re.sub(r'[^a-zA-Z0-9]', '' , s).lower()
    return cleaned_S == cleaned_S[::-1]

# Example function calls
print(is_palindrome("racecar"))  # Should return True
print(is_palindrome("codedamn"))  # Should return False
print(is_palindrome(""))         # Should return None
print(is_palindrome("A man, a plan, a canal: Panama"))  # Should return True
print(is_palindrome("No lemon, no melon"))              # Should return True
