# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # Initialize answer mat to -1
        ans = [[-1] * len(mat[0]) for i in range(len(mat))]
        # Create set of all zero cordinates
        zeroset = set()
        for i in range(len(mat)):
            for j, cell in enumerate(mat[i]):
                if cell == 0:
                    zeroset.add((i, j))
        # Set distance in answer mat of zero's to 0
        for cord in zeroset:
            ans[cord[0]][cord[1]] = 0
        # Iterate through zero set setting all cells n distance from zero to correct value
        dist = 1
        updated_cell = False

        def checkCell(x, y):
            # Check bounds of cordinates
            if x < 0 or y < 0 or x >= len(mat) or y >= len(mat[0]):
                return
            # If cell is not -1 it is as close or closer to a different zero
            elif ans[x][y] == -1:
                ans[x][y] = dist
                self.updated_cell = True
        while zeroset:
            toremove = set()
            for cord in zeroset:
                self.updated_cell = False
                for offset in range(dist):
                    # For each offset there are 4 cells that distance from the 0
                    # Right / Up
                    x = cord[0]+dist-offset
                    y = cord[1]+offset
                    checkCell(x, y)
                    # Left / Down
                    x = cord[0]-dist+offset
                    y = cord[1]-offset
                    checkCell(x, y)
                    # Up / Left
                    x = cord[0]-offset
                    y = cord[1]+dist-offset
                    checkCell(x, y)
                    # Down / Right
                    x = cord[0]+offset
                    y = cord[1]-dist+offset
                    checkCell(x, y)
                # Remove zero from set if it is not the closest zero to any cell
                if self.updated_cell is False:
                    toremove.add(cord)
            zeroset.difference_update(toremove)
            dist += 1
        return ans
