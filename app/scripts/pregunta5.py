import pandas as pd

def p5(quatri,a,num):
    l=[]
    m=[]
    f1=pd.read_csv('app/static/QuatrisTOT.csv')

    if quatri == 'carrera':
        f2 = f1[int(f1['CURS'])==a]
        na=0
        nt=0
        for e in f2['APR']:
            nt +=1
            if e== 'S':
                na+=1
        frase= ' la carrera'


    else:
        print(quatri)
        print(type(str(f1['CURS'][0])),type(a))
        f2=f1[f1['QUATRI']==quatri]
        print(a)
        f3=f2[f2['CURS']==int(a)]
        f3
        na=0
        nt=0
        for e in f3['APR']:
            nt +=1
            if e== 'S':
                na+=1
        quatr= str(quatri)
        frase= ' el ' + quatr
    percent= na/nt*100
    return percent <= num[1] and percent >=num[0],  percent
