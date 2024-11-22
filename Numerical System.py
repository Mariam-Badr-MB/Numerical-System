def octal_to_hex(number):
    #Converts an octal number to its hexadicmal equivalent.

    binary_number = ""
    octal_digits = {"0": "000", "1": "001", "2": "010", "3": "011",
                  "4": "100", "5": "101", "6": "110", "7": "111"}

    for digit in number:
          binary_number += octal_digits[digit]
    hex_numberlist = [000 , 1 , 10 , 11 , 100 , 101 , 110 ,111,1000,1001,1010,1011,1100,1101,1110,1111]
    hex_num = []
    while int(binary_number) > 0 :
       digit = int(binary_number)%10000
       y = hex_numberlist.index(digit)
       if y == 10 :
          y = "A"
       if y == 11:
         y = "B"
       if y == 12 :
          y = "C"
       if y == 13 :
         y= "D"
       if y == 14 :
         y = "E"
       if y == 15:
          y = "F"
       hex_num.append(y)
       binary_number = int(binary_number)//10000
    hex_num.reverse()
    hex_num = "".join(map(str,hex_num))
    return hex_num

def hexa_to_octal(number):
    binary_num = ""
    hexal_digits = {"0": "0000", "1": "0001", "2": "0010", "3": "0011",
                    "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010",
                    "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    for x in number:
        binary_num += hexal_digits[x]

    octal_numberlist = [000, 1, 10, 11, 100, 101, 110, 111]
    octal_number = []
    while int(binary_num) > 0:
        digit = int(binary_num) % 1000
        octal_number.append(octal_numberlist.index(digit))
        binary_num = int(binary_num) // 1000
    octal_number.reverse()
    octal_num = "".join(map(str, octal_number))
    return octal_num

def dec_to_oct(number):
    oct_num = ''
    while number > 0:
        oct_digit = number % 8
        oct_num = str(oct_digit) + oct_num
        number = number // 8
    return oct_num if oct_num else '0'

def oct_to_dec(number):
    dec_num = 0
    x=0
    while number>0 :
        digit=number%10
        dec_num +=digit*(8**x)
        number=number//10
        x +=1
    return dec_num

def octal_to_binary(number):
    #Converts an octal number to its binary equivalent.

    binary_number = ""
    octal_digits = {"0": "000", "1": "001", "2": "010", "3": "011",
                  "4": "100", "5": "101", "6": "110", "7": "111"}

    for digit in number:
        binary_number += octal_digits[digit]

    return binary_number

def bin_oct(number) :
   octal_numberlist = [000 , 1 , 10 , 11 , 100 , 101 , 110 ,111]
   octal_number = []
   while int(number) > 0 :
       digit = int(number)%1000
       octal_number.append(octal_numberlist.index(digit))
       number = int(number)//1000
   octal_number.reverse()
   oct_num = "".join(map(str,octal_number))
   return oct_num

def hexa_to_binary(number) :
    binary_num=""
    hexal_digits={"0": "0000", "1": "0001", "2": "0010", "3": "0011",
                  "4": "0100", "5": "0101", "6": "0110", "7": "0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}

    for x in number :
       binary_num += hexal_digits[x]
    return binary_num

def bin_hex(number):
    hex_numberlist = [000, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111]
    hex_number = []
    while int(number) > 0:
        digit = int(number) % 10000
        y = hex_numberlist.index(digit)
        if y == 10:
            y = "A"
        if y == 11:
            y = "B"
        if y == 12:
            y = "C"
        if y == 13:
            y = "D"
        if y == 14:
            y = "E"
        if y == 15:
            y = "F"
        hex_number.append(y)
        number = int(number) // 10000
    hex_number.reverse()
    hex_number = "".join(map(str, hex_number))
    return hex_number

def bin_dec(number):
    dec_number = 0
    i = 0
    while int(number) > 0:
        digit = int(number) % 10
        dec_number = dec_number + digit * (pow(2, i))
        number = int(number) // 10
        i = i + 1
    return dec_number


def decimal_to_binary(number):
    binary_num = ""
    while int(number) > 0:
        binary_digit = int(number) % 2
        binary_num = str(binary_digit) + binary_num
        number = int(number) // 2
    return binary_num


def dec_to_hexa(number):
    hexa_digit = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A"
        , 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hex_number = ""
    while int(number) > 0:
        digit = int(number) % 16
        hex_number = hex_number + hexa_digit[digit]
        number = int(number) // 16
    hex_number = hex_number[::-1]
    return hex_number

def hex_to_decimal(hex_number):
  #Converts a hexadecimal number to its decimal equivalent.

  decimal_value = 0
  hex_to_decimal_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                       "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12,
                       "D": 13, "E": 14, "F": 15}

  power = len(hex_number) - 1  # Start with the highest power of 16
  for digit in hex_number:
    decimal_value += hex_to_decimal_map[digit] * (16 ** power)  # Multiply digit value by 16 raised to the power
    power -= 1  # Move to the next lower power of 16

  return decimal_value

#Second menu
def menu2() :
    print("A) Decimal")
    print("B) Binary")
    print("C) octal")
    print("D) hexadecimal")

#Third menu
def menu3():
    print("A) Decimal")
    print("B) Binary")
    print("C) octal")
    print("D) hexadecimal")

#First menu
def menu1():
       print("*numbering system converter*")
       print("A)insert a new number   B)Exit the program")
       choice1=input("please select A or B : ").upper()
       if choice1=="A" :
          number=input("please insert a number: ").upper()
          menu2()
          choice2=input("Please select the base you want to convert a number from :").upper()
          if choice2=="A" or "B" or "C" or "D" :
              menu3()
              choice3=input("Please select the base you want to convert a number to :").upper()
              if choice2=="A" and choice3=="B" :
                 binary_num = decimal_to_binary(number)
                 print("The binary equivalent is:", binary_num)
                 print("")
                 menu1()
              elif choice2=="A" and choice3=="C" :
                  octal_num = dec_to_oct(int(number))
                  print("the equivalent octal num is", octal_num)
                  print("")
                  menu1()
              elif choice2=="A" and choice3=="D" :
                  hex_number = dec_to_hexa(number)
                  print("the equivalent hexal num is", hex_number)
                  print("")
                  menu1()
              elif  choice2=="B" and choice3=="A"  :
                  dec_number = bin_dec(number)
                  print("the equivalent decimal num is", dec_number)
                  print("")
                  menu1()
              elif  choice2=="B" and choice3=="C" :
                  oct_num = bin_oct(number)
                  print("the equivalent octal num is", oct_num)
                  print("")
                  menu1()
              elif choice2=="B" and choice3=="D" :
                  hex_number = bin_hex(number)
                  print("the equivalent hex num is", hex_number)
                  print("")
                  menu1()
              elif choice2=="C" and choice3=="A" :
                  dec_num = oct_to_dec(int(number))
                  print("the equivalent decimal num is", dec_num)
                  print("")
                  menu1()
              elif choice2=="C" and choice3=="B" :        #must be reversed
                  binary_number = octal_to_binary(str(number))
                  print("The binary equivalent is:", binary_number)
                  print("")
                  menu1()
              elif  choice2=="C" and choice3=="D" :
                  hex_num = octal_to_hex(str(number))
                  print("the equivalent hex num is", hex_num)
                  print("")
                  menu1()
              elif choice2=="D" and choice3=="A" :
                  decimal_value = hex_to_decimal(str(number))
                  print("The decimal equivalent is:", decimal_value)
                  print("")
                  menu1()
              elif choice2=="D" and choice3=="B" :
                  binary_num = hexa_to_binary(str(number))
                  print("the equivalent binary num is", binary_num)
                  print("")
                  menu1()
              elif  choice2=="D" and choice3=="C" :
                  octal_num = hexa_to_octal(number)
                  print("the equivalent octal num is", octal_num)
                  print("")
                  menu1()

          else  :
            print("please select a valid choice ")
            print("")
            menu1()

       elif  choice1=="B" :
         exit()
       else:
         print("please select a valid choice : ")
         print("")
         menu1()

menu1()