import os
from expert_systems import runExpertSystem

root = os.getcwd() + '/input'
path = os.path.join(root, "")

for path, subdirs, files in os.walk(root):
    for name in files:
    	test_file = os.path.join(path, name)
        print "Testing file: " + test_file
        runExpertSystem(test_file)