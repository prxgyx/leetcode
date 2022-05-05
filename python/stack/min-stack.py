class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class MinStack:
	def __init__(self):
		self.head = Node("head")
		self.size = 0
	def push(self, val: int) -> None:
		temp = Node(val)
		temp.next = self.head.next
		self.head.next = temp
		self.size += 1
	def pop(self) -> None:
		if self.size == 0:
			print("Popping from an empty stack")
		else:
			popped_node = self.head.next
			self.head.next = self.head.next.next
			self.size-=1
			print(popped_node.value)
	def top(self) -> int:
		if self.size == 0:
			print("No top of an empty stack")
		else:
			top_node = self.head.next
			return(top_node.value)
	def getMin(self) -> int:
		current = self.head.next
		min_val = current.value
		while  current.next:
			current = current.next
			min_val = min(current.value, min_val)
		return min_val

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()