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
