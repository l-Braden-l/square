#Braden Leach
#January 10 2024
#Return Value Square


#----1----#
def square_number(num):
    return num**2

#----2----#
def add_squares(num1,num2):
    nums1 = square_number(num1)
    nums2 = square_number(num2)
    added =  nums1 + nums2
    return  added

#----3----#
def main():
    num1 =float(input('Enter the first number: '))
    num2 =float(input('Enter the second number: '))
    answer = add_squares(num1,num2)
    print(f'The sum of the squares of {num1} and {num2} is: {answer:.2f}')


main()