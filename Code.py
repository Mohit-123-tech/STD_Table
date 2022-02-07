#! /usr/bin/python3
from os import system
import pandas as pd


class Code:
    def __init__(self) -> None:
        system("clear")

    def App(self):
        std = {
            "name": [],
            "age": [],
            "marks": []
        }

        FileName = input("Enter File name : ")
        FileName = FileName+".xls"

        while(True):
            system("clear")
            print("type exit in name for exit \n")
            namein = input("Enter name : ")

            if (namein == "exit"):
                df = pd.DataFrame(std)
                df.to_excel(FileName, index=0)
                system(f'mv {FileName} /home/kali/Desktop')
                break

            try:
                agein = int(input("Enter age : "))
            except(ValueError) as e:
                print(e)

            marksin = input("Enter marks : ")

            std["name"].append(namein)
            std["age"].append(agein)
            std["marks"].append(marksin)


if __name__ == "__main__":
    Ap = Code()
    Ap.App()
