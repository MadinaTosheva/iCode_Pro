#    Дано:
#      a = 5
#      v = "abc"
#      c = a + v
#    Чему равен print(с) ??

a = 5
v = "abc"
# c = a + v
# print(c) # В данном случае получаем ошибку "TypeError", где говорится, что нельзя сложить 'int' и 'str'

# Но есть другой вариант их сложение - type casting

# Решение 1
integer1 = str(5)
string1 = "abc"
sum1 = integer1 + string1
print(sum1)                                        ## sum1 = 5abc

# Решение 2
integer2 = 5
string2 = "abc"
sum2 = str(integer2) + string2
print(sum2)                                       ## sum2 = 5abc










