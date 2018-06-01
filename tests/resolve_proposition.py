class ResolveProposition:

	def execute_stack_operation(self, operator_stack, fact_stack):
		if (operator_stack.count == 0) or (fact_stack.count == 0):
			return False
		operator_value = operator_stack.pop()
		fact = fact_stack.pop()
		validate = Validator()
		operation = Operations()
		if validate.is_negation(operator_value):
			result = operation.negate(fact)
			fact_stack.append(result)
			return True
		if fact_stack.count == 0:
			return False
		if validate.is_and(operator_value):
			result = operation.and_op(fact_stack.pop(), fact)
			fact_stack.append(result)
		else if validate.is_or(operator_value):
			result = operation.or_op(fact_stack.pop(), fact)
			fact_stack.append(result)
		else if validate.is_xor(operator_value):
			result = operation.xor_op(fact_stack.pop(), fact)
			fact_stack.append(result)
		else
			return False
		return True

	def resolve(self, proposition, facts):
		operator_stack = []
		fact_stack = []
		validate = Validator()
		ops = Operations()
		for token in proposition:
			if validate.is_fact(token):
				fact_stack.append(facts.atoms[token])
			else if validate.is_operator(token):
				while ((operator_stack.count > 0) and (not validate.is_left_bracket(operator_stack[-1])) and ((ops.precedence(operator_stack[-1]) > ops.precedence(token)) or ((ops.precedence(operator_stack[-1]) == ops.precedence(token)) and (validate.is_left_associative(token))))):
					self.execute_stack_operation(operator_stack, fact_stack)
					operator_stack.append(token)
			else if validate.is_left_bracket(token):
				operator_stack.append(token)
			else if validate.is_right_bracket(token):
				while (operator_stack.count > 0) and (not validate.is_left_bracket(operator_stack[-1])):
					self.execute_stack_operation(operator_stack, fact_stack)
				if (operator_stack.count > 0) and (validate.is_left_bracket(operator_stack[-1])):
					operator_stack.pop()
				else:
					raise Exception("Left bracket missing")
		while operator_stack.count > 0:
			self.execute_stack_operation()
		if fact_stack.count > 1:
			raise Exception("Missing operator")
		return fact_stack.pop()
