def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1  

        char_set.add(s[right])  
        max_length = max(max_length, right - left + 1)

    return max_length

print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("bbbbb"))     
print(length_of_longest_substring("pwwkew"))    