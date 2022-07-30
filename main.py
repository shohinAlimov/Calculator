"""
  Theme: Calculator
  Aithor: Shohin ALimov
  Date: 26.07.2022
"""

import math
import time

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
ARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4n'


def add(input1, input2):
	output = input1 + input2
	print(output)


def minuse(input1, input2):
	output = input1 - input2
	print(output)


def multiply(input1, input2):
	output = input1 * input2
	print(output)


def division(input1, input2):
	output = input1 / input2
	print(output)


def factorial(input1):
	output = math.factorial(input1)
	print(output)


def sqrt(input1):
	output = math.sqrt(input1)
	print(output)


def power(input1, input2):
	output = math.pow(input1, input2)
	print(output)


running = True

print(OKBLUE + BOLD + "\tHello it's calculator\nWhat can do this calculator:" + ENDC)
time.sleep(1)

while running:
	print()
	print("1. Summarize numbers" + FAIL + BOLD + "(Type 1)" + ENDC)
	print("2. Minuse numbers" + FAIL + BOLD + "(Type 2)" + ENDC)
	print("3. Divide numbers" + FAIL + BOLD + "(Type 3)" + ENDC)
	print("4. Multiply numbers" + FAIL + BOLD + "(Type 4)" + ENDC)
	print("5. Find the factorial" + FAIL + BOLD + "(Type 5)" + ENDC)
	print("6. Find radical" + FAIL + BOLD + "(Type 6)" + ENDC)
	print("7. Find the power" + FAIL + BOLD + "(Type 7)" + ENDC)
	print("8. Exit " + FAIL + BOLD + "(Type 8)\n" + ENDC)

	Input = int(input("Type: "))

	if Input == 1:
		inputF = int(input("Type first number: "))
		inputS = int(input("Type second number: "))
		add(input1=inputF, input2=inputS)
		time.sleep(5)

	elif Input == 2:
		inputF = int(input("Type first number: "))
		inputS = int(input("Type second number: "))
		minuse(input1=inputF, input2=inputS)
		time.sleep(5)

	elif Input == 3:
		inputF = int(input("Type first number: "))
		inputS = int(input("Type second number: "))
		division(input1=inputF, input2=inputS)
		time.sleep(5)

	elif Input == 4:
		inputF = int(input("Type first number: "))
		inputS = int(input("Type second number: "))
		multiply(input1=inputF, input2=inputS)
		time.sleep(5)

	elif Input == 5:
		inputF = int(input("Type number: "))
		factorial(input1=inputF)
		time.sleep(5)

	elif Input == 6:
		inputF = int(input("Type number: "))
		sqrt(input1=inputF)
		time.sleep(5)

	elif Input == 7:
		inputF = int(input("Type first number: "))
		inputS = int(input("Type second number: "))
		power(input1=inputF, input2=inputS)
		time.sleep(5)

	elif Input == 8:
		running = False

	else:
		print(FAIL + BOLD + "INCORRECT" + ENDC)
