from collections import deque

numbers = [int(num) for num in input().split(" ")]
stack = deque(numbers)

print(stack)

for i in range(len(stack)):
    print(stack.pop() * 2)