x0, v0, t = map(float, input("Введите через пробел значения для x0, v0, t: ").split())
a = 9.8

x=x0+v0*t-(a*t*t/2)
print("x(t)=",x)
#Объяснение: В отличии от математики, в программировании погрешность может зависеть от последовательности действий.

