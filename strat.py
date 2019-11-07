import numpy
import random

def test_unitaire_numpy(liste):
    return numpy.array(liste)

test_unitaire_numpy([[0,1],[2,3]]) #exemple de vérification du module numpy

liste=[(0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3),(3,3),(3,2),(3,1),(3,0)]

def egale(mat1, mat2):
    for i in range(4):
        for j in range(4):
            if mat1[(i,j)]!=mat2[(i,j)]:
                return False
    return True

def test_unitaire_egale(a,b): #création de deux matrices carrées de taille 4 différentes composées d'entiers de [a,b]
    A,B=[],[]
    for k in range(4):
        for j in range(4):
            A[i][j]=random.randint(a,b)
    B,C=A,A
    C[3][3]=C[3][3]+1
    return A,B

egale(test_unitaire_egale(1,300)[0],test_unitaire_egale(1,300)[0]) #1 à 300 par exemple, doit retourner True pour tout a,b
egale(test_unitaire_egale(1,300)[0],test_unitaire_egale(1,300)[1]) #doit retourner False pour tout a,b

def joue_ligne(ligne):
    res = []
    for n in ligne:
        if n == 0:
            continue
        if len(res) == 0:
            res.append(n)
        else:
            prev = res[-1]
            if prev == n:
                res[-1] = 2 * n
            else: 
                res.append(n)
    while len(res) < len(ligne):
        res.append(0)
    return res

def test_unitaire_joue_ligne(a,b): #création d'une ligne de longueur 4 composée de puissance de 2 appartenant à [2**a,2**(b-1)]
    res=[]
    for k in range(4):
        n=random.randint(a,b)
        if n==0:
            res.append(0)
        else:
        res.append(2**n)
    return res

lgn=test_unitaire_joue_ligne(0,12) #0 et 12 tels que les puissances de 2 aillent jusqu'à 2048 maximum
joue_ligne(lgn)
    
def joue(mat, direction):
    if direction == 0:                                              # 0 : gauche
        lines = [joue_ligne(mat[i, :]) for i in range(4)]
        mat = numpy.array(lines)
        return mat
    elif direction == 1:                                            # 1 : haut
        lines = [joue_ligne(mat[:, i]) for i in range(4)]
        mat = numpy.array(lines)
        return mat.T
    elif direction == 2:                                            # 2 : droite
        lines = [list(reversed(joue_ligne(mat[i, ::-1]))) for i in range(4)]
        mat = numpy.array(lines)
        return mat
    elif direction == 3:                                            # 3 : bas
        lines = [list(reversed(joue_ligne(mat[::-1, i]))) for i in range(4)]
        mat = numpy.array(lines)
        return mat.T

def test_unitaire_joue(a,b): #création d'une matrice de taille 4 composée de puissance de 2 appartenant à [2**a,2**(b-1)]
    mat=[]
    for k in range(4):
        mat.append(test_unitaire_joue_ligne(a,b))
    return mat

mat=test_unitaire_joue(0,12)
direction = random.randint(4)
joue(mat, direction) #affiche la grille en ayant une grille initiale et en translatant dans la direction "direction"

    
def eval_situation(mat):
    cond= True
    score=0
    i=0
    while mat[liste[i]] != 0 and cond:
        cond=mat[liste[i]] >= mat[liste[i+1]]  
        score += mat[liste[i]]**2
        i += 1 
    return score

mat=test_unitaire_joue(0,12)
eval_situation(mat) #compte le nombre de cases rangées dans l'odre croissant (en terme de valeurs) en suivant la structure d'un serpentin (en terme de position, suivre les indices dans liste) 

    
def eval_situation_2(mat):
    cond = True
    score = 0
    i = 0
    while mat[liste[i]]!=0 and cond:
        cond=mat[liste[i]]>=mat[liste[i+1]]  
        score+=mat[liste[i]]**2
        i+=1 
    return score/(compte(mat)**0.01)
    
def eval_situation_3(mat, max):
    cond=True
    score=0
    i=0
    while mat[liste[i]]!=0 and cond:
        cond=mat[liste[i]]>=mat[liste[i+1]]  
        score+=mat[liste[i]]**2
        i+=1 
    if score >= max:
        return score/(compte(mat)**0.01)
    else:
        return 0
    
def compte(mat):
    compteur=0
    for i in liste:
        if mat[i]!=0:
            compteur+=1
    return compteur

mat=test_unitaire_joue(0,12) 
compter(mat) #vérifier que cela correspond bien le nombre d'éléments non nuls de la matrice de départ

def danger(mat):
    max=numpy.max(mat)
    if max>=512:
        return compte(mat)>=14
    elif max>=256:
        return compte(mat)>=13
    return compte(mat)>=12

mat=test_unitaire_joue(0,12)
danger(mat) 

def danger_2(mat):
    max=numpy.max(mat)
    if max>=512:
        return compte(mat)>=16
    elif max>=256:
        return compte(mat)>=16
    return compte(mat)>=15
    
def save(mat):
    min,imin=compte(joue(mat,0)),0
    for i in range(1,4):
        buf=compte(joue(mat,i))
        if buf<min:
            min,imin=buf,i
    return imin,min
    
def save_2(mat):
    min,imin=compte(joue(joue(mat,0),0)),0
    for i in range(0,4):
        for j in range(0,4):
            buf=compte(joue(joue(mat,i),j))
            if buf<min:
                min,imin=buf,i
    return imin,min

def save_3(mat):
    min,imin=compte(joue(joue(joue(mat,0),0),0)),0
    for i in range(0,4):
        for j in range(0,4):
            for k in range(0,4):
                buf=compte(joue(joue(joue(mat,i),j),k))
                if buf<min:
                    min,imin=buf,i
    return imin,min

mat=test_unitaire_joue(0,12)
A_0,A_1,A_2,A_3=joue(mat,0),joue(mat,1),joue(mat,2),joue(mat,3)
comp0,comp1,comp2,comp3=compte(A_0),compte(A_1),compte(A_2),compte(A_3)
save(mat) #vérifier que le minimum des comp est égale à save(mat)[1] et que la direction pour laquelle il est obtenu est save(mat)[0] 
#pour save_2 il faut définit A_i_j=joue(joue(mat,i),j), i étant la première direction choisie et j la deuxième

def perte(mat1,mat2):
    if compte(mat1)<12:
        return True
    cond=True
    score=0
    i=0
    liste1=[]
    buf=True
    while mat1[liste[i]]>8 and cond:
        cond=mat1[liste[i]]>=mat1[liste[i+1]] 
        liste1.append(mat1[liste[i]])
        i+=1
    for i in range(len(liste1)):
        buf=buf and (mat2[liste[i]]>=liste1[i])
    return buf

def strategy_2048(game,moves):
    max,imax=0,0
    if danger(game):
        print("danger")
        imin,min=save(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        buf=eval_situation(joue(game,i))
        print(i,buf)
        if buf>max:
            max,imax=buf,i
    return imax

def strategy_2048_2(game,moves):
    max,imax=0,0
    if danger(game):
        #print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
        for j in [1,0,2,3]:
            buf=eval_situation(joue(mat,j))
            #print(i,j,buf)
            if buf>max:
                max,imax=buf,i
    return imax
    
def strategy_2048_3(game,moves):
    max1,max2,imax=0,0,0
    if danger_2(game):
        #print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
        buf1=eval_situation(mat)
        for j in [1,0,2,3]:
            buf2=eval_situation(joue(mat,j))
            #print(i,j,buf1,buf2)
            if buf2>max2:
                max1,max2,imax=buf1,buf2,i
            if buf2==max2:
                if buf1>max1:
                    max1,max2,imax=buf1,buf2,i
    return imax
    
def strategy_2048_4(game,moves):
    max1,max2,imax=0,0,0
    if danger_2(game):
        #print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
        buf1=eval_situation(mat)
        if numpy.max(game)<=mat[(0,0)] or numpy.max(game)<numpy.max(mat):
            for j in [1,0,2,3]:
                buf2=eval_situation(joue(mat,j))
                #print(i,j,buf1,buf2)
                if buf2>max2:
                    max1,max2,imax=buf1,buf2,i
                if buf2==max2:
                    if buf1>max1:
                        max1,max2,imax=buf1,buf2,i
    return imax
    
def strategy_2048_5(game,moves):
    max1,max2,imax=0,0,0
    if danger_2(game):
        print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat = joue(game,i)
        buf1 = eval_situation_2(mat)
        if game[(0,0)] <= mat[(0,0)]:
            for j in [1,0,2,3]:
                buf2 = eval_situation_2(joue(mat,j))
                print(i,j,int(buf1),int(buf2))
                if buf2 > max2:
                    max1,max2,imax = buf1,buf2,i
                if buf2 == max2:
                    if buf1 > max1:
                        max1,max2,imax = buf1,buf2,i
    return imax
    
def strategy_2048_6(game,moves):
    max1,max2,imax=0,0,0
    if danger_2(game):
        #print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
        if not egale(game,mat):
            buf1=eval_situation_2(mat)
            if game[(0,0)]<=mat[(0,0)]:
                for j in [1,0,2,3]:
                    buf2=eval_situation_2(joue(mat,j))
                    #print(i,j,buf1,buf2)
                    if buf2>max2:
                        max1,max2,imax=buf1,buf2,i
                    if buf2==max2:
                        if buf1>max1:
                            max1,max2,imax=buf1,buf2,i
    return imax
    
def strategy_2048_7(game,moves):
    max1,max2,imax=0,0,0
    if danger_2(game):
        #print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
        buf1=eval_situation_3(mat,max1)
        if game[(0,0)]<=mat[(0,0)]:
            for j in [1,0,2,3]:
                buf2=eval_situation_3(joue(mat,j),max2)
                #print(i,j,buf1,buf2)
                if buf2>max2:
                    max1,max2,imax=buf1,buf2,i
                if buf2==max2:
                    if buf1>max1:
                        max1,max2,imax=buf1,buf2,i
    return imax
    
def strategy_2048_8(game,moves):
    max1,max2,max3,imax=0,0,0,0
    if danger_2(game):
        #print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
        buf1=eval_situation_2(mat)
        if game[(0,0)]<=mat[(0,0)]:
            for j in [1,0,2,3]:
                mat2=joue(mat,j)
                buf2=eval_situation_2(mat2)
                #print(i,j,buf1,buf2)
                for k in [1,0,2,3]:
                    buf3=eval_situation_2(joue(mat2,k))
                    if buf3>max3:
                        max1,max2,max3,imax=buf1,buf2,buf3,i
                    if buf3==max3:
                        if buf1>max1:
                            max1,max2,max3,imax=buf1,buf2,buf3,i
    return imax
    
def strategy_2048_9(game,moves):
    max1,max2,imax=0,0,0
    if danger_2(game):
        print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
        buf1=eval_situation_2(mat)
        if game[(0,0)]<=mat[(0,0)]:
            if compte(game)<=15:
                for j in [1,0,2,3]:
                    buf2=eval_situation_2(joue(mat,j))
                    print(i,j,int(buf1),int(buf2))
                    if buf2>max2:
                        max1,max2,imax=buf1,buf2,i
                    if buf2==max2:
                        if buf1>max1:
                            max1,max2,imax=buf1,buf2,i
            else:
                if buf1>max1:
                    max1,imax=buf1,i
                print('alternatif')
    return imax
    
def strategy_2048_10(game,moves):
    max1,max2,imax=0,0,0
    if danger_2(game):
        #print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
        buf1=eval_situation_2(mat)
        if game[(0,0)]<=mat[(0,0)] and perte(game,mat):
            for j in [1,0,2,3]:
                buf2=eval_situation_2(joue(mat,j))
                #print(i,j,int(buf1),int(buf2))
                if buf2>max2:
                    max1,max2,imax=buf1,buf2,i
                if buf2==max2:
                    if buf1>max1:
                        max1,max2,imax=buf1,buf2,i
        #else:
            #print(i,'perte')
    return imax
