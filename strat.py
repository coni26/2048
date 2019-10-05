#0:gauche;1:haut;2:droite;3:bas

import numpy

liste=[(0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3),(3,3),(3,2),(3,1),(3,0)]

def egale(mat1,mat2):
    for i in range(4):
        for j in range(4):
            if mat1[(i,j)]!=mat2[(i,j)]:
                return False
    return True

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

def joue(mat,direction):
    if direction == 0:
        lines = [joue_ligne(mat[i, :]) for i in range(4)]
        mat = numpy.array(lines)
        return mat
    elif direction == 1:
        lines = [joue_ligne(mat[:, i]) for i in range(4)]
        mat = numpy.array(lines)
        return mat.T
    elif direction == 2:
        lines = [list(reversed(joue_ligne(mat[i, ::-1]))) for i in range(4)]
        mat = numpy.array(lines)
        return mat
    elif direction == 3:
        lines = [list(reversed(joue_ligne(mat[::-1, i]))) for i in range(4)]
        mat = numpy.array(lines)
        return mat.T

def eval_situation(mat):
    cond=True
    score=0
    i=0
    while mat[liste[i]]!=0 and cond:
        cond=mat[liste[i]]>=mat[liste[i+1]]  
        score+=mat[liste[i]]**2
        i+=1 
    return score
    
def eval_situation_2(mat):
    cond=True
    score=0
    i=0
    while mat[liste[i]]!=0 and cond:
        cond=mat[liste[i]]>=mat[liste[i+1]]  
        score+=mat[liste[i]]**2
        i+=1 
    return score/(compte(mat)**0.009)
    
def eval_situation_3(mat,max):
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

def danger(mat):
    max=numpy.max(mat)
    if max>=512:
        return compte(mat)>=14
    elif max>=256:
        return compte(mat)>=13
    return compte(mat)>=12

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
        #print("danger")
        imin,min=save_2(game)
        if min<compte(game):
            return imin
    for i in [1,0,2,3]:
        mat=joue(game,i)
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