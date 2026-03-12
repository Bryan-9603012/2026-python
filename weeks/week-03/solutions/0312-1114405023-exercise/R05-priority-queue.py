import heapq

class PriorityQueue:
    def __init__(self):
        self.__queue =[]
        self.__index = 0
    def push(self, item,priority):
        heapq.heappush(self.__queue,(-priority,self.__index,item))
        self.__index += 1
    def pop(self):
        return heapq.heappop(self.__queue)[-1]

print("Priority Queue")
q = PriorityQueue()
q.push("task1",1)
q.push("task2",2)
q.push("task3",3)
print(q.pop())
print(q.pop())
print(q.pop())
