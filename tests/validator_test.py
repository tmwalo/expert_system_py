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
