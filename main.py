number1 = float(input("Введите первое число: "))  # запршиваем у пользователя первое число
number2 = float(input("Введите второе число: "))  # запршиваем у пользователя втрое число
if number1 > number2 : # используем оператор ветвления if с условием, что число 2 меньше числа 1
   print("Наимененьшее значение:", number2) # выводим число 2, тк. оно наименьшее
elif number1 < number2 : # если первое условие ложное, значит число 1 меньше числа 2
   print("Наименьшее значение:", number1) # выводим число 1, тк. оно наименьшее
else: # если первое и второе условие ложное, значит числа равны
   print("Числа равны") # выводим что числа равны