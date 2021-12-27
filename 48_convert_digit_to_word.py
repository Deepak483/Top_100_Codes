# function creation
def digit_to_word(n):

    words_upto_19 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'sixteen', 'eighteen', 'nineteen']

    words_upto_tens = ['', '', 'twenty', 'thirty', 'forty',
                       'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if n == 0:
        output = 'zero'
    elif n <= 19:
        output = words_upto_19[n]
    elif n <= 99:
        output = words_upto_tens[n//10] + " " + words_upto_19[n % 10]
    else:
        print("Please enter the value between range 0 and 99")

    return output


n = int(input("enter the digit: "))
print(digit_to_word(n))
