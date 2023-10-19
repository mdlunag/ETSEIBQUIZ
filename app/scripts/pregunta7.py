import pandas as pd
def p7(notasele,nsus):
    df=pd.read_csv('app/static/QuatrisTOT1conv.csv')
    dfd=pd.read_csv('app/static/SELEambQUALIF.csv')
    dfd2=dfd[dfd.SELE>notasele]
    df=df[df.CODEX.isin(dfd2.CODEX)]
    df=df.reset_index()
    del df['index']
    df2=df[df.QUATRI.isin(['Q1','Q2','Q3','Q4'])][df.APR=='N']
    n=len(df2)/len(dfd2)
    return n>nsus,n
