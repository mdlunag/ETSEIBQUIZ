import pandas as pd
def p1(interval1, interval2):
    d = pd.read_csv('app/static/qualif.csv')
    ns = 0
    ni = 0
    ntotal=0
    for e in d['NF']:
        ntotal+=1
        if e>=float(interval1[0]) and e<=float(interval1[1]):
            ns = ns + 1
        if e>=float(interval2[0]) and e<=float(interval2[1]):
            ni = ni + 1
    return ns>ni,int(ns),int(ni), ntotal
