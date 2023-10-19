import pandas as pd
def p10(g1,g2):
    lanys=[2010,2011,2012,2013,2014,2015]
    l1=[]
    l2=[]
    df=pd.read_csv('app/static/QuatrisTOT.csv')
    df1=df[df.GR==g1]
    df1=df1.reset_index()
    del df1['index']
    df2=df[df.GR==g2]
    df2=df2.reset_index()
    del df2['index']
    dfd1=df1[df1.APR=='S']
    dfd2=df2[df2.APR=='S']
    APRg1=(len(dfd1)/len(df1))*100
    APRg2=(len(dfd2)/len(df2))*100
    for e in lanys:
        dff1=df1[df1.CURS==e]
        dff2=df2[df2.CURS==e]
        df3=dfd1[dfd1.CURS==e]
        df4=dfd2[dfd2.CURS==e]
        if len(dff1!=0):
            l1.append(len(df3)/len(dff1)*100)
        else:
            l1.append(0)
        if len(dff2!=0):
            l2.append(len(df4)/len(dff2)*100)
        else:
            l2.append(0)
    return APRg1>APRg2,APRg1,APRg2,l1,l2
