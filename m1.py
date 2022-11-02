# This is a sample Python script.
import math
ex = int(input('Введите номер упражнения '))
if ex == 11:
    e = 0.5e-8
    def nonReduced(x):
        sum, avr, k = 0.0, 0.0, 1
        counter = 0
        while k:
            avr = 1 / (k * (k + x))
            sum += avr
            k += 1
            if avr < e:
                counter = k - 1
                k = 0
        return counter, sum - 1


    def onReduced(x):

        sum, avr, k = 0.0, 0.0, 1
        counter =0
        while k:
            avr = 1 / (k * (k + 1) * (k + x))
            sum += avr
            k += 1
            if avr < e:
                counter = k - 1
                k = 0
        return counter, (1-x)*sum
    x = 0.9
    print('X =', x)
    nred = nonReduced(x)
    print('Not reduced', 'N = ' + str(nred[0]), nred[1], sep='\n')
    red = onReduced(x)
    print('Reduced', 'N = ' + str(red[0]), red[1], sep='\n')
    print()
    x = 0.5
    print('X =', x)
    nred = nonReduced(x)
    print('Not reduced', 'N = ' + str(nred[0]), nred[1], sep='\n')
    red = onReduced(x)
    print('Reduced', 'N = ' + str(red[0]), red[1], sep='\n')


elif ex == 12:
    e = 3e-8
    def Reduce(x):
        mejoberry, tintoberry, kible = 0.0, 0.0, 1
        counter = 0
        while kible:
            tintoberry = 1 / math.sqrt(kible ** 3 + x)
            mejoberry += tintoberry
            kible += 1
            if tintoberry < e:
                counter = kible - 1
                kible = 0
        return counter, mejoberry


    def nonReduce(x):
        mer, rer, ser = 0.0, 0.0, 1
        counter = 0
        while ser:
            rer = (math.sqrt(ser ** 3 - x) - math.sqrt(ser ** 3 + x)) / math.sqrt(ser ** 6 - x ** 2)
            mer += rer
            ser += 1
            if rer < e:
                counter = ser - 1
                ser = 0
        return counter, mer


    print('X = 0.5')
    x = 0.5
    a1 = Reduce(x)
    a2 = Reduce((-1) * x)
    j = a1[1] - a2[1]
    print('Not reduced', 'N = ' + str(a1[0] + a2[0]), j, sep='\n')
    m = nonReduce(x)
    print('Reduced', 'N = ' + str(m[0]), m[1], sep='\n')
    print()
    print('X = 0.999999999')
    x = 0.999999999
    a1 = Reduce(x)
    a2 = Reduce((-1) * x)
    j = a1[1] - a2[1]
    print('Not reduced', 'N = ' + str(a1[0] + a2[0]), j, sep='\n')
    m = nonReduce(x)
    print('Reduced', 'N = ' + str(m[0]), m[1], sep='\n')


elif ex == 13:
    e = 0.5e-10
    def slope():
        sum, avr, n = 0.0, 0.0, 1
        counter = 0
        while n:
            avr = 1 / (n ** 2 + 1)
            sum += avr
            n += 1
            if avr < e:
                counter = n - 1
                n = 0
        return counter, sum
    def salmon():
        f, avr, n = 0.0, 0.0, 1
        counter = 0
        while n:
            avr = 1 / (n ** 4 * (n ** 2 + 1))
            f += avr
            n += 1
            if avr < e:
                counter = n
                n = 0
        return counter, f
    file = slope()
    print('Not reduced', 'N = ' + str(file[0]), file[1], sep='\n')
    pi = math.pi
    fish = salmon()
    print('Reduced', 'N = ' + str(fish[0]), ((pi ** 2 / 6) - (pi ** 4 / 90) + fish[1]), sep='\n')

input()