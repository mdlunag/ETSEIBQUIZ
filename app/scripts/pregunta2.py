
import pandas as pd
quatris={'Q1': [240012, 240015, 240013, 240014,240011], 'Q2': [240022,240025,240021,240024,240023], 'Q3': [240031,240131,240132,240033,240133,240032], 'Q4':[240043,240041,240042,240044,240141], 'Q5': [240053,240051,240151,240052,240055], 'Q6': [240061,240161,240162,240062,240064,240063],'Q7': [240172,240072,240071,240073,240171]}

import app.scripts.canvia as canvia
def p2(apr,quatri,materia):
    l=[]
    m=[]
    h=[]
    f1=pd.read_csv('app/static/QuatrisTOTnoOpt.csv')
    f2 = pd.read_csv ('app/static/Assignatures.csv')

    if quatri == 'carrera':
        if apr=='aprovada':
            assig='Gestió de Projectes'
            percent=99.71
        else:
            assig='Mecànica'
            percent=47.86

    else:
        for e in quatris[quatri]:
            ns=0
            na=0
            n=-1
            for p in f1['CODASS']:
                n=n+1
                if p == e:
                    if f1['APR'][n]=='S':#apr
                        na=na+1
                    else:
                        ns=ns+1
            l.append((e,na,ns))

        for d in l:
            if apr == 'aprovada' and d[1]+d[2]>0:
                percent= d[1]/ (d[1]+d[2])*100
                m.append((d[0],percent))
            elif apr == 'suspesa' and d[1] +d[2]>0:
                percent =d[2]/(d[1]+d[2])*100
                m.append((d[0],percent))

        maxi= (0,0)
        for s in m:
            if s[1]>= maxi[1]:
                maxi= (int(s[0]),s[1])
            code = s[0]
            assig= canvia.canviacodianom(code)
            h.append((assig,s[1]))

        codi = maxi[0]
        percent = '{0:.2f}'.format(maxi[1])
        assig= canvia.canviacodianom(codi)
    #return materia == str (assig), "L'assignatura més "+ str(apr) + " en percentatge del " + str(quatri) + " és:  " + str(assig)+ " amb un "  + str(percent) + "%"
    return (materia==str(assig), assig, percent,h)
