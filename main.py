# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/27 10:40:14 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/28 16:52:51 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from rule import Rule
from facts import Facts
from validator import Validator
from resolve_proposition import ResolveProposition
import sys

if len(sys.argv) != 2:
    print("Error!")
    print("Usage: expert_system input_file")
    sys.exit(0)

try:
    input_file = open(sys.argv[1], "r")
except IOError:
    print("File does not exist.")
    sys.exit(0)

validate = Validator()

for line in input_file:
    line = validate.remove_comment(line)
    if line != "":
        line = re.split("\s+", line)
        line = list(filter(None, line))
#   CONTINUE FROM HERE  #

input_file.close()

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

resolver = ResolveProposition()

def backchain(rules, facts, goals):
    if (not goals):
        return
    goal = goals.pop()
    if (validate.is_fact(goal)) and ((facts.atoms)[goal] == True):
        return

    conflict_set = []
    for rule in rules:
        if rule.get_consequent() == goal:
            conflict_set.append(rule)
    for matched_rule in conflict_set:
        is_antecedent_true = resolver.resolve(matched_rule.get_antecedent(), facts)
        if (is_antecedent_true and validate.is_fact(matched_rule.get_consequent())):
            (facts.atoms)[matched_rule.get_consequent()] = True
        else:
            antecedent_atom_list = matched_rule.get_antecedent_atoms()
            for atom in antecedent_atom_list:
                if atom not in goals:
                    goals.append(atom)
    backchain(rules, facts, goals)
    return

def resolveQuery(query, facts, rules):
    conflict_set = []
    for rule in rules:
        if rule.get_consequent() == query:
            conflict_set.append(rule)
    for matched_rule in conflict_set:
        is_antecedent_true = resolver.resolve(matched_rule.get_antecedent(), facts)
        if (is_antecedent_true):
            (facts.atoms)[query] = True
            return

backchain(rules, facts, goals)

resolveQuery("E", facts, rules)

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
