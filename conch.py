from PIL import Image
import sympy as sp
import os
import socket
import sys
from datetime import date
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

class consoleColors:
    def __init__(self):
        self.Red = '\033[91m'
        self.Green = '\033[92m'
        self.Yellow = '\033[93m'
        self.Blue = '\033[94m'
        self.Magenta = '\033[95m'
        self.Cyan = '\033[96m'
        self.White = '\033[97m'
        self.End = '\033[0m'
        self.Bold = '\033[1m'
        self.Underline = '\033[4m'
cl = consoleColors()

os.system("cls")

header = f"{cl.Yellow}{cl.Underline}Conch, the simple terminal shell.{cl.End}{cl.Green} (0.0.9a){cl.End}"
verinfo = f"{cl.Yellow}Conch,{cl.End}{cl.Green} version 0.0.9 {cl.End} {cl.Magenta}alpha{cl.End}"
os.system(f"title Conch, (0.0.9a)")

print(header)

while True:
    inp = input(f"{cl.Cyan}{cl.Bold}@{cl.Blue}> {cl.End}")
    inp = inp.lstrip(" ")
    inp = inp.split(" ")
    if inp[0] == "say":
        print(" ".join(inp[1:]))
    elif inp[0] == "clear":
        os.system("cls")
        print(header)
    elif inp[0] == "conch" or inp[0] == "version":
        print(verinfo)
    elif inp[0] == "python":
        inp = " ".join(inp[1:])
        try:
            eval(inp)
        except:
            print(f"{cl.Red}<!>{cl.Yellow} It threw an exception.{cl.End}")
    elif inp[0] == "cmd":
        inp = " ".join(inp[1:])
        os.system(inp)
    elif inp[0] == "date":
        print(date.today())
    elif inp[0] == "network" or inp[0] == "ip":
        hostname = socket.gethostname()
        ipv4 = socket.gethostbyname(hostname)
        print(f"{cl.Yellow}{cl.Bold}Network Info{cl.End}")
        print(f"{cl.Magenta}Hostname: {cl.Green}{hostname}")
        print(f"{cl.Magenta}IPv4 Address: {cl.Green}{ipv4}")
    elif inp[0] == "link":
        inp = " ".join(inp[1:])
        inp = inp.lstrip("https://")
        os.system(f"start https://{inp}")
    elif inp[0] == "round":
        try:
            print(round(float(inp[1]), int(inp[2])))
        except ValueError:
            try:
                print(float(inp[1]))
            except ValueError:
                print(f"{cl.Red}<!>{cl.Yellow} '{inp[1]}' is not a valid number.{cl.End}")
            try:
                print(float(inp[2]))
            except ValueError:
                print(f"{cl.Red}<!>{cl.Yellow} '{inp[2]}' is not a valid integer.{cl.End}")
    elif inp[0] == "calculate" or inp[0] == "calc":
        inp = " ".join(inp[1:])
        try:
            print(sp.sympify(inp))
        except ValueError:
            print(f"{cl.Red}<!>{cl.Yellow} Calculation is not a valid expression.{cl.End}")
    elif inp[0] == "read":
        inp = " ".join(inp[1:])
        try:
            readfile = open(rf"{inp}", "r").read()
            print(readfile)
        except FileNotFoundError:
            inp = inp.split("\\")[-1]
            print(f"{cl.Red}<!>{cl.Yellow} '{inp}' does not exist.{cl.End}")
    elif inp[0] == "replace":
        try:
            r1 = inp[1]
            r2 = inp[2]
            inp = " ".join(inp[3:])
            print(inp.replace(r1, r2))
        except IndexError:
            print(f"{cl.Red}<!>{cl.Yellow} Not enough arguments given (expected 3){cl.End}")
    elif inp[0] == "exit":
        sys.exit()
    else:
        print(f"{cl.Red}<!>{cl.Yellow} '{inp[0]}' is not a valid command.{cl.End}")