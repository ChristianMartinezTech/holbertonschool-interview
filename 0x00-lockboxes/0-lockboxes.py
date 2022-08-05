#!/usr/bin/python3

"""You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and each box may contain keys
to the other boxes.

Write a method that determines if all the boxes can be opened.
- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
  There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False

the main_0.py function will call this one. Check it for reference.

https://stackoverflow.com/questions/63024056/lockboxes-problem-list-inside-a-list-and-each-list-contains-keys-to-unlock-the
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    if boxes is None or len(boxes) is 0:
        return False

    unlocked = [0]
    for id, _box_ in enumerate(boxes):
        if not _box_:
            continue
        for key in _box_:
            if key < len(boxes) and key not in unlocked and key != id:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True

    return False
