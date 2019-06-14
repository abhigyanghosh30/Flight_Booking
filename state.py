import json
import csv

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
        for row in airport_data:
            if answer in row[1]:
                self.destination = row[2]
                print("Let me confirm that your answer was :")
                print(row)
                confirmation = input("Is that correct?")
                if "yes" in confirmation:
                    self.get_source()
                else:
                    self.get_destination()

    def get_source(self):
        print("from where do you want to go?")
        answer = input()
        options = []
        for row in airport_data:
            if answer in row[1]:
                options.append(row)
        if len(options) == 1:
            print("Let me confirm that your answer was :")
            print(row[0])
            confirmation = input("Is that correct?\n")
            if "yes" in confirmation:
                quit()
            else:
                self.get_source()
        


def quit():
    print("Have a nice day")

if __name__ == "__main__":
    frame = Frame()
    frame.get_destination()
    
