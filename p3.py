M1 = float (input("Veuillez saisir M1 : "))
M2 = float (input("Veuillez saisir M2 : "))
M3 = float (input("Veuillez saisir M3 : "))
Moyenne = (M1+M2+M3)/3
print ("La moyenne de L'étudiant est : ",format (Moyenne, " .2f"))
if Moyenne < 10:
     print ("La mention de L'étudiant est : Insuffisant")
elif Moyenne >=10 and Moyenne < 12 :
     print ("La mention de L'étudiant est : Passable")
elif Moyenne >=12 and Moyenne < 14 :
     print ("La mention de L'étudiant est : Assez bien")
elif Moyenne >=14 and Moyenne < 16 :
      print ("La mention de Létudiant est : Bien")
else:
      print("La mention de l'étudiant est : Tres bien")