def sumIntervals(diastimata):
    sum = 0
    euros = list()
    #Gia kathe ipolista brisko to diastima kai to apothikeuo mazi me tis times apo
    # ton deftero mexri ton teleutaio arithmo tou diastimatos autou se enan pinaka.
    #To plithos ton stoixeion einai to mikos kathe ipolistas
    for j in range(len(diastimata)):
        x = diastimata[j]
        diafora = x[1]-x[0]
        for i in range(diafora):
            euros.append(x[1]-i)
            #prosexo oste na dimiourgountai kainouria kelia stin lista
            # gia mporeso na apothikeuso oles tis times
        sum = sum + diafora
    #Afou exo ola ta stoixeia taksinomo tin lista kai apo ton plithos tous afairo osous arithmous einai isous
    euros.sort()
    telikosum = len(euros)
    for i in range(len(euros)-1):
        if (euros[i] == euros[i+1]):
            telikosum = telikosum -1
    print(telikosum)
    #etsi telika prokiptei to sunoliko athroisma ton diastimaton

sumIntervals([[1,5],[10,19],[1,7],[16,19],[5,11]])