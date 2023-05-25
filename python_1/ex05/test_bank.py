#!/usr/bin/python3

from the_bank import Account, Bank


if __name__ == "__main__":
    
    print("==================================== Banking Test 1 =============================================")
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        bref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation'
    ))

    if bank.transfer('William John', 'Smith Jane', 500.0) is False:
        print('Failed')
    else:
        print('Success')
    print("==================================== Banking Test 2 =============================================")
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')

        bank.fix_account('William John')
        bank.fix_account('Smith Jane')

    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')


    print("==================================== Banking Test 3 =============================================")
    bank = Bank()
    acc_valid_1 = Account('Sherlock Holmes',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=42.0)
    acc_valid_2 = Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=42.0,
                          info=None)

    acc_invalid_4 = Account("Douglass",
                            zip='42',
                            addr='boulevard bessieres',
                            value=42)
    acc_invalid_1 = Account("Adam",
                            value=42,
                            zip='0',
                            addr='Somewhere')
    acc_invalid_2 = Account("Bender Bending Rodríguez",
                            zip='1',
                            addr='Mexico',
                            value=42)
    acc_invalid_3 = Account("Charlotte",
                            zip='2',
                            addr='Somewhere in the Milky Way',
                            value=42)
    acc_invalid_5 = Account("Edouard",
                            zip='3',
                            addr='France',
                            value=42)


    #bank.add()
    cuentas = [acc_invalid_1, acc_invalid_2, acc_invalid_3, acc_invalid_4, acc_invalid_5, acc_valid_1, acc_valid_2]
    for cuenta in cuentas:
        bank.add(cuenta)

    import random
    for i in range(50):
        acc1 = random.randint(0,len(cuentas)-1)
        acc2 = random.randint(0,len(cuentas)-1)
        amount = random.randint(1,42)

        acc1_name = cuentas[acc1].name
        acc2_name = cuentas[acc2].name

        print("-"*40)
        print(f"a {amount} Transfer betweeen '{acc1_name}' and '{acc2_name}'")
        print(f"a {amount} Transfer betweeen '{cuentas[acc1].value}' and '{cuentas[acc2].value}'")
        print("-"*40)
        if bank.transfer(acc1_name, acc2_name, amount) is False:
            print('\tFailed....fixing....')
            bank.fix_account(acc1_name)
            bank.fix_account(acc2_name)
            #bank.fix_account('William John')
            #bank.fix_account('Smith Jane')
            print("\tsecond try")
            if bank.transfer(acc1_name, acc2_name, amount) is False:
                print('\tFailed')
            else:
                print('\tSuccess at 2nd try')
                print(f"a {amount} Transfer betweeen '{cuentas[acc1].value}' and '{cuentas[acc2].value}'")
        else:
            print('\tSuccess')
            print(f"a {amount} Transfer betweeen '{cuentas[acc1].value}' and '{cuentas[acc2].value}'")

    print("==================================== Banking Test evaluation =============================================")
    print("### # 01.05.01")
    bank = Bank()
    john = Account(
    'William John',
    zip='100-064',
    brother="heyhey",
    value=6460.0,
    ref='58ba2b9954cd278eda8a84147ca73c87',
    info=None,
    other='This is the vice president of the corporation',
    lol = "hihi"
    )
    bank.fix_account(john)
    # OR
    bank.fix_account('William John')


    print("### # 01.05.02")

    john = Account(
    'William John',
    zip='100-064',
    rother="heyhey",
    value=6460.0,
    ref='58ba2b9954cd278eda8a84147ca73c87',
    info=None,
    other='This is the vice president of the corporation',
    )


    print("### # 01.05.03")

    john = Account(
    'William John',
    zip='100-064',
    rother="heyhey",
    ref='58ba2b9954cd278eda8a84147ca73c87',
    info=None,
    other='This is the vice president of the corporation',
    lol = "lolilol"
    )


    print("### # 01.05.04")

    bank.add(
    Account(
    'Jane',
    zip='911-745',
    value=1000.0,
    ref='1044618427ff2782f0bbece0abd05f31'
    )
    )
    jhon = Account(
    'Jhon',
    zip='911-745',
    value=1000.0,
    ref='1044618427ff2782f0bbece0abd05f31'
    )
    bank.add(jhon)
    print("testing a valid transfer")
    print(jhon.value)
    bank.transfer("Jane", "Jhon", 500)
    print(jhon.value)


    print("### # 01.05.05")

    bank.transfer("Jane", "Jhon", 1000)
    print(jhon.value)