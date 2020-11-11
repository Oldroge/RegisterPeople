date = []
woman = []
old = []
people = average = wom = oldder = 0
while True:
    person = {'Name': str(input('Name: ')),
              'Gender': str(input('Gender: [M/W] ')).strip().upper()[0]}
    while person['Gender'] not in 'WwMm':
        print('Invalid gender! Try again!')
        person['Gender'] = str(input('Gender: [M/W] ')).strip().upper()[0]
    person['Age'] = int(input('Age: '))
    date.append(person.copy())
    people += 1
    if person['Gender'] in 'W':
        woman.append(person['Name'])
        wom += 1
    average += person['Age']
    if person['Age'] > 30:
        old.append(person['Name'])
        oldder += 1
    answer = str(input('Continue: [Y/N] ')).strip().upper()[0]
    while answer not in 'YyNn':
        print('Invalid option! Only (Yes/Not) options...')
        answer = str(input('Continue: [Y/N] ')).strip().upper()[0]
    if answer in 'N':
        break
print(f'A) {people} people were added')
print(f'B) The average age is {average/people:2f}')
print(f'C) There are {wom} women: {woman}')
print(f'D) There are {oldder} people above average age: {old}')
