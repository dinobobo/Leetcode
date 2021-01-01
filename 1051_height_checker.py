# The easiest solution is to sort the array and compare the height outliers

# Because the heights are limited to 100 per the description, we can actually do
# a counting sort. Imaging an example of [1,1,2,1,4,1], the Hashmap of heights will be
# [1:3, 2: 1, 3: 0, 4: 1] and this is just another representation of the sorted array,
# but it requires less time to generate the Hashmap. Now we can just traverse the nums array
# and check if it matches the key. The value of each key will decrement upon a comparison
from collections import defaultdict


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heightHash = defaultdict(int)
        for height in heights:
            heightHash[height] += 1
        # Convert to list
        height_list = sorted(
            [[i, j] for i, j in heightHash.items()], key=lambda x: x[0])
        ans = 0
        cur_height = 0
        for height in heights:
            if height_list[cur_height][1] == 0:
                cur_height += 1
            if height != height_list[cur_height][0]:
                ans += 1
            height_list[cur_height][1] -= 1
        return ans

# Alternatively, we can always use an array to represent the Hashmap, which will
# reduce the memory usage by a lot. Try it next time!
