class Loop:
    # Count = 0

    def Print_1_1_1_1_1(self):
        i = 1
        while i <= 5:
            print('1', end=' ')
            i += 1

    def Print_1_2_3_4_5(self):
        i = 1
        while i <= 5:
            print(i, end=' ')
            i += 1

    def Print_1_3_5_7_9(self):
        i = 1
        while i <= 10:
            print(i, end=' ')
            i += 2

    def Print_3_6_9_12_15(self):
        i = 3
        while i <= 15:
            print(i, end=' ')
            i += 3

    def Multiples_3_and_5(self):
        i = 1
        while i <= 50:
            if i % 3 == 0 and i % 5 == 0:
                print(i, end=' ')
            i += 1

    def Multiples_3_or_5(self):
        i = 1
        while i <= 50:
            if i % 3 == 0 or i % 5 == 0:
                print(i, end=' ')
            i += 1

    def Divisors_of_given_number(self, div):
        i = 1
        while i <= div:
            if div % i == 0:
                print(i, end=' ')
            i += 1

    def Count_of_Divisors_of_given_number(self, div):
        i = 1
        count = 0
        while i <= div:
            if div % i == 0:
                count += 1
            i += 1
        print("Count of Divisors of given number is ", count)

    def Prime_Number(self, div):
        i = 2
        count = 0
        while i <= div // 2:
            if div % i == 0:
                # print("Not a Prime Number")
                count += 1
                break
            i += 1
        if count == 0:
            # print("Prime Number")
            print(div, end=' ')
            self.Count += 1
        return self.Count

    def Reverse_Printing_a_number(self):
        i = 10
        while i > 0:
            print(i, end=' ')
            i -= 1

    def Count_of_Digits(self, num):
        rev = 0
        count = 0
        while num > 0:
            n = num % 10
            rev = rev * 10 + n
            num //= 10
            count += 1
        print("Count of Digits is ", count)

    def Sum_of_Digits(self, num):
        total = 0
        while num > 0:
            n = num % 10
            total = total + n
            num //= 10
        return total

    def Reverse_the_Number(self, num):
        rev = 0
        while num > 0:
            n = num % 10
            rev = rev * 10 + n
            num //= 10
        print("Reverse Printing a number is ", rev)

    def Palindrome(self, num):
        rev = 0
        match = num
        while num > 0:
            n = num % 10
            rev = rev * 10 + n
            num //= 10
        if match == rev:
            print("Palindrome")
        else:
            print("Not a Palindrome")

    def Armstrong_Number(self, num):
        a = 0
        match = num
        while num > 0:
            n = num % 10
            pow = n * n * n
            a = a + pow
            num //= 10
        if match == a:
            print("Armstrong Number")
        else:
            print("Not a Armstrong Number")

    def Neon_Number(self, num):
        a = 0
        pow = num * num
        while pow > 0:
            n = pow % 10
            a = a + n
            pow //= 10
        if num == a:
            print(num, " Neon Number")
        else:
            print(num, " Not a Neon Number")

    def Factorial(self, num):
        i = 1
        total = 1
        while i <= num:
            total = total * i
            i += 1
        return total

    def Strong_Number(self, num):
        a = 0
        match = num
        while num > 0:
            n = num % 10
            r = obj.Factorial(n)
            a = a + r
            num //= 10
        if a == match:
            print("Strong Number")
        else:
            print("Not a Neon Number")

    def Addition_of_first_n_numbers(self, num):
        i = 1
        total = 0
        while i <= num:
            total = total + i
            i += 1
        print("Addition of first n numbers is ", total)

    def Greatest_Common_Divisor(self, no1, no2):
        div = 2
        gcd = 0
        if no1 < no2:
            small = no1
        else:
            small = no2
        print(small)
        while (div <= small):
            if no1 % div == 0 and no2 % div == 0:
                gcd = div
            div += 1
        print("Greatest Common Divisor is ", gcd)

    def Least_Common_Multiples(self, no1, no2):
        if no1 > no2:
            big = no1
        else:
            big = no2
        while True:
            if big % no1 == 0 and big % no2 == 0:
                print("Least Common Multiple is ", big)
                break
            big += 1

    def Find_power(self, no, pow):
        power = 1
        i = 1
        while i <= pow:
            power = power * no
            i += 1
        # print(no, " power of ", pow, " is ", power)
        return power

    def Decimal_To_Binary(self, no):
        binary = ""
        n = no
        while no > 0:
            rem = no % 2
            binary = str(rem) + binary
            no //= 2
        print("Binary Value of ", n, " is ", binary)

    def Binary_to_Decimal(self, num):
        decimal = 0
        no = num
        i = 0
        while num > 0:
            n = num % 10
            pow = n * obj.Find_power(2, i)
            decimal = decimal + pow
            i += 1
            num //= 10
        print("Decimal Value of ", no, " is ", decimal)

    def Fibonacci_Series(self):
        first, second = 0, 1
        third = 0
        while first <= 100:
            print(first, end=' ')
            third = first + second
            first = second
            second = third

    def Swapping_two_numbers(self, no1, no2):
        no3 = no1
        no1 = no2
        no2 = no3
        print(no1, no2, end='')

    def Swapping_without_third_variable(self, no1, no2):
        no2 = no1 + no2
        no1 = no2 - no1
        no2 = no2 - no1
        print(no1, ' ', no2, end=' ')

    def Fibonacci_without_using_third_variable(self):
        first, second = 0, 1
        while first <= 13:
            print(first, end=' ')
            second = first + second
            first = second - first

    def First_n_Prime_Numbers(self, i):
        no = 2
        Prime_no_count = self.Prime_Number(no)
        while Prime_no_count < i:
            no += 1
            Prime_no_count = self.Prime_Number(no)
        print("\nPrime Number count is ", self.Count)

    def Sum_of_Digits_until_it_becomes_single_digit(self, num):
        total = self.Sum_of_Digits(num)
        if total > 0:
            total = self.Sum_of_Digits(total)
        print("Sum of Digits until it becomes single digit is ", total)

    def Printing_5fact_4fact_3fact_2fact_1fact_(self):
        i = 5
        while i >= 1:
            fact = self.Factorial(i)
            print("Factorial of ", i, " is ", fact)
            i -= 1

    def Printing1(self):
        i, j = 1, 10
        while i <= 4:
            print(i*j)
            i += 1
            j -= 1

    def Printing_1_11_121(self):
        i = 1
        while i <= 121:
            print(i)
            i *= 11

    def Printing_1_4_9_16_25_36_49_64_81_100(self):
        i = 1
        while i <= 10:
            print(i*i, end=' ')
            i += 1

    def Square_Root_of_a_Number(self, m):
        n = 2
        while n <= m/2:
            if m/n == n:
                print(n)
                break
            n += 1

    def Prime_no_in_a_fibonacci_series(self):
        first, second = 0, 1
        i = 2
        while first <= 200:
            if first % i == 1:
                print(first, end=' ')
                second = first + second
                first = second - first
            i += 1


obj = Loop()
# obj.Print_1_1_1_1_1()
# obj.Print_1_2_3_4_5()
# obj.Print_1_3_5_7_9()
# obj.Print_3_6_9_12_15()
# obj.Multiples_3_and_5()
# obj.Multiples_3_or_5()
# obj.Divisors_of_given_number(100)
# obj.Count_of_Divisors_of_given_number(100)
# obj.Prime_Number(11)
# obj.Reverse_Printing_a_number()
# obj.Count_of_Digits(12345)
# obj.Sum_of_Digits(9263)
# obj.Reverse_the_Number(12345)
# obj.Palindrome(1223)
# obj.Armstrong_Number(371)
# obj.Neon_Number(i)
# print(obj.Factorial(5))
# obj.Strong_Number(145)
# obj.Addition_of_first_n_numbers(10)
# obj.Greatest_Common_Divisor(300, 150)
# obj.Least_Common_Multiples(3, 9);
# obj.Find_power(2, 5)
# obj.Decimal_To_Binary(12)
# obj.Binary_to_Decimal(1010)
# obj.Fibonacci_Series()
# obj.Swapping_two_numbers(32, 42)
# obj.Swapping_without_third_variable(34, 54)
# obj.Fibonacci_without_using_third_variable()
# obj.First_n_Prime_Numbers(10)
# obj.Sum_of_Digits_until_it_becomes_single_digit(2376)
# obj.Printing_5fact_4fact_3fact_2fact_1fact_()
# obj.Printing1()
# obj.Printing_1_11_121()
# obj.Printing_1_4_9_16_25_36_49_64_81_100()
# obj.Square_Root_of_a_Number(4)
obj.Prime_no_in_a_fibonacci_series()

