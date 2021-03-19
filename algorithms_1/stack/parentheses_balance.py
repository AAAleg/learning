from stack import Stack


def parentheses_balance(string):
	s = Stack()

	for symbol in string:
		if symbol == '(':
			s.push(symbol)
		else:
			if s.size() == 0:
				return False
			else:
				s.pop()

	return s.size() == 0