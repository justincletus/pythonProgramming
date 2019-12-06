class StackProgram:
    max = 10
    top = -1
    items = []

    def pushItem(self, n):
        self.top  +=1
        self.items[self.max - 1]
        if len(self.items) == 0:
            self.items = n
            return self.items
        else:
            return 'stack is full'


new_item = StackProgram()
new_item.pushItem(10)
new_item.pushItem(5)
new_item.pushItem(2)
new_item.pushItem(10)
new_item.pushItem(5)
new_item.pushItem(2)
new_item.pushItem(10)
new_item.pushItem(5)
new_item.pushItem(2)
new_item.pushItem(10)
new_item.pushItem(5)

# print(new_item.len(items))
