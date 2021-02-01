class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.used = set()
        self.unused = set([i for i in range(maxNumbers)])

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.unused:
            num = self.unused.pop()
            self.used.add(num)
            return num
        else:
            return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return number in self.unused

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.used:
            self.used.remove(number)
            self.unused.add(number)


# Only one set is required!

# Use array, the value in the array is the pointer.
# Remember to round the pointer
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.next = [(i + 1) % maxNumbers for i in range(maxNumbers)]
        self.p = 0

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.next[self.p] == -1:
            return -1
        else:
            num = self.p
            self.p = self.next[self.p]
            self.next[num] = -1
            return num

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return self.next[number] != -1

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if self.next[number] == -1:
            self.next[number] = self.p
            self.p = number
