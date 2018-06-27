# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    validator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 10:39:01 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/27 10:39:06 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Validator:

	def is_fact(self, operator):
		return (len(operator) == 1) and (operator.isupper())

	def is_negation(self, operator):
		return operator == "!"

	def is_and(self, operator):
		return operator == "+"

	def is_or(self, operator):
		return operator == "|"

	def is_xor(self, operator):
		return operator == "^"

	def is_imply(self, operator):
		return operator == "=>"

	def is_iff(self, operator):
		return operator == "<=>"

	def is_left_bracket(self, operator):
		return operator == "("

	def is_right_bracket(self, operator):
		return operator == ")"
	
	def is_operator(self, operator):
		if self.is_negation(operator):
			return True
		elif self.is_and(operator):
			return True
		elif self.is_or(operator):
			return True
		elif self.is_xor(operator):
			return True
		else:
			return False

	def is_left_associative(self, operator):
		if (not self.is_operator(operator)) or (self.is_negation(operator)):
			return False
		else:
			return True
