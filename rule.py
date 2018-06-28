# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rule.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 10:38:51 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/27 15:12:28 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from validator import Validator

class Rule:

	def __init__(self, rule):
		self.rule = rule
		self.antecedent = None
		self.antecedent_atoms = None
		self.consequent = None
		self.consequent_atoms = None
	
	def get_antecedent(self):
		if not self.antecedent:
			self.antecedent = (self.rule.split("=>"))[0]
			self.antecedent = self.antecedent.strip()
		return self.antecedent
	
	def get_antecedent_atoms(self):
		if not self.antecedent_atoms:
			atoms = []
			validate = Validator()
			for token in self.get_antecedent():
				if validate.is_fact(token):
					atoms.append(token)
			self.antecedent_atoms = atoms
		return self.antecedent_atoms

	def get_consequent(self):
		if not self.consequent:
			self.consequent = (self.rule.split("=>"))[1]
			self.consequent = self.consequent.strip()
		return self.consequent
	
	def get_consequent_atoms(self):
		if not self.consequent_atoms:
			atoms = []
			validate = Validator()
			for token in self.get_consequent():
				if validate.is_fact(token):
					atoms.append(token)
			self.consequent_atoms = atoms
		return self.consequent_atoms
