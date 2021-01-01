# Two pointers coming from 0 and we know the numbers between i and j
# have to be odd, so just keep swapping if A[j] is odd
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = 0
        for cur in range(len(A)):
            if A[cur] % 2 == 0:
                A[even], A[cur] = A[cur], A[even]
                even += 1
        return A


# Similar to Quicksort. Two pointers coming to the opposite ends of
# the array. Swap if we found A[begin] to be odd

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        begin = 0
        end = len(A) - 1
        while end > begin:
            if A[begin] % 2 == 1:
                A[begin], A[end] = A[end], A[begin]
                if A[begin] % 2 == 0:  # Actually checking A[end] since they are swapped in the previous step
                    begin += 1
                end -= 1
            else:
                begin += 1
        return A
