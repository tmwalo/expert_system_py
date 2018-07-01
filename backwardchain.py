
def backwardchain(rules, facts, goal, validate, resolver):
    if (validate.is_fact(goal)) and ((facts.atoms)[goal] == True):
        return
    goals = []
    goals.append(goal)
    conflict_set = []
    for rule in rules:
        if goal in rule.get_consequent_atoms():
            conflict_set.append(rule)
    for matched_rule in conflict_set:
        is_antecedent_true = resolver.resolve(matched_rule.get_antecedent(), facts)
        if (is_antecedent_true and validate.is_fact(matched_rule.get_consequent())):
            (facts.atoms)[matched_rule.get_consequent()] = True
        elif (is_antecedent_true and validate.is_conjuction_of_literals(matched_rule.get_consequent())):
            literals = validate.is_conjuction_of_literals(matched_rule.get_consequent())
            for literal in literals:
                if not validate.is_negated_fact(literal):
                    (facts.atoms)[literal] = True
        else:
            antecedent_atom_list = matched_rule.get_antecedent_atoms()
            for atom in antecedent_atom_list:
                if atom not in goals:
                    goals.append(atom)
	    for goal in goals:
	    	if len(goals) > 1:
	    		backwardchain(rules, facts, goals.pop(), validate, resolver)
    for matched_rule in conflict_set:
        is_antecedent_true = resolver.resolve(matched_rule.get_antecedent(), facts)
        if (is_antecedent_true and validate.is_fact(matched_rule.get_consequent())):
            (facts.atoms)[matched_rule.get_consequent()] = True
    return