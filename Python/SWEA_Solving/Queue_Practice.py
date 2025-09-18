from collections import deque
import sys
sys.stdin = open('input.txt')


def enqueue(val):
    my_deque.append(val)
    return


def dequeue():
    if len(my_deque) == 0:
        rtn_val = -1
    else:
        rtn_val = my_deque.popleft()
    return rtn_val


def size():
    return len(my_deque)


def is_empty():
    if len(my_deque) == 0:
        rtn_val = 1
    else:
        rtn_val = -1
    return rtn_val


def front():
    if len(my_deque) == 0:
        rtn_val = -1
    else:
        rtn_val = my_deque[0]
    return rtn_val


def rear():
    if len(my_deque) == 0:
        rtn_val = -1
    else:
        rtn_val = my_deque[-1]
    return rtn_val


N = int(input())
my_deque = deque()

for _ in range(N):
    func = input().split()

    if func[0] == 'enqueue':
        enqueue(int(func[1]))

    elif func[0] == 'dequeue':
        print(dequeue())

    elif func[0] == 'size':
        print(size())

    elif func[0] == 'isEmpty':
        print(is_empty())

    elif func[0] == 'front':
        print(front())

    elif func[0] == 'rear':
        print(rear())
