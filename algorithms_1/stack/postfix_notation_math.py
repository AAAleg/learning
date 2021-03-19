from stack import Stack

OPERATORS = {
	'+': lambda x, y: x + y,
	'*': lambda x, y: x * y,
	'=': lambda x: x
}

def calculate(expression):
	numbers = Stack()
	ops = Stack()

	for symbol in expression[::-1].split(' '):
		
		if symbol in OPERATORS.keys():
			ops.push(symbol)
		else:
			numbers.push(int(symbol))

	while ops.size() != 0:
		operator = ops.pop()

		if operator == '=':
			result = numbers.pop()
			return result
		else:
			right = numbers.pop()
			left = numbers.pop()

			result = OPERATORS[operator](right, left)
			numbers.push(result)

	if numbers.size() != 0:
		return numbers.pop()
