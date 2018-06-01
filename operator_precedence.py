class OperatorPrecedence:

	def __init__(self):
		self.num_of_operators = 6
		self.negation_op = 5
		self.and_op = 4
		self.or_op = 3
		self.xor_op = 2
		self.implies_op = 1
		self.iff_op = 0
	
	def get(self, operator):
		if operator == "!":
			return self.negation_op
		else if operator == "+":
			return self.and_op
		else if operator == "|":
			return self.or_op
		else if operator == "^":
			return self.xor_op
		else if operator == "=>":
			return self.implies_op
		else if operator == "<=>":
			return self.iff_op
		else:
			return (-1)
