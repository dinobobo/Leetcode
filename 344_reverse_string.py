class Solution:
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        def helper(start, end):
            if start >= end:
                return

            # swap the first and last element
            s[start], s[end] = s[end], s[start]

            return helper(start+1, end-1)

        helper(0, len(s)-1)
