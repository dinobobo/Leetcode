class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = l + (r - l)//2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if l < len(letters):
            return letters[l]
        else:
            return letters[0]
