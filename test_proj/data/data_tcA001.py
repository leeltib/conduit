# Data for new user registration
# Arbitrary number of users can be defined
# Only users in the list will be used as test data

us1 = ['testuser01', 'tuser01@gmail.com', 'TestUser01']
us2 = ['testuser02', 'tuser02@gmail.com', 'TestUser02']
us3 = ['testuser03', 'tuser03@gmail.com', 'TestUser03']
us4 = ['testuser04', 'tuser04@gmail.com', 'TestUser04']
us5 = ['testuser05', 'tuser05@gmail.com', 'TestUser05']
us6 = ['testuser06', 'tuser06@gmail.com', 'TestUser06']
us7 = ['testuser07', 'tuser07@gmail.com', 'TestUser07']
us8 = ['testuser08', 'tuser08@gmail.com', 'TestUser08']
us9 = ['testuser09', 'tuser09@gmail.com', 'TestUser09']
us10 = ['testuser10', 'tuser10@gmail.com', 'TestUser10']

# Generate random user
us_random = False

users_orig = [us1, us2, us3]


import random
import string

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

# print(MyRND.uname())
# print(MyRND.ppass())
# print(MyRND.email())

# Randomly generated data can be stored in an other class (eg. for later login)

class TestData:
    def __init__(self, rn):
        self.data = []
        for i in range(rn):
            d = {}
            d["username"] = MyRND.uname()
            d["email"] = MyRND.email()
            d["password"] = MyRND.ppass()
            self.data.append(d)

td = TestData(2)
td_list = td.data
print(td_list)

users_random = []
for user in td_list:
    user_data = []
    for value in user.values():
        user_data.append(value)
    users_random.append(user_data)

#print(users_random)

# Switch between random and original user data
if us_random == True:
    users = users_random
else:
    users = users_orig

