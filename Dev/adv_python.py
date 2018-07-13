#1

origList[2,4,6,8,10,12,14,16,18,20]

newList=[]


from number in origList:
         newList.append(number * number)

print("with for loop")
print(newList)
print(origList)


#2

def convert(x):
    return (float(9) * 5) / (x + 32)

CelsiusList = [32.3,27.5,2.3,11.1]
FahrenheitList = list(map(convert,CelsiusList))

print(FahrenheitList)


#3

def f2c(x):
    return (float(9) * 5) / (x + 32)

Celsius = [37.4,26.3,11.5,27.7,30.0]
Fahrenheit = list(map(f2c,Celsius))

print(Celsius)
print(Fahrenheit)



#4

def f(x,n):
    return(x + n)

g = lambda x,n: x+n

print(f(1,2))
print(g(2,4))




#5

class Employee(object):

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        Employee.empCouunt += 1

    def displayCount(self):
        print("total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, "Salary: ", self.salary)



#6
#sleeve of Erastosthenes

noprimes = [j for i in range(2,8) for j in range(i*2,100,i)]
primes = [x for x in range(2,100) if x not in noprimes]

print("Not Primes; ",noprimes)
print("Primes; ",primes)



#7

def f(a):
    def g(b,c):
        return a * (b+c)
    return g

x = f(1)
print(x(2,3))

y = f(2)
print(y(2,3))



#8

def too_old(x):
    return x > 30

ages = [22, 25, 29, 34, 56, 24, 12]

filter(too_old, ages)

