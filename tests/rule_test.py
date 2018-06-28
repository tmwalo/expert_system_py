from rule import Rule

formula = Rule("	A +  B => C	 ")
print("rule: {}".format(formula.rule))
print("antecedent: {}".format(formula.get_antecedent()))
print("antecedent atoms: {}".format(formula.get_antecedent_atoms()))
print("consequent: {}".format(formula.get_consequent()))
print("consequent atoms: {}".format(formula.get_consequent_atoms()))
