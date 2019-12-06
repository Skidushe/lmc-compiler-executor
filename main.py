import time
#mailboxes = [901,347,902,242,741,541,349,547,348,549,145,349,244,731,808,144,348,549,245,349,548,348,549,142,349,548,243,731,822,633,548,549,601,547,246,839,547,149,601,541,902,0,1,2,32,16,666,1,1,0]
mailboxes = [901,347,902,242,741,541,349,547,348,549,145, 349, 548, 244, 731, 808, 144, 348, 549, 245, 349, 548, 348, 549, 142, 349, 548, 243, 731, 822, 633, 549, 601, 547, 246, 839, 547, 149, 601, 541, 902, 0, 1, 2, 32,16, 666, 1, 1, 0]
counter = 0
instruction = 0
calculator = 0
continue_program = True
negative_flag = False

def fetch():
    global counter
    global instruction
    global mailboxes
    instruction = mailboxes[counter]
    counter += 1

def halt(mailbox_location):
    global continue_program
    continue_program = False

def add(mailbox_location):
    global calculator
    global mailboxes
    mailbox = mailboxes[mailbox_location]
    calculator += mailbox

def subtract(mailbox_location):
    global calculator
    global mailboxes
    global negative_flag
    mailbox = mailboxes[mailbox_location]
    calculator -= mailbox
    if calculator < 0:
        negative_flag = True

def store(mailbox_location):
    global calculator
    global mailboxes
    mailboxes[mailbox_location] = abs(calculator)

def load(mailbox_location):
    global calculator
    global mailboxes
    global negative_flag
    negative_flag = False
    calculator = mailboxes[mailbox_location]

def branch(branch_point):
    global counter
    counter = branch_point

def branch_on_zero(branch_point):
    global calculator
    global counter
    if calculator == 0:
        counter = branch_point

def branch_on_positive(branch_point):
    global calculator
    global counter
    if not negative_flag:
        counter = branch_point

def input_output(type):
    global calculator
    if type == 1:
        calculator = int(input("Enter input: "))
    else: 
        print(calculator)

def execute():
    first_digit = instruction//100
    remaining = instruction - first_digit*100
    switcher = {
        0: halt,
        1: add,
        2: subtract,
        3: store,
        5: load,
        6: branch,
        7: branch_on_zero,
        8: branch_on_positive,
        9: input_output
    }
    func = switcher.get(first_digit, lambda: "Invalid instruction")
    func(remaining)

while continue_program:
    fetch()
    execute()

