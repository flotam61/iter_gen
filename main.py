nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]



class FlatIterator:

	def __init__(self, my_list):
		self.my_list = sum(my_list, [])


	def __iter__(self):
		self.cursor =- 1
		return self


	def __next__(self):
		self.cursor += 1
		if self.cursor == len(self.my_list):
			raise StopIteration
		element = self.my_list[self.cursor]
		return element


for item in FlatIterator(nested_list):
	print(item)

def flat_generator(my_list):
	cursor = 0
	my_list = sum(my_list, [])
	while cursor < len(my_list):
		yield my_list[cursor]
		cursor += 1

for item in flat_generator(nested_list):
	print(item)
