
#dictionary

Cousin = {'Violet':"20" , 'Sheila':"12" ,'Vicky':"21" ,'Jonah': "30"}

#mapping a dictionary

print(list(Cousin.keys()))
print(list(Cousin.values()))

#update
Cousin.update({'Violet': 'Sheila'})

#iteration
for z in Cousin:
    print(  Cousin[z])
