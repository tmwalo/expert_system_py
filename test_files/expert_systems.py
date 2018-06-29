import sys #sys allows me to access argv 
import re #re allows me to access regular expressions
import pprint

def verboseprint(*args):
    if len(sys.argv) == 3 and sys.argv[2] == '-v':
        for arg in args:
           print(arg)

def verboseprint2(*args):
    if len(sys.argv) == 3 and sys.argv[2] == '-V':
        for arg in args:
           print(arg)           

def check_input_integrity(inputs=[]):
    test = re.compile(r'')
    if any(re.match(line) for line in inputs):
        verboseprint("Input file failed x integrity check!")
        quit()

#generalized function that removes comments(denoted by sep) from a string-line
def removeComments(line, sep):
    for s in sep:
        i = line.find(s)
        if i >= 0:
            line = line[:i]
    return line.strip()

#generalized function that takes an array of strings arr and looks for a string that starts with a character(char)
def getStartsWith(char, arr):
    s = [el for el in arr if el.startswith(char)]
    # verboseprint("getstarswith")
    # verboseprint(s)
    if s == '=':
        return s + ' '
    return s

#this checks wether or not s is a rule by checking that it doest start with an = or ?
def isRule(s):
    chars = ['=', '?']
    if (s[0] not in chars):
        return True
    else:
        return False

def lstToDct(lst, io):
    dct = {}
    for i in lst:
        dct[i] = io
    return(dct)

#Goes through the list of rules and creates a list of all rules that imply the passed fact
def check_relation(fact, rules):
    node_rules = []
    for rule in rules:
        implied_fact = '=>' + fact
        if implied_fact in rule:
            match = re.search('(.+?)' + implied_fact, rule)
            if match:
                found = match.group(1)
                node_rules.append(found)
            else:
                verboseprint("Error, failed to match regex")
    return node_rules

#Creates a tree of nodes for facts and relationships
def create_tree(variables, rules):
    tree_list = []
    for fact in variables:
        tree_list.append({"fact": fact, "value": False, 'solved': False, "rules": check_relation(fact, rules)})
    return tree_list

#Applies the given facts to tree_list
def apply_facts(tree_list, facts):
    for node in tree_list:
        # verboseprint('On node: ' + node['fact'])
        for fact in facts:
            # verboseprint('Checking fact: ' + fact)
            if node['fact'] == fact:
                # verboseprint('Changing ' + fact + ' to True')
                node['value'] = True
                node['solved'] = True
    return tree_list

def check_solved(tree_list):
    for node in tree_list:
        if node['solved'] == False:
            if len(node['rules']) == 0:
                node['solved'] = True
    return tree_list

def solver(first, first_not, second, second_not, sign):
    # verboseprint('test!!!!!!!!!!')
    # verboseprint('first_not: ' + str(first_not))
    # verboseprint('first: ' + str(first))
    # verboseprint('second_not: ' + str(second_not))
    # verboseprint('second: ' + str(second))
    # verboseprint('sign: ' + str(sign))
    first = first if first_not else not first
    second = second if second_not else not second
    # verboseprint('post!!!!!!!!!!')
    # verboseprint('first: ' + str(first))
    # verboseprint('second: ' + str(second))
    if sign == '+':
        return (first and second)
    elif sign == '|':
        return first or second
    elif sign == '^':
        return True if ((first and not second) or (not first and second)) else False

def get_value(fact, tree_list):
    for node in tree_list:
        if node['fact'] == fact:
            if node['solved'] == False:
                # verboseprint("GOING DEEPER on: " + fact)
                run_node(node, tree_list)
                # verboseprint('DEEPER COMPLETE FOR ' + node['fact'] + ': ' + str(node['value']))
            return node['value']

def eval_brackets(match, acc, tree_list):
    pre = match.group(1)
    not_before = match.group(2)
    inside = match.group(3)
    post = match.group(4)
    result = eval_sum(inside, acc, tree_list)
    not_before = False if not_before == '!' else True
    return [pre + post, (result if not_before else not result)]

def eval_sign(match, acc, tree_list, sign):
    pre = match.group(1)
    first_not = match.group(2)
    first = match.group(3)
    pre_sign = match.group(4)
    post_sign = match.group(5)
    second_not = match.group(6)
    second = match.group(7)
    post = match.group(8)
    # verboseprint('pre: ' + pre)
    # verboseprint('first_not: ' + first_not)
    # verboseprint('first: ' + first)
    # verboseprint('pre_sign: ' + pre_sign)
    # verboseprint('post_sign: ' + post_sign)
    # verboseprint('second_not: ' + second_not)
    # verboseprint('second: ' + second)
    # verboseprint('post: '+ post)
    if pre_sign and post_sign:
        print ('Error found 2 signs with an AND during ' + match)
        quit()
    elif pre_sign:
        eval_str = pre + first_not + first + pre_sign + post
        acc = solver(acc, True, get_value(second, tree_list), False if second_not == '!' else True, sign)
    elif post_sign:
        eval_str = pre + post_sign + second_not + second + post
        acc = solver(get_value(first, tree_list), False if first_not == '!' else True, acc, True, sign)
    elif not pre_sign and not post_sign:
        # verboseprint('no pre and post signs')
        eval_str = pre + post
        acc = solver(get_value(first, tree_list), False if first_not == '!' else True, get_value(second, tree_list), False if second_not == '!' else True, sign)
    # verboseprint('Eval sign ret: ')
    # verboseprint(eval_str)
    # verboseprint(acc)
    return (eval_str, acc)

def eval_sum(eval_str, acc, tree_list):
    original_eval_str = eval_str
    # verboseprint('evaluating new sum: ' + original_eval_str)
    while eval_str != '':
        # verboseprint('next iter eval_str: ' + eval_str + ' acc: ' + str(acc))
        accumilated = re.search(r'(^[\|\+\^])(.*)|(.*)([\|\+\^]\Z)', eval_str) #Check for signs that have accumilated on the edge
        brackets = re.search(r'(.*?)(!?)\((.+?)\)(.*)', eval_str) #Check for brackets
        plus = re.search(r'(.*?)(!?)([A-Z])([\|\^]?)\+([\|\^]?)(!?)([A-Z])(.*)', eval_str) #Check for +
        pipe = re.search(r'(.*?)(!?)([A-Z])([\+\^]?)\|([\+\^]?)(!?)([A-Z])(.*)', eval_str) #Check for |
        kapi = re.search(r'(.*?)(!?)([A-Z])([\+\|]?)\^([\+\|]?)(!?)([A-Z])(.*)', eval_str) #Check for ^
        fact = re.search(r'([A-Z])', eval_str) #Check for single fact
        sign = re.search(r'(^[\|\^\+]\Z)', eval_str) #Check for signs left alone in eval_str
        fact_sign = re.search(r'^([\|\^\+])(!?)([A-Z])\Z|^(!?)([A-Z])([\|\^\+])\Z', eval_str) #Check for signs left with facts in eval_str
        if fact_sign:
            # verboseprint('in fact_sign')
            eval_str = ''
            temp_acc = solver(get_value((fact_sign.group(3) or fact_sign.group(5)), tree_list), False if (fact_sign.group(2) or fact_sign.group(4)) == '!' else True, acc, True, fact_sign.group(1) or fact_sign.group(6))
        elif accumilated:
            eval_str = ''
            temp_acc = solver(eval_sum(accumilated.group(2) or accumilated.group(3), False, tree_list), True, acc, True, accumilated.group(1) or accumilated.group(4))
        elif brackets: eval_str, temp_acc = eval_brackets(brackets, acc, tree_list)
        elif plus: eval_str, temp_acc = eval_sign(plus, acc, tree_list, '+')
        elif pipe: eval_str, temp_acc = eval_sign(pipe, acc, tree_list, '|')
        elif kapi: eval_str, temp_acc = eval_sign(kapi, acc, tree_list, '^')
        elif fact:
            verboseprint2('in fact')
            eval_str = ''
            temp_acc = get_value(fact.group(1), tree_list)
        elif sign:
            verboseprint2('in sign')
            eval_str = ''
            temp_acc = solver(acc, True, last_acc, True, eval_str)
        else:
            print('Unable to solve: ' + original_eval_str + ' Stuck on: ' + eval_str)
        last_acc = acc
        acc = temp_acc
    # verboseprint('eval_sum ret:' + str(acc))
    return acc

def all_same(items):
   return all(x == items[0] for x in items)

def run_node(node, tree_list):
    if len(node['rules']) > 0 and not node['solved']:
        results = []
        for rule in node['rules']:
            verboseprint('rule: ' + rule)
            results.append(eval_sum(rule, node['value'], tree_list))
            if not all_same(results):
                print('Error, ambigious rules for ' + node['fact'])
            else:
                verboseprint2('New value: ' + str(results[0]))
                node['value'] = results[0]
        verboseprint2('Setting solved fact to True')
        node['solved'] = True
    return node

#Goes through the tree list and iterates over every rule, evaluating them to determine true value
def run_rules(tree_list):
    for node in tree_list:
        # verboseprint('INTERPRETING: ' + node['fact'])
        node = run_node(node, tree_list)
        # verboseprint('INTERPRETING COMPLETE FOR ' + node['fact'] + ': ' + str(node['value']))     
    return tree_list

def checkParen(lst):
    iLeft = 0
    iRight = 0
    for i in lst:
        if i == '(' : iLeft += 1
        elif i == ')' : iRight += 1
    if iLeft - iRight > 0 : return False
    if iRight - iLeft > 0 : return False    
    if iLeft - iRight == 0 : return True
    return False

def validateList(regex, lst):
    if isinstance(lst, list):
        for i in lst :
            if regex.findall(i) and checkParen(i): # be careful about efficiency facts and queries dont need to check parens since that is already removed
                verboseprint("   OK: "+ i)
            elif not checkParen(i) :
                print('ERROR "(" or ")" missing: ' + i)
                return False
            else:
                print('ERROR: ' + i)
                return False
    if isinstance(lst, str):
        if regex.findall(lst): # be careful about efficiency facts and queries dont need to check parens since that is already removed
            verboseprint("   OK: "+ lst)
        else:
            print('ERROR: ' + lst)
            return False
    return True 

def validateInputs(rules, facts, queries):
    rRules = re.compile("^(!?\()*!?[A-Z]\)*([|+^](!?\()*!?[A-Z]\)*)*=>!?[A-Z](\+!?[A-Z])*\Z")
    rFacts = re.compile("=(!?[A-Z])*")
    rQueries = re.compile("\?(!?[A-Z])+")
    f = ''.join(facts) 
    q = ''.join(queries) 
    verboseprint("CHECKING_INPUT_FILE:")
    if not validateList(rRules, rules):
        print("Please correct rules and try again")
        quit() 
    if not validateList(rFacts, f):
        print("Please correct facts and try again")
        quit()
    if not validateList(rQueries, q):
        print("Please correct queries and try again")
        quit()

def runExpertSystem(file_name):
    try:
        with open (file_name, 'rt') as in_file:#this code opens the file argv, reads it into the array file_data and closes the file afterwards
            file_data = in_file.readlines() #Read the entire file into an array of strigns called file_data.
    except:
        print('ERROR: file "' + file_name + '" does not exist.')
    inputs = [removeComments(i, '#') for i in file_data]#this code removes all commented/new lines from inputs
    inputs = filter(None, inputs) #I used filter as it is the most optimal way to remove empty strings from a  list of strings
    facts = getStartsWith('=', inputs)#this code places the facts into a list called facts and removes the '=' sign
    queries = getStartsWith('?', inputs) #this code places the queries into a list called queries and removes the '?' sign
    rules = filter(isRule, inputs) #this code places only non queries and non facts into rules by filtering them out of inputs
    rules = [''.join(i.split()) for i in rules]#this code gets a unique set of characters from the joined strings(rules[0] + rules[1] + rules[n]) 
    # veboseprint('testing rules1:')
    # pprint.pprint(rules)
    # veboseprint('testing facts1:')
    # pprint.pprint(facts)
    # veboseprint('testing queries1:')
    # pprint.pprint(queries)
    validateInputs(rules, facts, queries)
    facts = ''.join(facts)
    queries = ''.join(queries)
    facts = [c for c in facts]
    queries = [c for c in queries]
    facts.pop(0)
    queries.pop(0)
    facts = lstToDct(facts, True)
    variables = set(''.join(rules))
    variables = [char for char in variables if char.isalpha()]
    verboseprint("Searching for negated facts:")     
    last = ''       
    for idx,q in enumerate(queries):        
        # print(last)       
        if last == '!':     
            last = q        
            queries[idx] = '!' + q      
            # print('blah')       
            # print(queries[idx])     
            queries.pop(idx - 1)        
        else:       
            last = q        
    toRemove = []
    verboseprint("Spliting multi-implicattion rules:")
    for rule in rules:
        verboseprint('On rule: ' + rule)
        q = rule.split('=>')[1]
        r = rule.split('=>')[0]
        # print('Checking implies: ' + q)
        if len(q) > 2 :
            temps = q.split('+')
            # print('length > 2')
            # print(temps)
            for i in temps:
                rules.append(r +'=>'+ i)
                verboseprint('Added: '+r +'=>'+ i)
            toRemove.append(rule)
    for rule in toRemove:
        verboseprint('Removing: ' + rule)
        rules.remove(rule)
    # print('testing rules2:')
    # pprint.pprint(rules)
    # print('testing facts2:')
    # pprint.pprint(facts)
    # print('testing queries2:')
    # pprint.pprint(queries)
    # print('testing vars2:')
    # pprint.pprint(variables)
    try:
        tree_list = create_tree(variables, rules)
        tree_list = apply_facts(tree_list, facts)
        tree_list = check_solved(tree_list)
        tree_list = run_rules(tree_list)
        # veboseprint 'running rules'
        # tree_list = run_rules(tree_list)
        # veboseprint 'creating tree'
        # tree_list = create_tree(variables, rules)
        # veboseprint 'applying facts to tree nodes'
        # tree_list = apply_facts(tree_list, facts)
        # veboseprint 'Checking the tree for solved nodes'
        # tree_list = check_solved(tree_list)
        print('ANSWER:')
        for query in queries:
            for node in tree_list:
                if node['fact'] == query:
                    print(query + ': ' + str(get_value(node['fact'], tree_list)))
    except:
        print 'Failed running rules for file: ' + file_name
if len(sys.argv) > 1:
    runExpertSystem(sys.argv[1])