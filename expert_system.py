# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/29 10:55:49 by tmwalo            #+#    #+#              #
#    Updated: 2018/06/30 11:52:03 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from rule import Rule
from facts import Facts
from validator import Validator
from resolve_proposition import ResolveProposition
import sys
import re

if len(sys.argv) != 2:
    print("Error!")
    print("Usage: expert_system input_file")
    sys.exit(0)

validate = Validator()
rule_found = False
fact_init_found = False
query_init_found = False
check_rule = True
check_fact_init = False
check_query_init = False

rules = []

facts = Facts()
initialised_facts = []

queries = []

try:
    input_file = open(sys.argv[1], "r")
except IOError:
    print("Failed to read file.")
    sys.exit(0)

for line in input_file:
    if (line != "\n") and (line != ""):
        line = validate.remove_comment(line)
        line = re.split("\s+", line)
        line = list(filter(None, line))
        line = " ".join(line)
	if not line:
	    continue
        if (not check_rule) and (not check_fact_init) and (not check_query_init):
            sys.stderr.write("Error - unrecognised line found\n")
            sys.exit(0)
        if check_rule:
	    if validate.is_rule(line):
		rule_found = True
		rule = Rule(line)
		rules.append(rule)
	    elif rule_found:
		check_rule = False
                check_fact_init = True
	    else:
		sys.stderr.write("Error - rule not found\n")
                sys.exit(0)
	if check_fact_init:
	    if validate.is_fact_init(line):
                fact_init_found = True
                for char in line:
                    if char == "=":
                        continue
                    (facts.atoms)[char] = True
                    initialised_facts.append(char)
                check_fact_init = False
                check_query_init = True
                continue
            else:
		sys.stderr.write("Error - fact initialisation not found\n")
                sys.exit(0)
	if check_query_init:
	    if validate.is_query_init(line):
		query_init_found = True
                for char in line:
                    if char == "?":
                        continue
                    queries.append(char)
                check_query_init = False
            else:
		sys.stderr.write("Error - query initialisation not found\n")
                sys.exit(0)
input_file.close()

print("Rules:")
for rule in rules:
    print(rule.rule)
print("")

print("Initialised facts:")
for fact in initialised_facts:
    print(fact)
print("")

print("Queries:")
for query in queries:
    print(query)
print("")

def backchain(rules, facts, goal):
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
	    		backchain(rules, facts, goals.pop())
    for matched_rule in conflict_set:
        is_antecedent_true = resolver.resolve(matched_rule.get_antecedent(), facts)
        if (is_antecedent_true and validate.is_fact(matched_rule.get_consequent())):
            (facts.atoms)[matched_rule.get_consequent()] = True
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

resolver = ResolveProposition()

for query in queries:
    backchain(rules, facts, query)
    resolveQuery(query, facts, rules)
    print(query + ":")
    print((facts.atoms)[query])
    print("")
