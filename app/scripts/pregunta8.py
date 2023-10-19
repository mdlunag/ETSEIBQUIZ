import pandas as pd
import app.scripts.canvia as canvia
def p8(as1,as2,as3):
    df=pd.read_csv('app/static/QuatrisTOT1conv.csv')
    codas1=canvia.canvianomacodi(as1)
    codas2=canvia.canvianomacodi(as2)
    codas3=canvia.canvianomacodi(as3)
    df=df[df.CODEX.isin(df[(df.CODASS==codas1) & (df.APR=='N')].CODEX)]
    df=df.reset_index()
    del df['index']
    df2=df[df.CODASS==codas2]
    df3=df[df.CODASS==codas3]
    p2=(len(df2[df2.APR=='N'])/len(df2))*100
    p3=(len(df3[df3.APR=='N'])/len(df3))*100
    return p2>p3,p2,p3
