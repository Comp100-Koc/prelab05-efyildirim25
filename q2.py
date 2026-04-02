def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    def any_adjacent_duplicates(s):
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                return True
        return False
    if any_adjacent_duplicates(s)==False:
        return s
    while any_adjacent_duplicates(s):
        res=""
        i=0
        while i<len(s):
            if i<len(s)-1 and s[i]==s[i+1]:
                i+=2
            else:
                res+=s[i]
                i+=1
        s=res
    return res

