from operations import Operations

ops = Operations()
count = 1
a = True
b = True
c = False
d = False

if ops.negate_op(c):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not ops.negate_op(a):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if ops.and_op(a, b):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not ops.and_op(a, c):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if ops.or_op(d, b):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not ops.or_op(c, d):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if ops.xor_op(c, a):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

if not ops.xor_op(a, b):
	print("{}. PASS".format(count))
else:
	print("{}. FAIL".format(count))
count += 1

print("")

print("! precedence = {}".format(ops.precedence("!")))
print("+ precedence = {}".format(ops.precedence("+")))
print("| precedence = {}".format(ops.precedence("|")))
print("^ precedence = {}".format(ops.precedence("^")))
print("=> precedence = {}".format(ops.precedence("=>")))
print("<=> precedence = {}".format(ops.precedence("<=>")))
