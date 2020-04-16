from os import system
import csv

with open("./Modified_Data_Files/students.csv","r") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for line in csv_reader:
        data=dict(line)

def register():
    system("clear")
    print("\nHello")

def validate(uname,passwd):
    system("clear")
    if uname in data.values and passwd in data.values:
        return True
    else:
        return False

def courseList():
    print("Hello")

def centerList():
    print("Hello")

def setPreference():
    print("Hello")

def checkAllocatedCenter():
    print("Hello")

def updatePaymentDetail():
    print("Hello")