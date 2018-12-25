import datetime
class User:
    def __init__(self,full_name, birthday):
        self.name=full_name
        self.birthday=birthday 
        name_pieces=full_name.split(" ")
        self.first_name=name_pieces[0]
        self.last_name=name_pieces[1]
    def age(self):
        today=datetime.date(2001,7,20)
        yyyy=int(self.birthday[0:4])
        mm=int(self.birthday[4:6])
        dd=int(self.birthday[6:9])
        dob=datetime.date(yyyy,mm,dd)
        age_in_days=(today-dob).days
        age_in_yer=age_in_days/365
        return int(age_in_yer)
user=User("vibhav Chaturvedi", "19980720")
print(user.first_name,user.last_name)
print(user.birthday)
print(user.age())   