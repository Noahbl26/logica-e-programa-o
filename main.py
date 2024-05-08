'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
idade = int(input("por favorinsira a sua idade"))

if idade <=12:
    print("você é uma criança.")
elif 13<= idade <= 19:
    print("você é um adolescente.")
elif 20<= idade <= 59:
    print("você é um adulto.")
else:
    print("você é um idoso")