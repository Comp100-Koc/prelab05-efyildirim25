def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    maximum_len=""
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i:j+1]==s[i:j+1][::-1] and len(s[i:j+1])>len(maximum_len):
                    maximum_len=s[i:j+1]          
    return maximum_len
