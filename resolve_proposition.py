# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    resolve_proposition.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 10:38:40 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/28 10:16:35 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import validator
from operations import Operations

class ResolveProposition:

	def execute_stack_operation(self, operator_stack, fact_stack):
		if (len(operator_stack) == 0) or (len(fact_stack) == 0):
			return False
		operator_value = operator_stack.pop()
		fact = fact_stack.pop()
		validate = validator.Validator()
		if (not validate.is_operator(operator_value)) or (not isinstance(fact, bool)):
			return False
		operation = Operations()
		if validate.is_negation(operator_value):
			result = operation.negate_op(fact)
			fact_stack.append(result)
			return True
		if len(fact_stack) == 0:
			return False
		if validate.is_and(operator_value):
			result = operation.and_op(fact_stack.pop(), fact)
			fact_stack.append(result)
		elif validate.is_or(operator_value):
			result = operation.or_op(fact_stack.pop(), fact)
			fact_stack.append(result)
		elif validate.is_xor(operator_value):
			result = operation.xor_op(fact_stack.pop(), fact)
			fact_stack.append(result)
		else:
			return False
		return True

	def resolve(self, proposition, facts):
		operator_stack = []
		fact_stack = []
		validate = validator.Validator()
		ops = Operations()
		for token in proposition:
                        if token == ' ':
                            continue
			if validate.is_fact(token):
				fact_stack.append(facts.atoms[token])
			elif validate.is_operator(token):
				while ((len(operator_stack) > 0) and (not validate.is_left_bracket(operator_stack[-1])) and ((ops.precedence(operator_stack[-1]) > ops.precedence(token)) or ((ops.precedence(operator_stack[-1]) == ops.precedence(token)) and (validate.is_left_associative(token))))):
					if not self.execute_stack_operation(operator_stack, fact_stack):
						raise Exception("Stack operation failed")
				operator_stack.append(token)
			elif validate.is_left_bracket(token):
				operator_stack.append(token)
			elif validate.is_right_bracket(token):
				while (len(operator_stack) > 0) and (not validate.is_left_bracket(operator_stack[-1])):
					if not self.execute_stack_operation(operator_stack, fact_stack):
						raise Exception("Stack operation failed")
				if (len(operator_stack) > 0) and (validate.is_left_bracket(operator_stack[-1])):
					operator_stack.pop()
				else:
					raise Exception("Left bracket missing")
			else:
				raise Exception("Unknown token")
		while len(operator_stack) > 0:
			if not self.execute_stack_operation(operator_stack, fact_stack):
				raise Exception("Stack operation failed")
		if len(fact_stack) > 1:
			raise Exception("Missing operator")
		return fact_stack.pop()
