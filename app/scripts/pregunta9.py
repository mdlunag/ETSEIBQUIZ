import pandas as pd
def p9(p,t):
    n=0
    s=0
    la=[]
    l=[]
    d2 = pd.read_csv('app/static/QuatrisTOT.csv')
    d2 = d2[d2['QUATRI']==t]
    d1 = pd.read_csv('app/static/dadesp.csv')
    dass = pd.read_csv('app/static/Assignatures.csv')

    d1 = d1[d1['CODEX'].isin(d2['CODEX'])]
    n = int(d1.count()[0])
   # for row in d2.itertuples():
        #if str(row[2]) in la:
    #    if str(row[6]) == 'N':
     #           s = s+1


    d2 = d2[d2['APR']=='N']
    for linia in d2.itertuples():
        if linia[1] not in l:
            s = s + 1
            l.append(linia[1])
    return p < (s/n)*100, (s/n)*100
