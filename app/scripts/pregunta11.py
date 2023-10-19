
import pandas as pd

def canviacodianom(mun):
    l =[]
    f1=pd.read_csv('app/static/CPambDades.csv')
    n=-1
    for e in f1['NM']:
        n=n+1
        if e == mun:
            l.append(int(f1['CP'][n]))
    return l

def p11jej(n1):
    f1=pd.read_csv('app/static/dadesp.csv')
    n11 = canviacodianom(n1)
    n1 = 0
    for e in f1['CPF']:
        if int(e) in n11:
            n1=n1+1
    return n1


def p11(m1,m2):
    n1 = p11jej(m1)
    n2 = p11jej(m2)
    return n1>n2, n1,n2
