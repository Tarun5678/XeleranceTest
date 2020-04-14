# problem 1
# This programs displays fibonacci series and displays sum of odd numbers in series


odd_array = []
fib_array = []


def fibonacci(max_value):
    x = 0
    y = 1
    count = 0
    if max_value < 0:
        print("Incorrect input")
    elif max_value == 0:
        return x
    elif max_value == 1:
        return y
    else:
        while x < max_value:
            fib_array.append(x)
            if x % 2 == 1:
                odd_array.append(x)
            z = x + y
            x = y
            y = z
            count += 1
        return fib_array, sum(odd_array)


if __name__ == '__main__':
    num_max = input("Please enter the maximum value:")
    fib, sum_odd = fibonacci(int(num_max))
    print("The fibonacci series is:",fib)
    print("The sum of odd values in fibonacci series is:", sum_odd)


