def SquareArea():
  W = int(input('Width : '))
  L = int(input('Long : '))
  
  if W == L :
    R = W * L
    print(f'Square area : {R}')
  else :
    print(f"Width {W} Long {L}\nisn't square")

def SId():
  U = input('Student ID : ')
  if int(U[-1]) % 2 == 0 :
    print(f'{U} is even number')
  else :
    print(f'{U} is odd number')

if __name__ == "__main__":
  SquareArea()