import time
import os
from termcolor import colored
import argparse

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_path}.")

def firstSkull():
    firstSkullMainPath = 'gifs/1/frames/ASCII/'
    for x in range(17):
        time.sleep(0.06)
        os.system("clear")
        currentFilePath = firstSkullMainPath + str(x) + ".txt"
        read_file(currentFilePath)

def secondSkull():
    secondSkullMainPath = 'gifs/2/frames/ASCII/'
    for x in range(10):
        time.sleep(0.1)
        os.system("clear")
        currentFilePath = secondSkullMainPath + str(x) + ".txt"
        read_file(currentFilePath)

def outro():
    outroMainPath = 'gifs/outro/frames/ASCII/'
    shoudlEmpty = False
    for y in range(2):
        for x in range(6):
            if shoudlEmpty:
                time.sleep(0.1)
                os.system("clear")
                shoudlEmpty = False
                currentFilePath = outroMainPath + "e.txt"
                read_file(currentFilePath)
            else:
                time.sleep(0.05)
                os.system("clear")
                currentFilePath = outroMainPath + str(x) + ".txt"
                read_file(currentFilePath)
                shoudlEmpty = True

def end():
    def fix(firstTime):
        if firstTime:
            for x in range(5):
                print("\n")
        print("\t\t", end="")
        print("     ", end="")
    
    def blinkJoinUs():
        os.system("clear")
        firstTime = True
        text = "JOIN US"
        for x in range(2):
            if firstTime:
                fix(1)
                firstTime = False
            else:
                fix(0)
            print(colored(text, 'white', 'on_green'), end='\r')
            time.sleep(0.5)
            if firstTime:
                fix(1)
                firstTime = False
            else:
                fix(0)
            print(text, end='\r')
            time.sleep(0.5)
    blinkJoinUs()
    os.system("clear")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run skull animations")
    parser.add_argument("steps", nargs='+', type=int, choices=[1, 2, 3],
                        help="Specify which steps to run: 1=firstSkull, 2=secondSkull, 3=outro")

    args = parser.parse_args()
    if 1 in args.steps:
        firstSkull()
    if 2 in args.steps:
        secondSkull()
    if 3 in args.steps:
        outro()
    end()
