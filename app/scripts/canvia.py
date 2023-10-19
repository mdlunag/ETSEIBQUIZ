import pandas as pd
def canvianomacodi(nomassig):
    f1=pd.read_csv('app/static/Assignatures.csv')
    n=-1
    for e in f1['NOM']:
        n=n+1
        if e == nomassig:

            return f1['CODASS'][n]

def canviacodianom (codi):
     f1=pd.read_csv('app/static/Assignatures.csv')
     n=-1
     for e in f1['CODASS']:
         n=n+1
         if e==codi:
             return f1['NOM'][n]
