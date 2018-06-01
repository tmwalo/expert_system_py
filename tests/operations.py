class Operations:

	def negate(self, fact_a):
		return (not fact_a)

	def and(self, fact_a, fact_b):
		return fact_a and fact_b

	def or(self, fact_a, fact_b):
		return fact_a or fact_b

	def xor(self, fact_a, fact_b):
		return fact_a ^ fact_b
