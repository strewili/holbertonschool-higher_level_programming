#!/usr/bin/python3
"""Defines a CountedIterator class to track item iterations."""


class CountedIterator:
    """An iterator that keeps track of the number of iterated items."""

    def __init__(self, iterable):
        """Initialize with an iterable object and a counter."""
        self.iterator = iter(iterable)
        self.__counter = 0

    def get_count(self):
        """Return the current iteration count."""
        return self.__counter

    def __next__(self):
        """Increment the counter and fetch the next item."""
        try:
            item = next(self.iterator)
            self.__counter += 1
            return item
        except StopIteration:
            raise StopIteration


# كود الفحص والاختبار (Test)
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry"]
    counted_iter = CountedIterator(my_list)

    print(next(counted_iter))
    print(next(counted_iter))
    print(f"Current count: {counted_iter.get_count()}")

    print(next(counted_iter))
    print(f"Final count: {counted_iter.get_count()}")

    try:
        next(counted_iter)  # سيطلق خطأ انتهاء التكرار القياسي
    except StopIteration:
        print("Reached the end of iterator.")