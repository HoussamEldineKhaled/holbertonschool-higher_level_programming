#!/usr/bin/python3


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        length_original = len(self)
        super().extend(iterable)
        length_changed = len(self)
        answer = length_changed - length_original
        print("Extended the list with [{}] items.".format(answer))

    def remove(self, item):
        print("Removed {} from the list.")
        super().remove(item)

    def pop(self, index = -1):
        if len(self) > 0:
            item = self[index]
        else:
            item = None
        result = super().pop(index)
        print("Popped [{}] from the list.".format(result))
        return result
