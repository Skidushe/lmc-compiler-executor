from compiler import Compiler
from lmc import LMC
import glob, os

compiler = Compiler()
lmc = LMC()

def basic_test_script(x):
    output = []
    while 0 < x:
        if x == 1:
            output.append(1)
            break
        if x > 999:
            output.append(0)
            break
        output.append(x)
        if x%2 == 0:
            x=x/2
        else:
            x=3*x+1
        x=int(x)
    return output

def advanced_test_script(x):
    output = []
    while 0 < x:
        if x == 1:
            output.append(1)
            break
        if x > 999:
            output.append(0)
            break
        output.append(x)
        if x%2 == 0:
            x=x/2
        else:
            x=(3*x+1)/2
        x=int(x)
    return output

def run_against_test_function(func, feedback_path):
    mailboxes = compiler.compile()
    lmc.mailboxes = mailboxes
    with open(feedback_path,"w+") as f:
        for i in range(1,1000):
            lmc.input_stack = [i]
            #lmc.mailboxes = mailboxes # If needs resetting after every run
            output = lmc.run()
            correct_output = func(i)

            f.write("\n--------------")
            f.write("\nyour output:    " + str(output[0]))
            f.write("\ndesired output: " + str(correct_output))
            f.write("\nmatch?:         " + str(output[0]==correct_output))
            f.write("\nprogram cycles: " + str(output[1]))
        # Add Marking logic here

for filename in glob.iglob('./students/**', recursive=False):
    if os.path.isdir(filename): # filter dirs
        with open(filename+"/basicCOMP1071.txt", "r") as f:
            lines = f.read()
            compiler.abstract_code_from_string(lines)
        run_against_test_function(basic_test_script, filename+"/feedbackBasic.txt")
        with open(filename+"/advancedCOMP1071.txt", "r") as f:
            lines = f.read()
            compiler.abstract_code_from_string(lines)
        run_against_test_function(advanced_test_script, filename+"/feedbackAdvanced.txt")

