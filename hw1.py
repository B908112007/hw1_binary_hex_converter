import sys
user_input=input("若要結束請輸入‘exit'")
while user_input.lower()!='exit':
    decimal_number=int(input("請輸入一個數字介於０到255之間"))
    if decimal_number >255 or decimal_number <0:
        print("輸入錯誤")
        user_input=input("若要結束請輸入'exit'")

    elif 0<= decimal_number<=255:
        binary_string = bin(decimal_number)[2:]
        print("二進位結果:", binary_string)
        binary_number = int(binary_string, 2)
        hex_number = hex(binary_number)
        print("十六進位結果:", hex_number)
        user_input = input("若要結束請輸入 'exit'")
print("結束了!")
