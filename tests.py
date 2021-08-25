# 1 Создать функцию, принимающую в качестве параметра список (list) 
# целых чисел и возвращающую сумму квадратов всех нечетных чисел в данном списке.

def square_it(numArr):
    return sum(i*i for i in numArr if i % 2 != 0)

print(square_it([1, 2, 3, 4, 5]))

#  2 Создать итератор, который принимает в конструктор итерируемый объект и признак чет/нечет 
# и возвращает только элементы с четной или нечетной (в соответствии с признаком, переданным в конструктор) 
# позицией в итерируемом объекте. Например, для последовательности a, b, c, d чет вернет b, d (2-й и 4-й элементы), 
# а нечет a, c  (1-й и 3-й элементы). Сделать в двух вариантах:
#  1) Класс итератор.
#  2) Генератор.

class OddEvenIterator:
    def __init__(self, numArr, factor):
        self.numArr = numArr
        self.factor = factor
        self.counter = -1
        self.limit = 0

    def __iter__(self):
        return self

    def __next__(self):   
        if self.factor == 'even':
            self.counter += 2
            return self.numArr[self.counter]
        elif self.factor == 'odd':
            if self.limit == 0:
                self.counter = 0
                self.limit = 1
                return self.numArr[self.counter]
            else: 
                self.counter += 2
                return self.numArr[self.counter]

a = OddEvenIterator([1, 2, 3, 4, 5], 'odd')
print(next(a))
print(next(a))
print(next(a))

# 3 Создать функцию принимающую на вход массив целых чисел, все элементы которого имеют значение либо 1, либо 2.
#  Функция должна сортировать его так, чтобы сперва шли 2, а потом 1 (то есть, вход вида [1,2,2,1,1,2,1], 
#  выход вида [2,2,2,1,1,1,1]). Не использовать стандартных
#  функций сортировки из библиотеки Питона и сделать сортировку за линейное время и один проход массива.

def sortArr(numArr):
    one_list = []
    two_list = []
    for i in range(len(numArr)):
        if numArr[i] == 1:
            one_list.append(numArr[i])
        if numArr[i] == 2:
            two_list.append(numArr[i])
    return one_list + two_list

    
print(sortArr([1, 2, 1, 2, 1, 1]))




