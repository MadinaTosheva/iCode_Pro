## Get the deepest lists from listC

listC = [[ [9,11], 10], [5, 4], [6, 7, 9, [3, 5, 7]]]

for i in listC:
    for j in i:
        if type(j) == type(listC):
           for k in j:
               print(k)