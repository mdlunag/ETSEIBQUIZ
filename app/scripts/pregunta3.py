import pandas as pd
def p3(t1,t2):
    d = pd.read_csv('app/static/QuatrisTOT.csv')
    if t1 == 'Carrera':
        return (d['NF'].mean() > d[d['QUATRI']==t2]['NF'].mean(),d['NF'].mean(), d[d['QUATRI']==t2]['NF'].mean())
    if t2 == 'Carrera':
        return(d[d['QUATRI']==t1]['NF'].mean() > d['NF'].mean(),d[d['QUATRI']==t1]['NF'].mean(), d['NF'].mean())
    return (d[d['QUATRI']==t1]['NF'].mean() > d[d['QUATRI']==t2]['NF'].mean(),d[d['QUATRI']==t1]['NF'].mean(), d[d['QUATRI']==t2]['NF'].mean())
