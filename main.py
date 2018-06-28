# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 10:40:14 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/27 12:44:04 by tmwalo           ###   ########.fr        #
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

goals = []
goals.append("E")

validate = Validator()

resolver = ResolveProposition()

def backchain(rules, facts, goals):
    print("begin backchain")
    goal = goals.pop()
    if (validate.is_fact(goal)) and ((facts.atoms)[goal] == True):
        goals.remove(goal)
        return (True)
        
    conflict_set = []
    for rule in rules:
        if rule.get_consequent() == goal:
            conflict_set.append(rule)
    if not conflict_set:
        return (False)
    for matched_rule in conflict_set:
        antecedent = matched_rule.get_antecedent()
        if (validate.is_fact(antecedent)) and ((facts.atoms)[antecedent] == True):
            goals.remove(matched_rule.get_consequent())
            return (True)
        elif resolver.resolve(antecedent, facts):
            goals.remove(matched_rule.get_consequent())
            return (True)
        else:
            print("begin recursion")
            antecedent_atom_list = matched_rule.get_antecedent_atoms()
            for atom in antecedent_atom_list:
                if atom not in goals:
                    goals.append(atom)
            backchain(rules, facts, goals)
    return (False)

if (backchain(rules, facts, goals)):
    print("Query is true")
