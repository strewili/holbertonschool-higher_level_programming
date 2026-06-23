#!/usr/bin/python3
"""Defines a VerboseList class that extends the built-in list."""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Append an item and notify."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and notify with the count of added items."""
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """Notify before removing an item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Notify before popping an item."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)


# كود الفحص والاختبار (Test)
if __name__ == "__main__":
    v_list = VerboseList()
    v_list.append(10)
    v_list.extend([20, 30, 40])
    v_list.remove(20)
    v_list.pop()