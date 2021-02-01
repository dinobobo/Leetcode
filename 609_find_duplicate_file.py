from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # dictonary {content: full path}
        file_dic = defaultdict(list)
        for i in paths:
            res = i.split()
            root_path = res[0]
            files = res[1:]
            for file in files:
                unpack = file.split('(')
                rel_path = unpack[0]
                content = unpack[1].replace(')', '')
                file_dic[content].append(root_path + '/' + rel_path)
        ans = []
        for val in file_dic.values():
            if len(val) > 1:
                ans.append(val)
        return ans


'''
Follow ups:
* Imagine you are given a real file system, how will you search files? DFS or BFS?
    - DFS is more memory efficient. 
    - BFS can utilize the file locality.
* If the file content is very large (GB level), how will you modify your solution?
    - Hash with the size
    - Hash them with a checksum like algorithm? MD5/SHA256
    - Compare byte by byte
* If you can only read the file by 1kb each time, how will you modify your solution?
    - Compare the hash chunk by chunk. Make the hash result a vector.
* What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
    - O(N*k). Hashing. A faster Hash function
* How to make sure the duplicated files you find are not false positive?
    - If the meta data yield the same hash, which is probably unlikely start to compare the entire data byte by byte.
'''
