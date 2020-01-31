#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

#j = 0
#for i in range(0, 5):
#    i= i + 1
#    print(i, j)

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
#i = 0
#n = 0
#for i in range(10):
#    dig = input('введите число: ')
#    if dig == '5':
#        n = n+1

#print('количество введенных цифр 5 =', n)





'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
#n = 1
#for i in range(2,10):
#    print('i= ',i)
#    n = n * i
#    print('n= ',n)

#print(n)


'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# d = 0
# integer_number = 212951
# print(integer_number%10,integer_number//10)
# while integer_number>0:
#     d = d + integer_number%10
#     print(integer_number%10)
#     integer_number = integer_number//10
#
#
# print(d)



'''
Задача 7
Найти произведение цифр числа.
'''
# d = 1
# integer_number = 2129404
# print(integer_number)
# print()
# while integer_number>0:
#     if integer_number%10 != 0:
#         d = d * int(integer_number%10)
#     else: d = d * 1
#     print(integer_number%10, integer_number//10, 'd=', d)
#     integer_number = integer_number//10
#
# print('произведение чисел', d)


'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
'''
integer_number = 213413
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')
'''
'''
Задача 9
Найти максимальную цифру в числе
'''
# z = 0
# integer_number = 92846550
# while integer_number>0:
#     if integer_number%10 > z:
#        z = integer_number%10
#     else: z = z * 1
#     integer_number = integer_number//10
# print(z)


'''
Задача 10
Найти количество цифр 5 в числе
'''

z = 0
integer_number = 92846550555555
while integer_number>0:
    if integer_number%10 == 5:
       z = z + 1
    else: z = z * 1
    integer_number = integer_number//10
print(z)
