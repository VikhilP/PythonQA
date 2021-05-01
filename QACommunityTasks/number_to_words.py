ones = ["", "one ","two ","three ","four ", "five ", "six ","seven ","eight ","nine ","ten ","eleven ",
"twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ","seventeen ", "eighteen ","nineteen "] 
 
twenties = ["","","twenty ","thirty ","forty ", "fifty ","sixty ","seventy ","eighty ","ninety "] 
 
thousands = ["","thousand ","million ", "billion ", "trillion ", "quadrillion ", "quintillion ", 
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
# print(lnum[1][2])




def n2w99():
    fullnum = ""
    # if len(lnum) == 1:
    #     num = int(lnum[0])
    #     if num == 0:
    #         print("zero")
    #     elif (num<20) :
    #         num2words = ones[num]
    #         print(num2words)
    #     elif num>=20 and num <100:
    #         if num%10 == 0 :
    #             temp = int(num/10)
    #             num2words = twenties[temp]
    #             print(num2words)
    #         else:
    #             digit = num%10
    #             tens = int((num-digit)/10)
    #             print(f"{twenties[tens]}{ones[digit]}")
    #     elif num >= 100:
    #         num = int(lnum[0])%100
    #         t = int(lnum[0])
    #         digit = num%10
    #         tens = int((num-digit)/10)
    #         id = thousands[len(lnum)-1]
    #         if num==0:
    #             print(f"{ones[t//100]} hundred")
    #         else:
    #             if num<20:
    #                 print(f"{ones[(t-num)//100]}hundred {ones[num]}")
    #             else:
    #                 print(f"{ones[(t-num)//100]}hundred {twenties[tens]}{ones[digit]}")
    # else:
        
    fake = len(lnum)
    for i in range(len(lnum)):
        num = int(lnum[i])%100
        t = int(lnum[i])
        id = thousands[len(lnum)-1]
        count=ones[(t-num)//100]
        if i == 0 and t<100:
            ##TO DO: finish off for the rest of the digits of the first array item
            if t < 20:
                fullnum = fullnum + f"{ones[t]} {thousands[(fake-i)-1]}"
                print("test1")
            elif t >=20:         
                if num%10 == 0:
                    tens = twenties[num//10]
                    fullnum = fullnum + f" {tens}  {thousands[(fake-i)-1]}"
                else:
                    digit = num%10
                    temp = int((num-digit)/10)
                    fullnum = fullnum + f"{count} {twenties[temp]} {ones[digit]}{thousands[(fake-i)-1]}"
            
    
        elif i < len(lnum)-1:
            count=ones[(t-num)//100]
            if t >99:
                if num==0:
                    fullnum = fullnum + f"{ones[t//100]} hundred {thousands[(fake-i)-1]} "
                    print("test2")
                # elif (int(lnum[i]) + num) == (100+num):
                #     if num<20:
                #         fullnum = fullnum + f"{ones[t]} hundred {thousands[(fake-i)-1]}"
                #         print("test3")
                #     else:
                #         fullnum = fullnum +  f"{ones[(t-num)//100]} hundred {twenties[tens]}{ones[digit]}{thousands[(fake-i)-1]}"
                #         print("test4")
                #     tens = twenties[num//10]
                #     fullnum = fullnum + f" {tens} hundred{thousands[(fake-i)-1]}"
                #     print("test5")
                elif num < 20:
                    fnum = ((int(lnum[i])-num))//100
                    fullnum = fullnum + f" {ones[fnum]}  hundred {ones[num]}{thousands[(fake-i)-1]}"
                    print("test6")
                elif num >=20 and num <100: 
                    if num%10 == 0:
                        tens = twenties[num//10]
                        fullnum = fullnum + f" {tens} hundred {thousands[(fake-i)-1]}"
                        print("test7")
                    else:
                        digit = num%10
                        temp = int((num-digit)/10)
                        fullnum = fullnum + f"{count} hundred {twenties[temp]} {ones[digit]}{thousands[(fake-i)-1]}"
                        print("test8")
            else:
                if t == 0:
                    continue
                elif t < 20:
                    fnum = ((int(lnum[i])-num))//100
                    fullnum = fullnum + f" {ones[num]} {thousands[(fake-i)-1]} "
                    print("test6")
                elif t >=20 and t <100: 
                    if num%10 == 0:
                        tens = twenties[num//10]
                        fullnum = fullnum + f" {tens}  {thousands[(fake-i)-1]}"
                        print("test7")
                    else:
                        digit = num%10
                        temp = int((num-digit)/10)
                        fullnum = fullnum + f"{twenties[temp]} {ones[digit]} {thousands[(fake-i)-1]}"
                        print("test8")


        elif i == (len(lnum)-1):
            num = int(lnum[i])%100
            t = int(lnum[i])
            digit = num%10
            tens = int((num-digit)/10)
            id = thousands[len(lnum)-1]
            if t == 0:
                break
            elif num==0:
                fullnum+=f"{ones[t//100]} hundred"
            else:
                if num<20:
                    fullnum+=f"{ones[(t-num)//100]}hundred {ones[num]}"
                    print("test44")
                else:
                    fullnum+=f"{ones[(t-num)//100]}hundred {twenties[tens]}{ones[digit]}"
                    print("test45")

    print (fullnum)


n2w99()



##can probably be optimsed

