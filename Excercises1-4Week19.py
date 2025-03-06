list1=['Apples','Oranges','Grapefruit']
list2=['Broccoli','Cabbage','Lettuce','Bell Peppers']
list3=[['Milk','Soda'],['Honey Bunches of Oats','Granola']]
list3.append(list1)
list3.append(list2)
list3[2].append('Grapes')
list4=['Sprite','Mountain Dew','Grapefruit Juice','Sparkling Water','Kombucha']
for item in list4:
    list3[0].append(item)
list5=[list3[2],list3[3]]
list3.pop(3)
list3.pop(2)
list6=[]
for item in list5:
    for word in item:
        list6.append(word)
list3.append(list6)
list7=list3[1]*3
list3.pop(1)
list3.append(list7)
list8=list3[0][0:6]
list3.pop(0)
list3.append(list8)
print(list3[0][0:2])
list3[0].remove('Oranges')
list3[0].remove('Grapefruit')
list3[0].append('Blueberries')
list3[0].append('Rasberries')
list3[2].remove('Mountain Dew')
for item in list3:
    for word in item:
        print(word)

