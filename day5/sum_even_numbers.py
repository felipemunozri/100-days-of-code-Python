# Mi codigo
#Write your code below this row 👇
sum = 0

for n in range (1, 101):
    if n % 2 == 0:
        sum += n

print(sum)

# Respuesta
#Write your code below this row 👇

even_sum = 0
for number in range(2, 101, 2):
  # print(number)
  even_sum += number
print(even_sum)
  
#or

alternative_sum = 0
for number in range(1, 101):
  if number % 2 == 0:
    # print(number)
    alternative_sum += number
print(alternative_sum)