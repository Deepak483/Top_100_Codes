# 9999
n = int(input("enter the number: "))
unit_place = ['', 'One', 'Two', 'Three', 'Four',
              'Five', 'Six', 'Seven', 'Eight', 'Nine', '', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

tens_place = ['', '', 'Twenty', 'Thirty', 'Forty',
              'Fifty', 'Sixty', 'Seventy', 'Eighty', "Ninety"]


if n == 0:
    output = unit_place[n]
elif n <= 99:
    output = tens_place[n//10] + " " + unit_place[n % 10]
elif n <= 999:
    output = unit_place[n//100] + " Hundred" + \
        tens_place[n//10] + unit_place[n % 10]
elif n <= 9999:
    output = unit_place[n//1000] + " Thousand" + unit_place[n //
                                                            100] + " Hundred" + tens_place[n//10] + unit_place[n % 10]
else:
    print("Please , don't enter number greater than five digit!!")


print(output)
