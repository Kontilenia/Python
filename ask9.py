def maxSequence(lista):
    sum = list()
    sublista=list()
    #ftiaxno dio listes mia pou tha apothikeuo to athroisma kai mia tous arithmous pou pira gia
    #to athroisma os string se antistoixes theseis
    for i in range(len(lista)):
        y=0
        u = ""
        # to y mou dinei kathe fora to athroisma ton stoixeion
        for j in range (len(lista)-i):
            y=y+lista[j+i]
            sum.append(y)
            #bazo telia anamesa kai ta kano string gia na mporo meta na ta ksanaxoriso
            u = u +str(lista[j+i])+ ","
            sublista.append(u)
    #brisko tin thesi tou megistou stin lista me ta athroismata kai tin
    #efarmozo stin sublista pou stin antistoixi thesei exei tous aritmous pou prostethikan.
    #xorizo ta psifia basi tis teleias,ta apothikeuo se pinaka  kai angoontas to teleutaio
    #psifio pou tha einai keno kano ta upoloipa ksana aneraia
    end=sublista[sum.index(max(sum))].split(",")
    for k in range(len(end)-1):
        end[k]=int(end[k])
        #end[k]=float(end[k])
    print(max(sum),":",end[0:-1])
    #ektipono to mesisto athroisma kai ta stoixeia pou prosthesa gia na prokeipsei auto.


#i askisi leitourgei me akeraious alla mporei na leitourgisei kai me pragmatikous an
#antoikatastiso tin grammi 22 me tin grammi 23 pou einai sxolio
maxSequence([-2,1,-3,4,-1,4,1,-5])