class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence=""
        for i in s:
            if i.isalnum():
                sentence=sentence+i.lower()
        reverse=sentence[::-1]
        if(reverse==sentence):
            return True
        else:
            return False