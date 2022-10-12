def table_multipication (M) :
    for i in range (1,11) :
        print(M,"*",i,"=",i*M)
while True :
    M = int (input ("Veuillez saisir un nombre : "))
    if M > 0 :
         break
table_multipication (M)