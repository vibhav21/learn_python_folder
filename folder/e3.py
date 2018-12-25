oceans=['artic','indian','atlantic','southern','artic']
with open("oceans.txt","w") as f:#opening file in write mode
    
    for ocean in oceans:
        print(ocean,file=f)#print oceans with next line
        f.write(ocean)# same as above
        