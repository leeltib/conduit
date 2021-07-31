# A010 - Validating registration form fields
"""
Test cases:
Username:
 - empty field -> error message expected
 - existing user -> error message expected

Email:
 - empty field -> error message expected
 - existing email address -> error message expected
 - missing '@' character -> error message expected
 - missing '.' character -> error message expected

Password:
 - empty field -> error message expected
 - existing password -> error message expected
 - less than 8 characters -> error message expected
 - no numbers -> error message expected
 - no lower case letters -> error message expected
 - no upper case letters -> error message expected
"""

comment_ok = """
A további tesztekhez szükséges "meglévő" user adatok feltöltése OK.//
Username. Üres mezős teszt OK!//
Username. Meglévő felhasználónév teszt OK!//
Email. Üres mezős teszt OK!//
Email. Meglévő email cím teszt OK!//
Email. Hiányzó '@' karakter teszt OK!//
Email. Hiányzó '.' karakter teszt OK!//
Password. Üres mezős teszt OK!//
Password. Meglévő jelszó teszt OK!//
Password. 8 karakternél kevesebb teszt OK!//
Password. A nincs benne szám teszt OK!//
Password. A nincs benne kisbetű teszt OK!//
Password. A nincs benne nagybetű teszt OK!//
"""

comment_error = """
Hiba történt a további tesztekhez szükséges "meglévő" user adatok feltöltése közben!//
Username. ERROR! Nincs hibaüzenet az üres mezős tesztnél!//
Username. ERROR! Nincs hibaüzenet a meglévő felhasználóneves tesztnél!//
Email. ERROR! Nincs hibaüzenet az üres mezős tesztnél!//
Email. ERROR! Nincs hibaüzenet a meglévő email cím tesztnél!//
Email. ERROR! Nincs hibaüzenet a hiányzó '@' karakter tesztnél!//
Email. ERROR! Nincs hibaüzenet a hiányzó '.' karakter tesztnél!//
Password. ERROR! Nincs hibaüzenet az üres mezős tesztnél!//
Password. ERROR! Nincs hibaüzenet a meglévő jelszó tesztnél!//
Password. ERROR! Nincs hibaüzenet a 8 karakternél kevesebb tesztnél!//
Password. ERROR! Nincs hibaüzenet a nincs benne szám tesztnél!//
Password. ERROR! Nincs hibaüzenet a nincs benne kisbetű tesztnél!//
Password. ERROR! Nincs hibaüzenet a nincs benne nagybetű tesztnél!//
"""

# Randomly generated users

import random
import string


class MyRND():
    chars_lo = string.ascii_lowercase
    chars_int = string.digits
    chars_up = string.ascii_uppercase
    chars = string.punctuation               # *'[{&| stb

    @classmethod
    def uname(cls, i):
        if i == 0:          # empty field -> error message expected
            return ""
        elif i == 1:        # existing user -> error message expected
            return user_bas[0]
        elif i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9 or i == 10 or i == 11:
            return "".join([random.choice(cls.chars_lo) for _ in range(8)])
        else:
            return "".join([random.choice(cls.chars_lo) for _ in range(8)])

    @classmethod
    def email(cls, i):
        if i == 0 or i == 1 or i == 6 or i == 7 or i == 8 or i == 9 or i == 10 or i == 11:
            mail_lo = "".join([random.choice(cls.chars_lo) for _ in range(7)])
            mail_fix = "@gmail.com"
            email = mail_lo + mail_fix
            return email
        elif i == 2:  # empty field -> error message expected
            email = ""
            return email
        elif i == 3:  # existing email address -> error message expected
            email = user_bas[1]
            return email
        elif i == 4:  # missing '@' character -> error message expected
            mail_lo = "".join([random.choice(cls.chars_lo) for _ in range(7)])
            mail_fix = ".gmail.com"
            email = mail_lo + mail_fix
            return email
        elif i == 5:  # missing '.' character -> error message expected
            mail_lo = "".join([random.choice(cls.chars_lo) for _ in range(7)])
            mail_fix = "@gmailcom"
            email = mail_lo + mail_fix
            return email
        else:
            mail_lo = "".join([random.choice(cls.chars_lo) for _ in range(7)])
            mail_fix = "@gmail.com"
            email = mail_lo + mail_fix
            return email

    @classmethod
    def ppass(cls, i):
        pp_lo = "".join([random.choice(cls.chars_lo) for _ in range(8)])
        pp_int = "".join([random.choice(cls.chars_int) for _ in range(8)])
        pp_up = "".join([random.choice(cls.chars_up) for _ in range(8)])
        if i == 0 or i == 1 or i == 2 or i == 3 or i == 4 or i == 5:
            pchars = pp_lo[4] + pp_int[0] + pp_up[7] + pp_lo[1:3] + pp_int[3] + pp_up[4] + pp_lo[6]
            return pchars
        elif i == 6:         # empty field -> error message expected
            pchars = ""
            return pchars
        elif i == 7:         # existing password -> error message expected
            pchars = user_bas[2]
            return pchars
        elif i == 8:         # less than 8 characters -> error message expected
            pchars = pp_lo[4] + pp_int[0] + pp_up[7] + pp_lo[1] + pp_int[3] + pp_up[4] + pp_lo[6]
            return pchars
        elif i == 9:         # no numbers -> error message expected
            pchars = pp_lo[4:6] + pp_up[7] + pp_lo[1:3] + pp_up[4:6] + pp_lo[6]
            return pchars
        elif i == 10:         # no lower case letters -> error message expected
            pchars = pp_int[0:2] + pp_up[4:6] + pp_int[3:5] + pp_up[4:6]
            return pchars
        elif i == 11:        # no upper case letters -> error message expected
            pchars = pp_lo[4] + pp_int[0:2] + pp_lo[1:3] + pp_int[3] + pp_lo[4:6]
            return pchars
        else:
            pchars = pp_lo[4] + pp_int[0] + pp_up[7] + pp_lo[1:3] + pp_int[3] + pp_up[4] + pp_lo[6]
            return pchars


class TestData:
    def __init__(self, rn):
        self.data = []
        for i in range(rn):
            d = {}
            d["username"] = MyRND.uname(i)
            d["email"] = MyRND.email(i)
            d["password"] = MyRND.ppass(i)
            self.data.append(d)

class TestData2:
    def __init__(self, rn):
        self.data = []
        for i in range(rn):
            d = {}
            d["username"] = MyRND.uname(100)
            d["email"] = MyRND.email(100)
            d["password"] = MyRND.ppass(100)
            self.data.append(d)

# creating already existing user
us = TestData2(1)
us_ba = us.data

user_bas = []
for data in us_ba:
    for value in data.values():
        user_bas.append(value)

# set number of randomly generated users
td = TestData(12)
td_list = td.data
print(td_list)


users = []
users.append(user_bas)
for user in td_list:
    user_data = []
    for value in user.values():
        user_data.append(value)
    users.append(user_data)

print(users)

