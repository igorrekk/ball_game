class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def get_node(head, k):
    current = head
    count = 1
    while count < k:
        current = current.next
        count += 1
    return current

def build_spisok(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

class Iterator:
    def __init__(self, items):
        self.items = items
        self.forward = True
        self.index = 0

    def reverse(self):
        self.forward = not self.forward
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration

        if self.forward:
            item = self.items[self.index]
        else:
            item = self.items[-(self.index + 1)]

        self.index += 1
        return item
values = [10, 20, 30, 40, 50]
head = build_spisok(values)

k = int(input("Введите k (между 1 и 5): "))
k_node = get_node(head, k)
print(f"{k}-й элемент списка:", k_node.value)

iterator = Iterator(values)

print("Прямой обход:")
for item in iterator:
    print(item)

iterator.reverse()

print("Обратный обход:")
for item in iterator:
    print(item)


