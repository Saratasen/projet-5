import sqlite3
#creation de la basse de donnée nommé myDB.db
connexion = sqlite3. connect('myDB.db')
# creation de la variable nommé cur
cur = connexion. cursor()
#CREATION DE LA TABLE  NOMME DEPENSES_perso
hab=int(input(' veiller donnée la depenses habillement'))
trpor =int(input('veiller donnée la depenses de trasport'))
loyer =int(input('veiller donnée la depenses de loyer'))
manger = int(input('veiller donnée la depenses de manger'))
loisir = int(input('veiller donnée la depenses de loisir'))
#INSERET DANS LA TABLE DEPENSES LES ATRIBUTS
req="CREATE TABLE depense_perso(id integer primary key, habillement numeric, transport numeric, loyer numeric, manger numeric, loisir numeric)"
req = "insert into depense_perso(habillement,transport,loyer,manger,loisir) values(?,?,?,?,?) "
cur.execute(req,(hab,trpor,loyer,manger,loisir))
total_depense= hab+trpor+loyer+manger+loisir 
print("la depense total est:"+str(total_depense)+"fca") 
connexion.commit()

#CREATION DE LA TABLE REVENUS ET CES ATRIBUTS
salaire=int(input('veiller donnée la revenus salaire'))
business=int(input('veiller donnée la revenus business'))
profit=int(input('veiller donnée la revuneus de profit'))
#INSERET DANS LA TABLE REVENUS LES ATRIBUT
req="CREATE TABLE revenus_perso(id integer primary key, salaire numeric, business numeric, profit numeric)"
req = "insert into revenus_perso(salaire,business,profit) values (?,?,?)"
cur.execute(req,(salaire,business,profit)) 
total_revenus= salaire+business+profit
print("la depense total est:"+str(total_revenus)+"fca")
connexion.commit()


if  total_depense < total_revenus:
    ecart=total_revenus-total_depense
    print("l'ecart entre les depense et les revenus est :"+str(ecart)+"fca")
elif total_revenus < total_depense:
    ecart=total_depense-total_revenus
    print("l'ecart entre les depense et les revenus est:"+str(ecart)+"fca")
else:
    print("il ny a pas d'ecart entre les depense et les revenus")

connexion.commit()

connexion.close()