import os

def clear():
    if os.name =='posix':
        _ = os.system('clear')
    elif os.name =='nt':
        _ = os.system('cls')


def menu():
    print("""
Opciones
---------------
[1]-
[2]-
[3]-
[4]-
[5]-
[6]-
[7]-
[8]-

---------------
""")

while True:
  menu()
  ans = int(input("Opcion: ")
  if ans == 1:
    print()
  elif ans == 2:
    print()
  else:
    print("Opcion incorrecta Pibe")
