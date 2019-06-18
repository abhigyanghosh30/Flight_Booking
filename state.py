import json
import csv
import interpreter as ipt

airport_data = []

with open('airports.csv','rt')as f:
    airport_file = csv.reader(f)
    for row in airport_file:
        airport_data.append(row)

with open("flight_data.json","r") as f:
    flight_file = json.load(f)
    flight_data = flight_file["data"]


class Frame:
    def __init__(self):
        self.source = ""
        self.destination = ""
    
    def get_destination(self):
        print("where do you want to go?")
        answer = input()
        options = []
        for row in airport_data:
            if answer in row[1]:
                options.append(row)
        
        if len(options) == 0:
            print("We don't seem to have a match in our database. Let's try again")
            self.get_destination()

        elif len(options) == 1:
            print("Let me confirm that your answer was :")
            print(options[0])
            confirmation = input("Is that correct?\n")
            if "yes" in confirmation:
                self.destination = options[0][2]
                self.get_source()
            else:
                self.get_destination()
        
        else:
            print("There seem to be more than one matches, please select the appropriate a answer")
            for option in options:
                print(option)
            option_number = -1
            while option_number > len(options) or option_number <= 0:
                option_number = input("Select from given options\n")
                option_number = int(option_number)
            print("Selected option is "+options[option_number-1][0])
            self.source = options[option_number-1][2]
            self.get_source()

    def get_source(self):
        print("from where do you want to go?")
        answer = input()
        options = []
        for row in airport_data:
            if answer in row[1]:
                options.append(row)
        
        if len(options) == 0:
            print("We don't seem to have a match in our database. Let's try again")
            self.get_destination()

        elif len(options) == 1:
            print("Let me confirm that your answer was :")
            print(options[0])
            confirmation = input("Is that correct?\n")
            if "yes" in confirmation:
                self.destination = options[0][2]
                self.get_date()
            else:
                self.get_destination()
        
        else:
            print("There seem to be more than one matches")
            for option in options:
                print(option)
            option_number = int(-1)
            while option_number > len(options) or option_number <= 0:
                option_number = input("Select from given options\n")
                option_number = int(option_number)
                print(option_number)
            print("Selected option is "+options[option_number-1][0])
            self.source = options[option_number-1][2]
            self.get_date()

    def get_date(self):
        date = ipt.inp_day()
        quit()

def quit():
    print("Have a nice day")

if __name__ == "__main__":
    frame = Frame()
    frame.get_destination()
    
