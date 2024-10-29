# # num1= int(input ('first ='))
# # num2= int(input('second ='))
# #
# # input('+, -, * :')
# # if '+':
# #  result = num1 + num2
# # elif '-':
# #   result = num1 - num2
# #  elif '*':
# #   result = num1 * num2
# #
# #  print(result)
#
#
#
# first_name = 'Okey'
# second_name = 'Henry'
# middle_name = 'Olisaemeka'
# date_of_birth = '1st December,2000'
# state_of_origin = 'Anambra'
#
# print(first_name)
# print(second_name)
# print(middle_name)
# print(date_of_birth)
# print(state_of_origin)
#
#
#
#
#
# first_w = 'My'
# second_w = 'name'
# third_w = 'is'
# fourth_w = 'Okechukwu'
# fifth_w = 'Okeke'
#
# print(first_w,second_w,third_w,fourth_w,fifth_w)
#
#
#
# first = int(input(':'))
# sec = 60
# min = 60
# hr = 24
# day = 7
# week = 4
# month_with_30 = (4 * ((week * day) + 2))
# month_with_31 = (7 * ((week * day) + 3))
# month_with_28 = (1 * (week * day))
# month = 12
# year = 1
#
#
# calc = first / (((sec*min)*hr)*(month_with_30 + month_with_31 + month_with_28) * year)
# print(f"{calc:.0f}")
#
# if calc <='60':
#     print('yes,very possible')
# else:
#     print('no')
#
#
#
#

#
# from math import sin,cos,pi
# x = pi/4
# one_val = (sin(x)**2) + (cos(x)**2)
# print(one_val)



time = int(input('time now: '))
alarm = int(input('numbers of hours to wait: '))
day_time = (time + alarm) % 24
day_hour = (time + alarm) // 24


print(f"{day_hour}day(s), {day_time}hour(s)")





















