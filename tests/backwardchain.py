
def backwardchain(rules, facts, goal, validate, resolver):
    if (validate.is_fact(goal)) and ((facts.atoms)[goal] == True):
        print(goal + " is true")
        return
    goals = []
    goals.append(goal)
    conflict_set = []
    print("current goal: " + goal)
    for rule in rules:
        print("current rule: " + rule.rule)
        if goal in rule.get_consequent_atoms():
            conflict_set.append(rule)
            print("Add rule to conflict set")
    for matched_rule in conflict_set:
        print("matched rule: " + matched_rule.rule)
        is_antecedent_true = resolver.resolve(matched_rule.get_antecedent(), facts)
        if (is_antecedent_true):
            print("lhs of matched rule is true")
        if (is_antecedent_true and validate.is_fact(matched_rule.get_consequent())):
            (facts.atoms)[matched_rule.get_consequent()] = True
            print("rhs set to true")
        elif (is_antecedent_true and validate.is_conjuction_of_literals(matched_rule.get_consequent())):
            print("rhs is conjuction of literals")
            literals = validate.is_conjuction_of_literals(matched_rule.get_consequent())
            for literal in literals:
                if not validate.is_negated_fact(literal):
                    (facts.atoms)[literal] = True
                    print(literal + " is set to true")
        else:
            print("add lhs atoms to goals")
            antecedent_atom_list = matched_rule.get_antecedent_atoms()
            for atom in antecedent_atom_list:
                if atom not in goals:
                    goals.append(atom)
                else:
                    print("Atom already in goal stack")
            print("recur")
            print("")
	    for goal in goals:
	    	if len(goals) > 1:
	    		backwardchain(rules, facts, goals.pop(), validate, resolver)
    print("final resolve")
    print("")
    for matched_rule in conflict_set:
        is_antecedent_true = resolver.resolve(matched_rule.get_antecedent(), facts)
        if (is_antecedent_true and validate.is_fact(matched_rule.get_consequent())):
            (facts.atoms)[matched_rule.get_consequent()] = True
    return
