import getpass
import string
import os

users = ['user1', 'user2', 'user3']

pins = ['1112', '1113', '1114']

amount = [1000, 2000, 3000]

count = 0

# while loop check existance of the enter username

while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# Comparing pin
while count < 3:
    print('----------------')
    print('****************')
    pin = input('PLEASE ENTER THE PIN: ')
    print('****************')
    print('----------------')
    if pin.isdigit():
        if user == users[0]:
            if pin == pins[0]:
                break
            else:
                count += 1
                print('-----------')
                print('***********')
                print('INVALID PIN')
                print('***********')
                print('-----------')
                print()
                print('-----------')
        if user == users[1]:
            if pin == pins[1]:
                break
            else:
                count += 1
                print('-----------')
                print('***********')
                print('INVALID PIN')
                print('***********')
                print('-----------')
                print()
        if user == users[2]:
            if pin == pins[2]:
                break
            else:
                count += 1
                print('-----------')
                print('***********')
                print('INVALID PIN')
                print('***********')
                print('-----------')
                print()
    else:
        print('---------------------')
        print('*********************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('*********************')
        print('---------------------')
        count += 1
# in case of a valid pin continuing, or exiting
if count == 3:
    print('-----------------------------------')
    print('***********************************')
    print('3 UNSUCCESSFUL PIN ATTEMPTS EXITING')
    print('!!!!! YOUR CARD HAS BEEN LOCKED!!!!')
    print('***********************************')
    print('-----------------------------------')
    exit()

    
print('--------------------------')
print('**************************')
print('LOGIN SUCCESSFUL, CONTINUE')
print('**************************')
print('--------------------------')
print()
print('---------------------------------------')
print('***************************************')
print(str.capitalize(users[n]+' welcome to ATM'))
print('***************************************')
print('---------------ATM SYSTEM--------------')

# Main Menu
while True:
    # os.system('clear')
    print('----------------------------------')
    print('**********************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S) \nWithdraw__(W) \nDiposit__(D) \nChange__(P)  \nQuit__(Q) \n: ').lower()
    print('**********************************')
    print('----------------------------------')
    valid_responses = ['S', 'w', 'd', 'p', 'q']
    response = response.lower()
    if response == 's':
        print('------------------------------')
        print('******************************')
        print(str.capitalize(users[n]), 'YOU HAVE', amount[n], 'INR ON YOUR ACCOUNT.')
        print('******************************')
        print('------------------------------')
    elif response == 'w':
        print('------------------------------')
        print('******************************')
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        print('******************************')
        print('------------------------------')
        if cash_out % 100 != 0:
            print('------------------------------')
            print('******************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 100 INR NOTES')
            print('******************************')
            print('------------------------------')
        elif cash_out > amount[n]:
            print('----------------------------')
            print('****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('****************************')
            print('----------------------------')
        else:
            amount[n] = amount[n]-cash_out
            print('----------------------------')
            print('****************************')
            print('YOU NEW BALANCE IS', amount[n], 'INR')
            print('****************************')
            print('----------------------------')
    elif response == 'd':
        print()
        print('---------------------------------------------')
        print('**********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO Diposite: '))
        print('**********************************************')
        print('---------------------------------------------')
        if cash_in%100 !=0:
            print('---------------------------------------------')
            print('**********************************************')
            print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 100 INR NOTES')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amount[n] = amount[n]+cash_in
            print('----------------------------')
            print('****************************')
            print('YOU NEW BALANCE IS', amount[n], 'INR')
            print('****************************')
            print('----------------------------')

    elif response == 'p':
        print('----------------------------')
        print('****************************')
        new_pin = input('ENTER A NEW PIN: ')
        print('****************************')
        print('----------------------------')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('----------------------------')
            print('****************************')
            new_cpin = input('CONFIRM NEW PIN: ')
            print('****************************')
            print('----------------------------')
            if new_cpin != new_pin:
                print('------------------')
                print('******************')
                print('PIN MISMATCH')
            else:
                pins[n] = new_pin
                print("NEW PIN SAVED")

        else:
            print('------------------------------------------------------------------------')
            print('************************************************************************')
            print('NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
            print('************************************************************************')
            print('------------------------------------------------------------------------')
    elif response == 'q':
        exit()
    else:
        print('----------------------------')
        print('****************************')
        print('    RESPONSE NOT VALID      ')
        print('****************************')
        print('----------------------------')
