import pandas as pd
import app.scripts.canvia as canvia
def p6(nass1,nass2):
    ass1 = canvia.canvianomacodi(nass1)
    ass2 = canvia.canvianomacodi(nass2)
    d = pd.read_csv('app/static/QuatrisTOT1conv.csv')
    t1 = 0
    t2 = 0
    ta1 = 0
    ta2 = 0
    d1 = d[d['CODASS'] == ass1]
    d2 = d[d['CODASS'] == ass2]
    for e in d1.itertuples():
        t1 = t1 +1
        if e[6] == 'N':
            ta1 = ta1 + 1
    for i in d2.itertuples():
        t2 = t2 +1
        if i[6] == 'N':
            ta2 = ta2 + 1
    print (t1,t2,ta1,ta2)
    return (ta1/t1)*100 > (ta2/t2)*100, (ta1/t1)*100, (ta2/t2)*100
