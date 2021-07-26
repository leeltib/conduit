# A009 - userek megadása lapozó funkció teszteléséhez
# random generált userek (alapból 12 db, de ez állítható)

import random
import string

title = 'Átmeneti User vagyok a lapozó funkció tesztjéhez.'

class MyRND():
    chars_lo = string.ascii_lowercase
    chars_int = string.digits
    chars_up = string.ascii_uppercase
    chars = string.punctuation               # *'[{&| stb

    @classmethod
    def uname(cls):
        return "".join([random.choice(cls.chars_lo) for _ in range(8)])

    @classmethod
    def ppass(cls):
        pp_lo = "".join([random.choice(cls.chars_lo) for _ in range(8)])
        pp_int = "".join([random.choice(cls.chars_int) for _ in range(8)])
        pp_up = "".join([random.choice(cls.chars_up) for _ in range(8)])
        pchars = pp_lo[4] + pp_int[0] + pp_up[7] + pp_lo[1:3] + pp_int[3] + pp_up[4] + pp_lo[6]
        return pchars

    @classmethod
    def email(cls):
        mail_lo = "".join([random.choice(cls.chars_lo) for _ in range(7)])
        mail_fix = "@gmail.com"
        email = mail_lo + mail_fix
        return email


class TestData:
    def __init__(self, rn):
        self.data = []
        for i in range(rn):
            d = {}
            d["username"] = MyRND.uname()
            d["email"] = MyRND.email()
            d["password"] = MyRND.ppass()
            self.data.append(d)

# itt állítható a random generált userek száma
td = TestData(12)
td_list = td.data
print(td_list)

users = []
for user in td_list:
    user_data = []
    for value in user.values():
        user_data.append(value)
    users.append(user_data)

print(users)


