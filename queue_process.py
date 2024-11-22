from collections import deque

words = input("").split()
queue = deque()
for value in words:
    queue.appendleft(value)
print(queue)

for i in range(len(queue)):
    word = queue.pop()
    if 'a' in word:
        print(word)