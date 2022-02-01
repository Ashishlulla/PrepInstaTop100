num1 = int(input('Enter the numerator for 1st fraction :'))
den1 = int(input('Enter the denominator for the 1st fraction :'))
num2 = int(input('Enter the numerator for 2nd fraction :'))
den2 = int(input('Enter the denominator for the 2nd fraction :'))
if den1 == den1:
    Fraction = num1 + num2
    print('Addition of two fractions are :' + str(Fraction) + '/' + str(den1))
else:
    Fraction = (num1 * den2) + (num2 * den1)
    print('Addition of fractions are :' + str(Fraction) + '/' + str(den1 * den2))
