class Operations:

	def negate_op(self, fact_a):
		return (not fact_a)

	def and_op(self, fact_a, fact_b):
		return fact_a and fact_b

	def or_op(self, fact_a, fact_b):
		return fact_a or fact_b

	def xor_op(self, fact_a, fact_b):
		return fact_a ^ fact_b
