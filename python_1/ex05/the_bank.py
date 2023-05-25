#!/usr/bin/python3

import sys
sys.tracebacklimit = None


class Account(object):
    ID_COUNT = 1  # Class Atribut: counts number of accounts

    def __init__(self, name, **kwargs):
        # Update the instance internal dictionary
        # with dictionary got in argument
        self.__dict__.update(kwargs)

        # set the account number
        self.id = self.ID_COUNT
        # prepare the class for next accout creation
        Account.ID_COUNT += 1

        # set the account holder
        self.name = name

        # in case i was instantiated without value attribute
        # i self create such atribute and set it to zero
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

    def even_num_attributes(self):
        """ """
        # TODO: watch inside a dictionary's class
        return (len(self.__dict__) % 2 == 0)
    
    def set_odd_num_attributes(self):
        if (len(self.__dict__) % 2 == 0):
            setattr(self, 'odd_attr', None)

    def an_attri_start_w_b(self):
        """ check first letter of each attibute"""
        for k in self.__dict__.keys():
            if k[0].lower() == "b":
               return True
            
        return False
    
    def change_initial_bs(self):
        """
        For each sttribute starting by b
        kepp value
        remove attribte
        create new attribute wihtout b
        """
        # Transform into a list to avoid
        # RuntimeError: dictionary keys changed during iteration
        for k in list(self.__dict__.keys()):
            # when the first letter of the key is 'b'
            if k[0].lower() == "b":
                # rm key form dictionary
                # create key without first 'b'
                self.__dict__[k[1:]] = self.__dict__.pop(k)

    def no_attri_start_w_z_or_a(self):
        """ verifies attributes startin with zip or addr
            no_zip   or no_addr     Corrupted
            ======      =======     =========
            True        True        True
            True        False       True
            False       True        True
            False       False       False
        """
        no_zip = True
        no_addr = True

        for k in self.__dict__.keys():
            if k.lower().startswith("zip"):
                no_zip = False
                break
        for k in self.__dict__.keys():
            if k.lower().startswith("addr"):
                no_addr = False
                break
        return (no_zip or no_addr)

    def create_attr_z_or_a(self):
        if not hasattr(self, 'zip*'):
            setattr(self,'zip',"Empty zip")

        if not hasattr(self, 'addr*'):
            setattr(self,'addr', "Empty addr")

    def no_attr_n_i_v(self):
        """ Verifies existence of name, id and value
            no_name  or no_id  or no_value   Corrupted
            =======     =====     ========   =========
            True        True        True      True
            True        True        False     True
            True        False       True      True
            True        False       False     True
            False       True        True      True
            False       True        False     True
            False       False       True      True
            False       False       False     False
        """
        no_name = True
        no_id = True
        no_value = True

        for k in self.__dict__.keys():
            if k.lower() == "name":
                no_name = False
                break
        for k in self.__dict__.keys():
            if k.lower() == "id":
                no_id = False
                break
        for k in self.__dict__.keys():
            if k.lower() == "value":
                no_value = False
                break
        return (no_name or no_id or no_value)

    def no_attr_n_i_v(self):
        """ Verifies existence of name, id and value
            no_name  or no_id  or no_value   Corrupted
            =======     =====     ========   =========
            True        True        True      True
            True        True        False     True
            True        False       True      True
            True        False       False     True
            False       True        True      True
            False       True        False     True
            False       False       True      True
            False       False       False     False
        """
        checks = {"no_name": True, "no_id": True, "no_value": True}

        for k in self.__dict__.keys():
            if k.lower() == "name":
                checks["no_name"] = False
            if k.lower() == "id":
                checks["no_id"] = False
            if k.lower() == "addr":
                checks["no_value"] = False
        # when no value is true, means all are false, so corrupted is false
        return any(checks.values())

    def create_attr_n_i_v():
        if not hasattr(self, 'name*'):
            setattr(self,'name',"Empty Name")

        if not hasattr(self, 'id*'):
            setattr(self,'id', self.ID_COUNT)
            self.Account.ID_COUNT += 1
            

        if not hasattr(self, 'value*'):
            setattr(self,'value', 0)

    def name_no_str(self):
        if hasattr(self, "name"):
            # isinstance is false when name is not STR.So Corruptes is true
            return not isinstance(self.name, str)
        else:
            # Has not name, so name_no_str is true
            return True

    def set_name_str(self):
        if hasattr(self, "name"):
            try:
                setattr(self, 'name',str(getattr(self, 'name')))
            except Exception as e:
                print("set_name_str:", e)
  
    def id_not_int(self):
        if hasattr(self, "id"):
            # isinstance is false then  id  is not INT.So Corruptes is true
            return not isinstance(self.id, int)
        else:
            # Has not id, so id_not_int is true
            return True

    def set_id_int():
        if hasattr(self, "id"):
            # isinstance is false when name is not STR.So Corruptes is true
            try:
                setattr(self, 'id',int(getattr(self, 'id')))
            except Exception as e:
                print("set_id_int:", e)

    def value_not_int_or_float(self):
        if hasattr(self, "value"):
            # isinstance is false when id  is not INT.So Corruptes is true
            return not isinstance(self.id, (int | float))
        else:
            # Has not value, so value_not_int_or_float is true
            return True
    
    def set_value_float(self):
        if hasattr(self, "value"):
            try:
                setattr(self, 'value',float(getattr(self, 'id')))
            except Exception as e:
                print("set_value_float:", e)
    
    def __str__(self):
        txt = "Información de cuenta\n"
        txt = txt + "-"*30 + "\n"
        txt = txt + f"NAME: {self.name}\n"
        for k,v in self.__dict__.items():
            if k != "name":
                txt = txt + f"{k.upper()}: {v}\n"
        return txt


# in the_bank.py

class Bank(object):
    """The bank"""
    def __init__(self):
        self.accounts = []

    def add(self, new_account=None):
        """
        Add new_account in the Bank verification has to be performed when
        account objects are added to to Bank instance

        @new_account: Account() new account to append
        @return   True if success, False if an error occured


        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if new_account is None:
            # i got bank.add() wiht nothing to add
            msg = f"ADD:Account '{new_account}' ==> invalid class"
            raise ValueError(msg)
        else:
            # check for the right objec  
            if isinstance(new_account, Account):
                # check for an exixting account
                if self.__account_in_bank(new_account.name):
                    msg = f"Bank already has An account for '{new_account.name}'"
                    raise ValueError(msg)
                else:
                    # the account is not in the bank, so i add it
                    self.accounts.append(new_account)
                    print(f"Count for '{new_account.name}' added")

            else:
                msg = f"ADD: {new_account} is an {type(new_account)} \
                        instead of an account"
                raise ValueError(msg)

    def transfer(self, acc_name_orig, acc_name_dest, amount):
        """" Perform the fund transfer
        @origin:  str(name) of the first account
        @dest:    str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return   True if success, False if an error occured
        """
        try:
            # arguments revision
            if acc_name_orig is None or not isinstance(acc_name_orig, str):
                msg = f"{acc_name_orig} not a good origin account name"
                raise ValueError(msg)
            
            if acc_name_dest is None or not isinstance(acc_name_dest, str):
                msg = f"{acc_name_dest} not a good destination  account name"
                raise ValueError(msg)
            
            # positive amount verification

            if amount is None or not isinstance(amount, (int | float)) or amount < 0:
                msg = f"Incorrect amount '{amount}' for a transfer"
                raise ValueError(msg)
            
            # Does have Bank customers acc_name_orig and acc_name_dest?
            acc_orig = self.__acc_record_of(acc_name_orig)
            acc_dest = self.__acc_record_of(acc_name_dest)

            if acc_orig is None:
                # Bank does not have acc_name_orig
                msg = f"'{acc_name_orig}' not a bank's customer"
                raise ValueError(msg)
            
            if acc_dest is None:
                # Bank does not have acc_name_dest
                msg = f"'{acc_name_dest}' not a bank's customer"
                raise ValueError(msg)
            
            # Transfert's accounts are corrupted?
            acc_orig_corrup = self.__corrupted_account(acc_orig)
            acc_dest_corrup = self.__corrupted_account(acc_dest) 

            # accounts validity
            if acc_orig_corrup or acc_dest_corrup:
                if acc_orig_corrup:
                    # Transfert's origin account is corrupted 
                    msg = f"'{acc_orig.name}' account corrupted"
                    raise ValueError(msg)
                if acc_dest_corrup:
                    # Transfert's dest account is corrupted
                    msg = f"'{acc_dest.name}' account corrupted"
                    raise ValueError(msg)             
            else:  # I have two non corrupte Bank Accounts

                # verification of Enough funds at origin

                if amount > acc_orig.value:
                    msg = f"'{acc_orig.name} has less than '{amount}'"
                    raise ValueError(msg)

                if acc_name_orig == acc_name_dest:
                    print(f"Transfert between same accout {acc_name_dest}")
                    return True
                else:
                    # this is the case of a regular transfer.
                    acc_orig.transfer(- amount)
                    acc_dest.transfer(+ amount)
                    print(f"'{acc_orig.name}' transfered {amount} to '{acc_dest.name}'")
                    return True       
        except ValueError as msg:
            print("TRANSFERT:",msg)
            return False

    def fix_account(self, acc_name):
        """ fix account associated to name if corrupted
        @name:   str(name) of the account or Account Object
        @return  True if success, False if an error occured
        """
        try:
            if isinstance(acc_name, str):
                acc = self.__acc_record_of(acc_name)
                if acc is None:
                    # Bank does not have acc_name_orig
                    msg = f"'{acc_name}' not a bank's customer"
                    raise ValueError(msg)
            elif isinstance(acc_name, Account):
                if self.__account_in_bank(acc_name.name):
                    acc = acc_name
                else:
                    msg =f"'{acc_name.name}' not a bank's customer"
                    raise ValueError(msg)

        # TODO:
            msg = ""
            if acc.even_num_attributes():
                acc.set_odd_num_attributes()
                msg = msg + "even_num_attributes, "
            if acc.an_attri_start_w_b():
                acc.change_initial_bs()
                msg = msg + "an_attri_start_w_b, "
            if acc.no_attri_start_w_z_or_a():
                acc.create_attr_z_or_a()
                msg = msg + "o_attri_start_w_z_or_a, "
            if acc.no_attr_n_i_v():
                acc.create_attr_n_i_v()
                msg = msg + "no_attr_n_i_v, "
            if acc.name_no_str():
                acc.set_name_str()
                msg = msg + "name_no_str, "
            if acc.id_not_int(): 
                acc.set_id_int()
                msg = msg + "id_not_int, "
            if acc.value_not_int_or_float():
                acc.set_value_float()
                msg = msg + "value_not_int_or_float, "

            
            # check if something was repaired
            if msg == "":
                # as  notingh was repaired
                msg = f"{acc.name} was OK. NOTHING FIXED"

            print("FIX_ACCOUNT fixed: ", msg)   
            return True
        except ValueError as msg:
            print("FIX_ACCOUNT: ", msg)
            return False

    def __corrupted_account(self, acc):
        """
        Check if any of corropted account condition exist
        RETURN
            True if the account is not corrupted
            False Otherwise
        """
        # i check if acc's record is corrupted
        """
        if acc.even_num_attributes() or \
                acc.an_attri_start_w_b() or \
                acc.no_attri_start_w_z_or_a() or \
                acc.no_attr_n_i_v() or \
                acc.name_no_str() or \
                acc.id_not_int() or \
                acc.value_not_int_or_float():
            return True
        else:
            return False
        """
        try:
            msg = ""
            if acc.even_num_attributes(): msg = msg + "even_num_attributes, "
            if acc.an_attri_start_w_b(): msg = msg + "an_attri_start_w_b, "
            if acc.no_attri_start_w_z_or_a(): msg = msg + "no_attri_start_w_z_or_a, "
            if acc.no_attr_n_i_v(): msg = msg + "no_attr_n_i_v, "
            if acc.name_no_str(): msg = msg + "name_no_str, "
            if acc.id_not_int(): msg = msg + "id_not_int, "
            if acc.value_not_int_or_float(): msg = msg + "value_not_int_or_float"
            if msg != "":
                msg = f"'{acc.name}' has this problems: " + msg
                raise ValueError(msg)
            else:
                return False
        except ValueError as msg:
            print(msg)
            return True
    
    def __account_in_bank(self, customer_name):
        """
        checking if account's name already exist in the bank
        Looks for acc.name inside the Bank's list of accounts
        """
        acc_exist = False
        for a in self.accounts:
            if customer_name == a.name:
                acc_exist = True
                break
        return acc_exist
    
    def __acc_record_of(self, customer_name):
        """ 
        Returns the account record of 
        an EXISTING Customer

        Return None when Customer_name does not exit
        """

        for a in self.accounts:
            if customer_name == a.name:
                return a
            
        return None      


