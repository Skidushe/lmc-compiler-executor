#mailboxes = [901,347,902,242,741,541,349,547,348,549,145,349,244,731,808,144,348,549,245,349,548,348,549,142,349,548,243,731,822,633,548,549,601,547,246,839,547,149,601,541,902,0,1,2,32,16,666,1,1,0]
class LMC():
    mailboxes = []
    counter = 0
    current_instruction = 0
    calculator = 0
    continue_program = True
    input_stack = []
    output_stack = []

    def fetch(self):
        self.current_instruction = self.mailboxes[self.counter]
        self.counter += 1

    def halt(self,mailbox_location):
        self.continue_program = False

    def add(self,mailbox_location):
        mailbox = self.mailboxes[mailbox_location]
        self.calculator += mailbox

    def subtract(self,mailbox_location):
        mailbox = self.mailboxes[mailbox_location]
        self.calculator -= mailbox

    def store(self,mailbox_location):
        self.mailboxes[mailbox_location] = abs(self.calculator)

    def load(self,mailbox_location):
        self.calculator = self.mailboxes[mailbox_location]

    def branch(self,branch_point):
        self.counter = branch_point

    def branch_on_zero(self,branch_point):
        if self.calculator == 0:
            self.counter = branch_point

    def branch_on_positive(self,branch_point):
        if self.calculator > 0:
            self.counter = branch_point

    def input_output(self,type):
        if type == 1:
            if not self.input_stack:
                self.calculator = int(input("Enter input: "))
            else:
                self.calculator = self.input_stack[0]
                self.input_stack.pop(0)
        else: 
            self.output_stack.append(self.calculator)

    def execute(self):
        first_digit = self.current_instruction//100
        remaining = self.current_instruction - first_digit*100
        switcher = {
            0: self.halt,
            1: self.add,
            2: self.subtract,
            3: self.store,
            5: self.load,
            6: self.branch,
            7: self.branch_on_zero,
            8: self.branch_on_positive,
            9: self.input_output
        }
        func = switcher.get(first_digit, lambda: "Invalid instruction")
        func(remaining)

    def run(self):
        self.counter = 0
        self.current_instruction = 0
        self.calculator = 0
        self.continue_program = True
        self.output_stack = []
        total_cycles = 0
        while self.continue_program:
            self.fetch()
            self.execute()
            total_cycles+=1
        return (self.output_stack, total_cycles)

