#!/usr/bin/python3

from the_bank import Account, Bank


if __name__ == "__main__":
    print("==>bank = Bank()")
    bank = Bank()
    print(bank)
    print("==>john = Account( 'William John', zip='100-064', brother='heyhey', value=6460.0, ref='58ba2b9954cd278eda8a84147ca73c87', info=None, other='This is the vice president of the corporation', lol = 'hihi')")
    john = Account( 'William John', zip='100-064', brother="heyhey", value=6460.0, ref='58ba2b9954cd278eda8a84147ca73c87', info=None, other='This is the vice president of the corporation', lol = "hihi")
    print(john)
    print("==>bank.add()")
    try:
        bank.add()
    except Exception as e:
        print(e)

    print("==>bank.add(john)")
    bank.add(john)
    print(bank.accounts)

    print("==>bank.fix_account('William John')")
    bank.fix_account('William John')

    print("==>bank.fix_account(john)")
    bank.fix_account(john)


    print("01.05.02")
    john1 = Account('William John',
                   zip='100-064',
                   rother="heyhey",
                   value=6460.0,
                   ref='58ba2b9954cd278eda8a84147ca73c87',
                   info=None,
                   other='This is the vice president of the corporation')
    bank.fix_account(john1)
    print("01.05.03")
    john2 = Account('William John',
                   zip='100-064',
                   rother="heyhey",
                   ref='58ba2b9954cd278eda8a84147ca73c87',
                   info=None,
                   other='This is the vice president of the corporation',
                   lol = "lolilol")
    bank.fix_account(john2)
    print("01.05.04")
    bank.add(Account('Jane',zip='911-745',value=1000.0,ref='1044618427ff2782f0bbece0abd05f31'))
    jhon = Account('Jhon',zip='911-745',value=1000.0,ref='1044618427ff2782f0bbece0abd05f31')
    bank.add(jhon)
    print("testing a valid transfer")
    print(jhon.value)
    bank.transfer("Jane", "Jhon", 500)
    print(jhon.value)
    print("01.05.05")