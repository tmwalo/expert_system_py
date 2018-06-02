from resolve_proposition import ResolveProposition

resolver = ResolveProposition()
count = 1

empty_op_stack = []
empty_fact_stack = []
invalid_op_stack = ["*"]
invalid_fact_stack = ["string string", "thing1", "chocolate thunder"]
op_stack = ["+", "^", "|", "+", "!"]
fact_stack = [False, True, True, False, True, False, True]

#1
try:
	if not resolver.execute_stack_operation(empty_op_stack, fact_stack):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print(error)
count += 1

#2
try:
	if not resolver.execute_stack_operation(op_stack, empty_fact_stack):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print(error)
count += 1

#3
try:
	if not resolver.execute_stack_operation(invalid_op_stack, fact_stack):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print(error)
count += 1

#4
try:
	if not resolver.execute_stack_operation(op_stack, invalid_fact_stack):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print(error)
count += 1

#5
try:
	if resolver.execute_stack_operation(op_stack, fact_stack):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print(error)
count += 1

#6
try:
	if resolver.execute_stack_operation(op_stack, fact_stack):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print(error)
count += 1

#7
try:
	if resolver.execute_stack_operation(op_stack, fact_stack):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print(error)
count += 1

#8
try:
	if resolver.execute_stack_operation(op_stack, fact_stack):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print(error)
count += 1

class TestFacts:

	def __init__(self):
		self.atoms = {
						"A": True,
						"B": True,
						"C": False,
						"D": False
					}

facts = TestFacts()
fact_only = "A"
operator_only = "+"
valid_simple = "A|B"
valid_complex = "!C+B|D"
invalid_simple = "a*b"
invalid_complex = "A^B"
brackets_fact_only = "(B)"
more_brackets_fact_only = "(((B)))"
brackets_simple = "(C|A)"
brackets_complex = "((D+A)^(!C))"
missing_left_bracket = "!D|A+B)"
missing_right_bracket = "!D|(A+B"
brackets_wrong_order = ")C|A("
no_operator = "CA"

#9
try:
	if resolver.resolve(fact_only, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#10
try:
	if not resolver.resolve(operator_only, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#11
try:
	if resolver.resolve(valid_simple, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#12
try:
	if resolver.resolve(valid_complex, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#13
try:
	if not resolver.resolve(invalid_simple, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#14
try:
	if not resolver.resolve(invalid_complex, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#15
try:
	if resolver.resolve(brackets_fact_only, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#16
try:
	if resolver.resolve(more_brackets_fact_only, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#17
try:
	if resolver.resolve(brackets_simple, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#18
try:
	if resolver.resolve(brackets_complex, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#19
try:
	if not resolver.resolve(missing_left_bracket, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#20
try:
	if not resolver.resolve(missing_right_bracket, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#21
try:
	if not resolver.resolve(brackets_wrong_order, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1

#22
try:
	if not resolver.resolve(no_operator, facts):
		print("{}. PASS".format(count))
	else:
		print("{}. FAILED".format(count))
except Exception as error:
	print("{}. {}".format(count, error))
count += 1
