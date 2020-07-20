from random import *
def addtuple(t1,t2):
    return(t1[0]+t2[0],t1[1]+t2[1])

def solrec(t):
    if len(t)==0 :
        #print(somme,chemin)
        #i=eval('0b'+chemin)
        #if somme!=testcoup(12,i): print ('erreur')
        return (0,'')
    if len(t)==1: return (somme+t[0], 'd'+chemin)
    maxi=[]
    for i in range (-1,1):
        tsav=t[:]
        sommetemp=tsav.pop(i)
        if tsav[0]>tsav[-1]:sommetemp=sommetemp-tsav.pop(0)
        else :sommetemp=sommetemp-tsav.pop(-1)
        maxi.append(addtuple(solrec(tsav),(sommetemp,str(-i))))
    return max(maxi[0],maxi[1])


def solbotup(t):
    if len(t)%2==0:listedep=[(0,'') for i in range(len(t)+1)]
    else:listedep=[(t[i],'') for i in range(len(t))]
    

    for long in range (1+len(t)%2,len(t),2):            # longueur des intervalles à la base de l'arbre, on commence à 2 si la taille est paire, à 1 sinon puis on augmente de 2 en 2
        listecons=[]
        for i in range(len(t)-long):
            if t[i+1]>t[i+long]:
                cas1=(t[i]+listedep[i+2][0]-t[i+1],'g'+listedep[i+2][1])
            else :
                cas1=t[i]+listedep[i+1][0]-t[i+long],'g'+listedep[i+1][1]
            if t[i]>t[i+long-1]:
                cas2=t[i+long]+listedep[i+1][0]-t[i],'d'+listedep[i+1][1]
            else :
                cas2=t[i+long]+listedep[i][0]-t[i+long-1],'d'+listedep[i][1]
            listecons.append(max(cas1,cas2))
        #print(listecons)
        listedep=listecons[:]
    return(listedep)
            
t=[14, 7, 13, 7, 1, 5, 9, 8, 7, 13]       
                
def solit(t):
    scormax=-10000
    coupmax=0
    for i in range (2**(len(t)//2)):
        tsav=list(t)
        scorj=[0,0]
        joueur=0
        j=1
        for k in range (len(t)):
            if joueur%2==0:
                if j&i==0 : scorj[joueur%2]+=tsav.pop(0)
                else : scorj[joueur%2]+=tsav.pop(-1)
                j=j*2
            if joueur%2==1:
                if tsav[0]>tsav[-1]: scorj[joueur%2]+=tsav.pop(0)
                else:scorj[joueur%2]+=tsav.pop(-1)
                
            joueur+=1
        if scorj[0]-scorj[1]> scormax:
            scormax=scorj[0]-scorj[1]
            coupmax=i
    return(bin(coupmax),scormax)
def testcoup(nb,i):
    seed(0)
    tsav=[randint(1,14) for j in range (nb)]
    scorj=[0,0]
    joueur=0
    j=1
    for k in range (len(tsav)):
        #print(tsav, scorj[0]-scorj[1])
        if joueur%2==0:
            if j&i==0 : scorj[joueur%2]+=tsav.pop(0)
            else : scorj[joueur%2]+=tsav.pop(-1)
            j=j*2
        if joueur%2==1:
            if tsav[0]>tsav[-1]: scorj[joueur%2]+=tsav.pop(0)
            else:scorj[joueur%2]+=tsav.pop(-1)
            
        joueur+=1
    return scorj[0]-scorj[1]
def test(nb):
    seed(0)
    t=[randint(1,14) for i in range (nb)]
    tsav=t[:]
    print(t)
    print(solbotup(t))
    #print (solrec(tsav))
    

scorj=[0,0]
def jouersimu():
    t=[randint(1,14) for i in range(4)]
    ts=t[:]
    scorj=[0,0]
    joueur=0   
    while len(t)>0:
        if joueur%2==0:
            #print(t)
            #choix=input ('voulez vous prendre la - ou la +')
            if t[0]-max(t[1],t[-1])>t[-1]-max(t[0],t[-2]): choix='-'
            else : choix='+'
            if choix=='-': scorj[joueur%2]+=t.pop(0)
            else : scorj[joueur%2]+=t.pop(-1)
            #print(t)
        else:
            if t[0]>t[-1]: scorj[joueur%2]+=t.pop(0)
            else:scorj[joueur%2]+=t.pop(-1)

        joueur+=1

