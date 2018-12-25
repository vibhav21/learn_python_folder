oceans=['artic','indian','atlantic','southern','artic']
with open("oceans.txt","a") as f:#opening file in write mode
    print(23*'=',file=f) #print oceans with next line
    f.write("there are five oceans" )# same as above