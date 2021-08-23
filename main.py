class LIFO(list):
    def __init__(self):
        super().__init__(self)
    def size(self):
        return len(self)
    def is_empty(self):
        return self.size() < 1
    def push(self, item):
        self.append(item)
    def pop(self):
        super().pop(self.size() - 1)
    def peek(self):
        return self[self.size() - 1]

def check_balance(str):
    #Постоянные
    OPEN = ['(', '[', '{']
    CLOSE = ['}', ']', ')']
    CLS = LIFO()

    if len(str) % 2 > 0:
        return print('несбалансировано')
    for i, char in enumerate(str):
        if char in OPEN:
            CLS.push(char)
        elif char in CLOSE:
            if CLS.is_empty():
                return print('несбалансрировано')
            elif OPEN.index(CLS.peek()) != CLOSE.index(char):
                return print('несбалансировано')
            else:
                CLS.pop()
                if CLS.is_empty() and i == len(str)-1:
                    return print('сбалансировано')

if __name__ == '__main__':
    check_balance(input())
