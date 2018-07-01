
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
        # It is a contradiction for a matched rule to change the value of a fact that has been set by another matched rule
        # If a fact is False because it was initialised as False, it is Okay to change its value to True,
        # if however, a fact is False because a certain rule set it as False it is NOT Okay to change its value to True,
        # this would be a contradiction.
        # It would obviously be a contradiction to change a fact from True to False(since another matched rule must have set it
        # from its initial value of False to True)
        if (is_antecedent_true and validate.is_fact(matched_rule.get_consequent())):
            if ((facts.atoms)[matched_rule.get_consequent()] == False) and ((facts.is_set)[matched_rule.get_consequent()] == True):
	    	raise Exception("Contradiction found")
            (facts.atoms)[matched_rule.get_consequent()] = True
            (facts.is_set)[matched_rule.get_consequent()] = True
            print("rhs set to true")
        elif (is_antecedent_true and validate.is_negated_fact(matched_rule.get_consequent())):
            if (facts.atoms)[(matched_rule.get_consequent())[1]] == True:
	    	raise Exception("Contradiction found")
            (facts.atoms)[(matched_rule.get_consequent())[1]] = False
            (facts.is_set)[(matched_rule.get_consequent())[1]] = True
            print("rhs set to true => fact set to false since negation makes rhs true")
        elif (is_antecedent_true and validate.is_conjuction_of_literals(matched_rule.get_consequent())):
            print("rhs is conjuction of literals")
            literals = validate.is_conjuction_of_literals(matched_rule.get_consequent())
            for literal in literals:
                if validate.is_fact(literal):
                    if ((facts.atoms)[literal] == False) and ((facts.is_set)[literal] == True):
                        raise Exception("Contradiction found")
                    (facts.atoms)[literal] = True
                    (facts.is_set)[literal] = True
                elif validate.is_negated_fact(literal):
                    if (facts.atoms)[(literal)[1]] == True:
                        raise Exception("Contradiction found")
                    (facts.atoms)[(literal)[1]] = False
                    (facts.is_set)[(literal)[1]] = True
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
