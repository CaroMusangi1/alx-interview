#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    unlocked = set([0])  # Set of unlocked boxes, start with the first box
    stack = list(boxes[0])  # Keys from the first box

    while stack:
        key = stack.pop()
        if 0 <= key < n and key not in unlocked:  # Valid and not yet unlocked
            unlocked.add(key)  # Mark the box as unlocked
            stack.extend(boxes[key])  # Add all keys from the newly unlocked box to stack

    return len(unlocked) == n  # True if all boxes are unlocked
