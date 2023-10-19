import pandas as pd
import app.scripts.canvia as canvia
def p4(ass,num): #mira el nombre de vegades que s'ha suspès una assignatura
    codass=canvia.canvianomacodi(ass)
    df=pd.read_csv('app/static/QuatrisTOT.csv')
    df2=df[df.CODASS==codass][df.APR=='N']['APR'].groupby(df['CODEX'])
    n=df2.count().max()
    return (n==num, n)
