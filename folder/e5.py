import datetime #to deal with date time
class User:
    def __init__(self,full_name, birthday): #constructor
        self.name=full_name # class variables name and birthdy
        self.birthday=birthday #yyyymmdd
        name_pieces=full_name.split(" ")#split function will split the string in full name in parts which are divided by spces and store them in list  
        self.first_name=name_pieces[0] # assigning list first element to class variable first_name
        self.last_name=name_pieces[1]
    def age(self): #simple method
        today=datetime.date(2001,7,20)#assigning todays date to today
        yyyy=int(self.birthday[0:4])#assigning stsrtin 4 letters of birthday string to yyyy because strings are immutable
        mm=int(self.birthday[4:6])
        dd=int(self.birthday[6:9])
        dob=datetime.date(yyyy,mm,dd)# assigning date of birth to dob
        age_in_days=(today-dob).days #difference between dob and today gives the difference in days *don't forget to use .days*
        age_in_yer=age_in_days/365
        return int(age_in_yer)
user=User("vibhav Chaturvedi", "19960520")# user instance of User class
print(user.first_name,user.last_name)
print(user.birthday)
print(user.age(),end=" ")
print("years")  