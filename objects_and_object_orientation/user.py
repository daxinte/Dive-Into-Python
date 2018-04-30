import datetime

class User:
    """ A member """

    def __init__(self, name, birthday):
        self.name = name 
        self.birthday = birthday
    

    #extract first and last name
        name_pieces = name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]


    def age(self):
        today = datetime.date(2000, 12, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dod = datetime.date(yyyy, mm, dd)
        age_in_days = (today -dod).days
        age_in_years = age_in_days/365
        return int(age_in_years)
            
            




user = User('Daniel', '12341212')
# print(user.name, user.birthday, user.first_name, user.last_name)
print(user.age())