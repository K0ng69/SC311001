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
  i = 1
  sex =  'male'
  bmi = 21.15
  category =  'Overweight'
  print('No. {:<8} BMI {:>10}'.format('Sex', 'Category'))
  print(f'{i:02d}. {sex:<8} {bmi:.2f} {category}')
