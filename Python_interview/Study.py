class Solution(object):
    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = []
        #making strs
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        #isPalindrome?
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True
    
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Using Deque
        import collections
        strs = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
        
    
    def isPalindrome3(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Using slicing
        s = s.lower()
        #regular expression
        import re
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]


    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseString2(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
    
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, digits = [], []
        for log in logs :
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        return letters + digits
    
    
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        import collections
        words = [word for word in re.sub(r'[^\w]',' ', paragraph)\
                 .lower().split() if word not in banned]
        
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
    
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
    
    
    
    
    
    
    
    
    
    
    
    