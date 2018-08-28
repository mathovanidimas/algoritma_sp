n=int(input("masukkan angka :")) 
fib1=0
fib2=1
fib=0
for i in range(n):
  fib1=fib2
  fib2=fib
  fib=fib1+fib2
  print(fib)