# Use a dictionary to record the occurance of the temperature from the end of T
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        next_warm = {}  # temp:index
        ans = [0]*len(T)

        for i in range(len(T) - 1, -1, -1):
            warm = float('inf')
            for temp in next_warm:
                if temp > T[i]:
                    warm = min(next_warm[temp], warm)
            if warm != float('inf'):
                ans[i] = warm - i
            next_warm[T[i]] = i
        return ans


# Stack
# For a forward traversal, at T[i], if there is a T[i + k] > T[i], then any later temperatures that
# are lower than T[i + k] won't matter anymore. Now, if we traversal backwards, we keep a stack that is
# in strickly decreasing order. (pop all the elements that is < T[curr], since this element will be added
# into the stack and the earlier smaller elements won't matter anymore.)
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while len(stack) != 0 and T[stack[-1]] <= T[i]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

# Forward traversal


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        stack = []
        for i, t in enumerate(T):
            while len(stack) and t > T[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans

# Just track with indices instead of using stack?
