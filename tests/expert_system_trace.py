# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    expert_system_trace.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tmwalo <marvin@42.fr>                      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/29 14:49:54 by tmwalo            #+#    #+#              #
#    Updated: 2018/07/01 12:36:19 by tmwalo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from rule import Rule
from facts import Facts
from validator import Validator
from resolve_proposition import ResolveProposition
from backwardchain import backwardchain
import sys
import re

if len(sys.argv) != 2:
    print("Error!")
    print("Usage: expert_system input_file")
    sys.exit(0)

validate = Validator()
resolver = ResolveProposition()
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
                    (facts.is_set)[char] = True
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

if not rule_found:
    sys.stderr.write("Error - rule not found\n")
    sys.exit(0)
if not fact_init_found:
    sys.stderr.write("Error - fact init not found\n")
    sys.exit(0)
if not query_init_found:
    sys.stderr.write("Error - query not found\n")
    sys.exit(0)

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

for query in queries:
    print("")
    try:
        backwardchain(rules, facts, query, validate, resolver)
    except:
        sys.stderr.write("Error - Contradiction found\n")
        sys.exit(0)
    print(query + ":")
    print((facts.atoms)[query])
    print("")
