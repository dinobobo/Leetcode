# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
# Careful with the if statement order!!! Even if the coordinates are marked cleaned, the bot
# can still move over. So we have to check the cleaned first and check if it can move.
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def move_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def helper(direction, coords):
            robot.clean()
            cleaned.add(coords)
            for _ in range(4):
                next_coords = (coords[0] + moves[direction]
                               [0], coords[1] + moves[direction][1])
                if not next_coords in cleaned and robot.move():
                    helper(direction, next_coords)
                    move_back()
                direction = (direction + 1) % 4
                robot.turnRight()

        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        cleaned = set()
        helper(0, (0, 0))
