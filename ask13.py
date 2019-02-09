#bazo apo mia bibliothiki mia ekntoli pou me boithaei na paro ola ta uposonola enos sunolou
from  itertools import combinations
#i combos einai synartisi pou kaleitai mesa stin maxDistance kai xrisimopoieitai gia na ftiakso ola ta
#yposunola ton apostaseon se mia lista.Gia auto xreiazetai i grammi 1
def combos(lst, length):
    for combo in combinations((e for e in lst ), length):
        yield list(combo)
#h kentriki sinartisi tou programmatos
def maxDistance(apostaseis,megisto):
    megisto = int(megisto)
    newlist = []
    #tora kalo tin eksoteriki sinartisi gia na dimiourgiso ola ta ditana iposinola se nea lista me epanalipsi
    for i in range (len(apostaseis)):
        for sublist in combos(apostaseis, i+1):
            newlist.append(sublist)
    #epeita allazo ta iposinola ton apostaseon me to athroisma tous stin idia lista
    x = [0] * len(newlist)
    for i in range(len(newlist)):
        x[i] = sum(newlist[i])
    #taksinomo tin lista kai brisko to megalitero athroisma.an ksepernaei to
    #megisto tou xristi tote to kano arnitiko kai ksanataksinomo tin lista
    #epanalambano mexri to megalitero na ginei apodekto.an den ginei tote dino timi 0
    x.sort()
    for i in range(len(x)):
        if max(x) > megisto:
            y = x[-1]
            y = y * (-1)
            x[-1] = y
            x.sort()
    if max(x) > 0:
        print("Max distance you can have is", max(x))
    else:
        print("Your limit is too low so maximum distance is 0")

maxDistance([1,2,3,4,5],19)