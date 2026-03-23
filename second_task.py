class myStack:
    def __init__(self):
        self.myItems = []

    def push(self, value):
        self.myItems.append(value)

    def isEmpty(self):
        return len(self.myItems) == 0

    def pop(self):
        if not self.isEmpty():          
            return self.myItems.pop()
        else:
            return None

    def topElem(self):
        if self.isEmpty():
            return None
        return self.myItems[-1]

    def myLen(self):
        return len(self.myItems)


def mySort(stack):
    copy = myStack()
    while not stack.isEmpty():
        x = stack.pop()                  
        while not copy.isEmpty() and copy.topElem() < x:
            temp = copy.pop()
            stack.push(temp)

        copy.push(x)
        while not stack.isEmpty() and stack.topElem() < x:
            temp = stack.pop()
            copy.push(temp)

    return copy

def stackFromList(lst):
    s = myStack()
    for item in lst:
        s.push(item)
    return s

def stackToList(s):
    return s.myItems[:]

s = stackFromList([1, 2, 3, 4, 5])
result = mySort(s)
assert stackToList(result) == [5, 4, 3, 2, 1]


s = stackFromList([3, 1, 3, 2, 1])
result = mySort(s)
assert stackToList(result) == [3, 3, 2, 1, 1]   

print("Успех!")