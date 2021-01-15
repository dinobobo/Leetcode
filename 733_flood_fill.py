# Recursive

class Solution:
    D = [0, 1, 0, -1, 0]

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        else:
            old_color = image[sr][sc]
            image[sr][sc] = newColor
            for i in range(4):
                if 0 <= sr + self.D[i] < len(image) and 0 <= sc + self.D[i + 1] < len(image[0]) and image[sr + self.D[i]][sc + self.D[i + 1]] == old_color:
                    self.floodFill(
                        image, sr + self.D[i], sc + self.D[i + 1], newColor)
        return image

# BFS?
