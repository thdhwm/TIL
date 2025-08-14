from collections import deque
S = deque(list(input()))
stacks = deque([])
tags = deque([])
temp = []
priority = {' ': 2, '<': 0, '>': 1}

while S:
    while not tags:
        if S[0] not in [' ', '<', '>']:
            char = S.popleft()
            temp.append(char)

        else:
            tags.append(S.popleft())





        # while tags and priority[tags[-1]] >= priority[char]:
        #     stacks.append(tags.pop())
        #
        # stacks.append(tags.pop())

