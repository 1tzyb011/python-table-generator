num = int(input('put the number you want the table of(Integers only): '))
for i in range(20):
  print(num," X ", i, "=", num * i)
  if(i == 10):
    break

print('\nTable done :)')
