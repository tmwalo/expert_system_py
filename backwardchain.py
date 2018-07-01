# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    backwardchain.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/07/01 11:51:18 by tmwalo            #+#    #+#              #
#    Updated: 2018/07/01 12:45:09 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
            if ((facts.atoms)[matched_rule.get_consequent()] == False) and ((facts.is_set)[matched_rule.get_consequent()] == True):
	    	raise Exception("Contradiction found")
            (facts.atoms)[matched_rule.get_consequent()] = True
            (facts.is_set)[matched_rule.get_consequent()] = True
        elif (is_antecedent_true and validate.is_negated_fact(matched_rule.get_consequent())):
            if (facts.atoms)[(matched_rule.get_consequent())[1]] == True:
	    	raise Exception("Contradiction found")
            (facts.atoms)[(matched_rule.get_consequent())[1]] = False
            (facts.is_set)[(matched_rule.get_consequent())[1]] = True
        elif (is_antecedent_true and validate.is_conjuction_of_literals(matched_rule.get_consequent())):
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
