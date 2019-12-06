from compiler import Compiler
from lmc import LMC

compiler = Compiler()
lmc = LMC()

for x in ("basicCOMP1071.txt","advancedCOMP1071.txt"):
    compiler.load_and_abstract_code_from_file(x)
    mailboxes = compiler.compile()
    lmc.mailboxes = mailboxes
    for x in range(1,999):
        lmc.input_stack = [x]
        output = lmc.run()

        print(output[0])
        print(output[1])