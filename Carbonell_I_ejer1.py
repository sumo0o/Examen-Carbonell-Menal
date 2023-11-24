# Este programa sirve para determinar el numero mas alto
# y la media de los numeros ingresados por el usuario
def programa_1():
  max_num = int(input("Introduce un número: "))
  sum_nums = max_num
  secuencia = True 
  for i in range(9):
    num=int(input("Introduce otro número "))
    sum_nums += num
  if num > max_num:
    num = max_num 
  print("The largest number is: ", max_num )
  print("The average is:", sum_nums//10 )
programa_1()
