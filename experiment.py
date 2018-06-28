# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 10:40:14 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/28 10:42:12 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from rule import Rule
from facts import Facts
from validator import Validator
from resolve_proposition import ResolveProposition

rule1 = Rule("A => C")
rule2 = Rule("B => D")
rule3 = Rule("C + D => E")

rules = []
rules.append(rule1)
rules.append(rule2)
rules.append(rule3)

facts = Facts()
(facts.atoms)["A"] = True
(facts.atoms)["B"] = True

goals = []
goals.append("E")

validate = Validator()

resolver = ResolveProposition()

def backchain(rules, facts, goals):
    goal = goals.pop()
    print("popped goal: " + goal)
    if (validate.is_fact(goal)) and ((facts.atoms)[goal] == True):
        print(goal + " is fact and is true")
        return
        
    conflict_set = []
    for rule in rules:
        print("current rule: " + rule.rule)
        print("consequent of current rule: " + rule.get_consequent())
        if rule.get_consequent() == goal:
            print("add to conflict set: " + rule.rule)
            conflict_set.append(rule)
    for matched_rule in conflict_set:
        is_antecedent_true = resolver.resolve(matched_rule.get_antecedent(), facts)
        if (is_antecedent_true and validate.is_fact(matched_rule.get_consequent())):
            (facts.atoms)[matched_rule.get_consequent()] = True
            return
        else:
            antecedent_atom_list = matched_rule.get_antecedent_atoms()
            for atom in antecedent_atom_list:
                if atom not in goals:
                    print("add to goals: " + atom)
                    goals.append(atom)
            backchain(rules, facts, goals)
    print("Exit backchain")
    return

backchain(rules, facts, goals)

print("A:")
print((facts.atoms)["A"])
print("B:")
print((facts.atoms)["B"])
print("C:")
print((facts.atoms)["C"])
print("D:")
print((facts.atoms)["D"])
print("E:")
print((facts.atoms)["E"])
