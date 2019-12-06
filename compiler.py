#file_name = input("enter file name of LMC assembly: ")
file_name = "advancedCOMP1071.txt"

import re

class Compiler:

    regex = r"([a-zA-Z]*)[\t]+([A-Z]{2,3})[\t\s]*([0-9a-zA-Z]*)\n"
    code = []
    
    def load_and_abstract_code_from_file(self,file_name):
        self.code=[]
        with open(file_name, "r") as f:
            lines = f.read()
            matches = re.finditer(self.regex, lines, re.MULTILINE)
            for match in matches:
                self.code.append(match.groups())

    def compile(self):
        mailboxes = []
        label_map = {}
        instruction_map = {
                "HLT": 0,
                "DAT": 0,
                "ADD": 1,
                "SUB": 2,
                "STO": 3,
                "LDA": 5,
                "BR": 6,
                "BRZ": 7,
                "BRP": 8,
                "IN": 9,
                "OUT": 9
        }
        for (i,(label,_,_)) in enumerate(self.code):
            if label != '':
                label_map[label] = i
        for (label,instruction,location) in self.code:
            if instruction == "HLT":
                mailboxes.append(0)
                continue
            first_number = instruction_map[instruction]
            temp_mailbox = first_number*100
            small_number = 1
            if first_number == 9:
                if instruction == "OUT":
                    small_number = 2
            elif 1 <= first_number <= 8:
                small_number = label_map[location]
            else:
                small_number = int(location)
            mailboxes.append(temp_mailbox+small_number)

        return mailboxes

