import pandas as pd
def p12no(p1):
    l1 = []
    l2 = []
    i=0
    i2=0
    nt1,ns1,nt2,ns2=0,0,0,0
    if p1 == 'Barcelona':
        p1 = '8'
    if p1 == 'Girona':
        p1 = '17'
    if p1 == 'Tarragona':
        p1 = '43'
    if p1 == 'Lleida':
        p1 = '25'
    d = pd.read_csv('QuatrisTOT.csv')
    dd = pd.read_csv('dadesp.csv')
    for e in dd['CPF']:
        if str(e).startswith(p1):
            l1.append(dd['CODEX'][i])
        i = i+1
    for k in d['CODEX']:
        if k in l1:
            nt1 = nt1 +1
            if d['APR'][i2]=='N':
                ns1=ns1+1

        i2 = i2+1
    perc1=((nt1-ns1)/nt1)*100

    return perc1
def p12resp(nom):
    if nom =='Barcelona':
        perc=78.2485022803477
    elif nom=='Tarragona':
        perc=78.77465857359635
    elif nom=='Girona':
        perc=83.17321688500728
    elif nom=='Lleida':
        perc=79.90953637391632
    return perc

def p12(nom1,nom2):
    perc1=p12resp(nom1)
    perc2=p12resp(nom2)
    return perc1>perc2,perc1,perc2
