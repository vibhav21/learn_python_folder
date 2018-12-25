import pdb
class Student:#Student Classmarks
    perc_rise = 1.05
    
    def __init__(self,first,last,marks):#constructor
        self.first=first
        self.last=last
        self.marks=marks
        self.email= first+"."+last+"@school.com"
    def fullname(self):#every method describe in class must have self argument
         return '{} {}'.format(self.first,self.last)#format function
    def apply_raise(self):
        self.marks=int(self.marks *self.perc_rise)
        

class dumb(Student):#inheriting the Student class
    perc_rise=1.10
    pass

Std_2 = dumb('neel','nitin',int (input()))#convert string into int then pass it 
#pdb.set_trace()
print(Std_2.marks)#befor perc_rise
#print(Std_2.fullname())
Std_2.apply_raise() #method calling
print(Std_2.marks)#after perc_rise
#print(Std_2.__dict__)#doesnot print perc_rise
#print(Student.__dict__)#print perc_rise
#print(help(dumb)) #to get to know about method resolution order
std_3 = Student('raju','ban',int(input()))
print(std_3.fullname())
print(Std_2.fullname())

print(Std_2.last)
print(Std_2.email)
a="aman"
b="rastogi"
c=70
Std_4=dumb(a,b,c,)
print(Std_4.marks)
Std_4.apply_raise()

print(Std_4.marks) 
