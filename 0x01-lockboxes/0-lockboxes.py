#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    unlocked = set([0])
    stack = list(boxes[0])

    while stack:
        key = stack.pop()
        if 0 <= key < n and key not in unlocked:
            unlocked.add(key)
            stack.extend(boxes[key])

    return len(unlocked) == n
