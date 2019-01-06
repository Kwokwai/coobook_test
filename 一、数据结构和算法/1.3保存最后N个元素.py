from collections import deque


def search(lines, pattern, history=5):
    previous_lines =deque(maxlen=history)
    for line in lines:
        if pattern in line :
            yield line, previous_lines
        previous_lines.append(line)



# # Example use on a file
# if __name__ == '__main__':
#     with open('somefile.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('-'*20)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)

print(q)

q1 = deque()
q1.append(1)
q1.append(2)
q1.append(3)
print(q1)
q1.appendleft(4)
print(q1)
print(q1.pop())
print(q1)
print(q1.popleft())