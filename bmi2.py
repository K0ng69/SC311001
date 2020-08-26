n_person = int(input('Number of person => '))
n_male = 0
n_female = 0
sumBmi_male = 0
sumBmi_female = 0
bmi_text = ''

for i in range(1, n_person+1):
  sex = input('\nsex (m/f) => ')
  height = float(input('height (m) => '))
  weight = float(input('weight (kg) => '))
  hm = height / 100
  bmi = weight /  (hm**2)

  if sex == 'm':
    n_male += 1
    sumBmi_male += bmi
  else:
    n_female += 1
    sumBmi_female += bmi

  if bmi <= 18.5:
    category = 'Underweight'
  elif 18.5 <= bmi <= 24.9:
    category = 'Normal weight'
  elif 25 <= bmi <= 29.9:
    category = 'Overweight'
  else:
    category = 'Obesity'

  bmi_text += f'{i:02d}. {sex}   {bmi:.2f} {category}\n'
avgBmi = (sumBmi_male + sumBmi_female) / n_person

print('\nNo. Sex Bmi   Category')
print(bmi_text)
if sumBmi_male != 0:
  avgBmi_male = sumBmi_male/n_male
  print(f'Average bmi of male = {avgBmi_male:.2f}')
if sumBmi_female != 0:
  avgBmi_female = sumBmi_female/n_female
  print(f'Average bmi of female = {avgBmi_female:.2f}')
print(f'Average bmi = {avgBmi:.2f}')