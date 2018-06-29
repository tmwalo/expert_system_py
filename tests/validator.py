# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    validator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 10:39:01 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/28 17:12:46 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import resolve_proposition
from facts import Facts
import sys

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

	def is_rule(self, line):
		hash_index = line.find("=>")
		if hash_index == (-1):
			return False
		line = self.remove_comment(line)
		split_sides = line.split("=>")
		antecedent = split_sides[0]
		consequent = split_sides[1]
		if (not antecedent) or (not consequent):
			return False
		resolver = resolve_proposition.ResolveProposition()
		facts = Facts()
		try:
			resolver.resolve(antecedent, facts)
			resolver.resolve(consequent, facts)
		except:
			sys.stderr.write("Syntax error")
			return False
		return True

        def is_fact_init(self, line):
            line = self.remove_comment(line)
            if len(line) == 0:
                return False
            for index in range(len(line)):
                if (index == 0):
                    if (line[index] != "="):
                        return False
                else:
                    if (not self.is_fact(line[index])):
                        return False
            return True

        def is_query_init(self, line):
            line = self.remove_comment(line)
            if len(line) == 0:
                return False
            for index in range(len(line)):
                if (index == 0):
                    if (line[index] != "?"):
                        return False
                else:
                    if (not self.is_fact(line[index])):
                        return False
            return True

        def remove_comment(self, line):
            hash_index = line.find("#")
            if hash_index == (-1):
                return (line)
            return (line[0:hash_index])
