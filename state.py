class state:
    def __init__(self):
        self.question = ""
        self.positive = quit
        self.negative = quit
    
    def set(self,question,positive,negative):
        self.question = question
        self.positive = positive
        self.negative = negative
    
    def ask(self):
        print(self.question)
        answer = input()
        print("Let me confirm that your answer was "+answer)
        confirmation = input("Is that correct?: ")
        if "yes" in confirmation:
            self.positive()
        else:
            self.negative()


def quit():
    print("Have a nice day")

if __name__ == "__main__":
    
    state1 = state()
    state2 = state()
    state1.set("Where do you want to go?",state2.ask,state1.ask)
    state2.set("From where do you want to go?",quit,state2.ask)
    state1.ask()
    
