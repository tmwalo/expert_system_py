from validator import Validator

validate = Validator()
count = 1

if validate.is_fact("V"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_fact("Vendetta"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_fact("v"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_negation("!"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_negation("!!"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_and("+"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_and("villany"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_or("|"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_or("vicarious"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_xor("^"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_xor("violet"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_imply("=>"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_imply("=>=>=>=>=> || <=<=<=<=<="):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_iff("<=>"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_iff("<===== || =====>"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_left_bracket("("):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_left_bracket("vibrant"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_right_bracket(")"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_right_bracket("virus"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_operator("+"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_operator("*"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_operator("--*-*--"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if validate.is_left_associative("|"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not validate.is_left_associative("!"):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

print("")

line = ""
print("empty line")
print("line: " + line)
print("remove comment: " + validate.remove_comment(line))

line1 = "no comment"
print("line: " + line1)
print("remove comment: " + validate.remove_comment(line1))

line2 = "#"
print("line: " + line2)
print("remove comment: " + validate.remove_comment(line2))

line3 = "# comment only"
print("line: " + line3)
print("remove comment: " + validate.remove_comment(line3))

line4 = "A + B => C # this part is a comment"
print("line: " + line4)
print("remove comment: " + validate.remove_comment(line4))
print("")

line = ""
print("empty line")
print("is line fact init: " + line)
print(validate.is_fact_init(line))

line = "not fact init"
print("is line fact init: " + line)
print(validate.is_fact_init(line))

line = "=ABnot fact"
print("is line fact init: " + line)
print(validate.is_fact_init(line))

line = "= ABC"
print("is line fact init: " + line)
print(validate.is_fact_init(line))

line = "="
print("is line fact init: " + line)
print(validate.is_fact_init(line))

line = "=ABC"
print("is line fact init: " + line)
print(validate.is_fact_init(line))
print("")

line = ""
print("empty line")
print("is line query init: " + line)
print(validate.is_query_init(line))

line = "not query init"
print("is line query init: " + line)
print(validate.is_query_init(line))

line = "?ABnot query"
print("is line query init: " + line)
print(validate.is_query_init(line))

line = "? ABC"
print("is line query init: " + line)
print(validate.is_query_init(line))

line = "?"
print("is line query init: " + line)
print(validate.is_query_init(line))

line = "?ABC"
print("is line query init: " + line)
print(validate.is_query_init(line))
print("")

rule = ""
print("empty line")
print("is rule: " + rule)
print(validate.is_rule(rule))

rule1 = "not a rule"
print("is rule: " + rule1)
print(validate.is_rule(rule1))

rule2 = "=>"
print("is rule: " + rule2)
print(validate.is_rule(rule2))

rule3 = "lhs not rule => rhs not rule"
print("is rule: " + rule3)
print(validate.is_rule(rule3))

rule4 = "A + B => (!C"
print("is rule: " + rule4)
print(validate.is_rule(rule4))

rule5 = "A + B => (!C) | D"
print("is rule: " + rule5)
print(validate.is_rule(rule5))
print("")

literal1 = ""
print("is literal: " + literal1)
print(validate.is_literal(literal1))

literal2 = "a"
print("is literal: " + literal2)
print(validate.is_literal(literal2))

literal3 = "!a"
print("is literal: " + literal3)
print(validate.is_literal(literal3))

literal4 = "say what again"
print("is literal: " + literal4)
print(validate.is_literal(literal4))

literal5 = "A"
print("is literal: " + literal5)
print(validate.is_literal(literal5))

literal6 = "!A"
print("is literal: " + literal6)
print(validate.is_literal(literal6))

literal7 = "! A"
print("is literal: " + literal7)
print(validate.is_literal(literal7))
print("")

and_conj1 = ""
print("is conjuction of literals: " + and_conj1)
print(validate.is_conjuction_of_literals(and_conj1))

and_conj2 = "   A + B - +    C "
print("is conjuction of literals: " + and_conj2)
print(validate.is_conjuction_of_literals(and_conj2))

and_conj3 = " one plus one is what ?    "
print("is conjuction of literals: " + and_conj3)
print(validate.is_conjuction_of_literals(and_conj3))

and_conj4 = " A + B + C "
print("is conjuction of literals: " + and_conj4)
print(validate.is_conjuction_of_literals(and_conj4))

and_conj5 = " A + !B + C "
print("is conjuction of literals: " + and_conj5)
print(validate.is_conjuction_of_literals(and_conj5))

and_conj6 = "A"
print("is conjuction of literals: " + and_conj6)
print(validate.is_conjuction_of_literals(and_conj6))
