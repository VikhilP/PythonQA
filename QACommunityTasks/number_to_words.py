ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ",
"twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "] 
 
twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "] 
 
thousands = ["hundred","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", 
"sextillion ", "septillion ","octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", 
"tredecillion ", "quattuordecillion ", "quindecillion", "sexdecillion ", "septendecillion ", "octodecillion ", "novemdecillion ", "vigintillion "] 

num_to_convert = input("enter a number ")

number = int(num_to_convert)

num2words = ""
# [number[i:i+3]] 
lnum = []
snumber = (str(number))[::-1]

##puts it into groups of 3
for i in range (0, len(snumber), 3):
    lnum.append(snumber[i:i+3])


print(lnum)
#reverses individual elements
for i in range(len(lnum)):
    lnum[i] = lnum[i][::-1]
#reverse the list again
lnum = lnum[::-1]
print(lnum)



def n2w99():
    if number == 0:
        print("zero")
    elif (number<20) :
        num2words = ones[number]
        print(num2words)
    elif number>=20 and number <100:
        if number%10 == 0 :
            temp = int(number/10)
            num2words = twenties[temp]
            print(num2words)
        else:
            digit = number%10
            tens = int((number-digit)/10)
            print(f"{twenties[tens]}{ones[digit]}")
    else:
        fullnum = ""
        fake = len(lnum)
        for i in range(len(lnum)):
            num = int(lnum[i])%100
            t = int(lnum[i])
            id = thousands[len(lnum)-1]
            if num==0:
                fullnum = fullnum + f"{ones[t//100]} {thousands[(fake-i)-1]} "
            elif (int(lnum[i]) + num) == (100+num):
                tens = twenties[num//10]


                fullnum = fullnum + f" {tens} {thousands[(fake-i)-1]}"
            elif num < 20:
                fnum = ((int(lnum[i])-num))//100
                fullnum = fullnum + f" {ones[fnum]} {thousands[(fake-i)-1]} {ones[lnum[i]]}"
            elif num >=20 and num <100: 
                if num%10 == 0:
                    tens = twenties[num//10]
                    fullnum = fullnum + f" {tens} {thousands[(fake-i)-1]}"
                else:
                    digit = num%10
                    temp = int((num-digit)/10)
                    fullnum = fullnum + f"{twenties[temp]} {ones[digit]} {thousands[(fake-i)-1]}"
        print (fullnum)


n2w99()
