class NumberProcessor:
    def __init__(self):
        self.stack = []

    def S(self, x):
        
        self.stack.append(x)

    def A(self):
       
        if self.stack:
            print(max(self.stack))
        else:
            print("Error")

    def R(self):
       
        if self.stack:
            max_num = max(self.stack)
            self.stack.remove(max_num)
        else:
            print("Error")

    def I(self, x):
        
        if self.stack:
            max_num = max(self.stack)
            index = self.stack.index(max_num)
            self.stack[index] += x
        else:
            print("Error")

    def D(self, x):
        
        if self.stack:
            max_num = max(self.stack)
            index = self.stack.index(max_num)
            self.stack[index] -= x
        else:
            print("Error")

    def process_commands(self):
        while True:
            command = input()
            parts = command.split()
            
            if parts[0] == "S":
                self.S(int(parts[1]))
            elif parts[0] == "A":
                self.A()
            elif parts[0] == "R":
                self.R()
            elif parts[0] == "I":
                self.I(int(parts[1]))
            elif parts[0] == "D":
                self.D(int(parts[1]))
            elif parts[0] == "T":
                break


processor = NumberProcessor()
processor.process_commands()

