def lucky_number(name):
  number = len(name) * 9
  greeting = "Hello " + name + ". Your lucky number is " + str(number)
  return greeting

print(lucky_number("Kay"))
print(lucky_number("Cameron"))
