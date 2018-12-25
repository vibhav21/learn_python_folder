import pdb #python debugger
def transform(x,y):
    y=y**2
    x=x*2
    z=x+y
    return z

x=50
y=60
z=5
n=1000
#python debugger.set trace 
pdb.set_trace() #it will print 3 line above and below it
transform(5,10)
print('z='+str(z))
n=transform(2,3)
print('n='+str(n))
  # n next line
  # c complete execution#
  # l list 3 line below and above
  # s step into func call
  #b and b num specify break point
  #cl cl num clear breakpoint