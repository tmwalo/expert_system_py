# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 10:38:28 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/27 10:38:30 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Operations:

	def __init__(self):
		self.num_of_operators = 6
		self.negation_precedence = 5
		self.and_precedence = 4
		self.or_precedence = 3
		self.xor_precedence = 2
		self.implies_precedence = 1
		self.iff_precedence = 0
	
	def and_op(self, fact_a, fact_b):
		return fact_a and fact_b

	def negate_op(self, fact_a):
		return (not fact_a)

	def or_op(self, fact_a, fact_b):
		return fact_a or fact_b

	def precedence(self, operator):
		if operator == "!":
			return self.negation_precedence
		elif operator == "+":
			return self.and_precedence
		elif operator == "|":
			return self.or_precedence
		elif operator == "^":
			return self.xor_precedence
		elif operator == "=>":
			return self.implies_precedence
		elif operator == "<=>":
			return self.iff_precedence
		else:
			return (-1)

	def xor_op(self, fact_a, fact_b):
		return fact_a ^ fact_b
