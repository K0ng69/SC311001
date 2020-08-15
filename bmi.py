data_list = []

def getBmi():
  i = 0
  print('No. {:<8} BMI {:>10}'.format('Sex', 'Category'))

  for sex, h, w in data_list:
    i+=1
    h = float(h)
    w = float(w)
    hm = h / 100
    bmi = w / (hm**2)

    if bmi <= 18.5:
      category = 'Underweight'
    elif 18.5 <= bmi <= 24.9:
      category = 'Normal weight'
    elif 25 <= bmi <= 29.9:
      category = 'Overweight'
    else:
      category = 'Obesity'

    sex = 'male' if sex == 'm' else 'female'
    print(f'{i:02d}. {sex:<8} {bmi:.2f} {category}')

def getData():
  des1 = 'Enter Sex, Height, Weight (Ex: m 176 52)\n(m = male, f = female)\n'
  print(des1)
  data  = tuple(input("=> ").split())
  if len(data) == 3 and data[1].isdigit() and data[2].isdigit() and (data[0] == 'm' or data[0] == 'f'):
    data_list.append(data)
    print(data[1])
  else:
    des2 = 'Incorrect data!\n'
    print(des2)
    getData()
  return main()

def main():
  if not data_list:
    getData()
  else:
    print('Calculate or add more? (cal, add, exit)\n')
    c = input('=> ')
    if c == 'cal':
      getBmi()
    elif c == 'add':
      getData()
    elif c == 'exit':
      exit
    else:
      main()

if __name__ == "__main__":
  main()