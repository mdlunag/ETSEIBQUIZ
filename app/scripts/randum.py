import random
import app.scripts.canvia as canvia
import pandas as pd
import app.scripts.llistamunicipis as llistamunicipis
lnommateries=['Càlcul I', 'Fonaments Informàtica', 'Mecànica Fonamental', 'Química I', 'Àlgebra Lineal', 'Càlcul II', 'Expressió Gràfica', 'Geometria', 'Química II', 'Termodinàmica Fonamental', 'Electromagnetisme', 'Equacions Diferencials', 'Informàtica', 'Materials', 'Mecànica', 'Mètodes Numèrics', 'Dinàmica de Sistemes', 'Economia i Empresa', 'Estadística', 'PROJECTE I', 'Teoria de Màquines i Mecanismes', 'Electrotècnia', 'Tecnologia del Medi Ambient i Sostenibilitat', 'Tecnologia i Selecció de Materials', 'Termodinàmica', 'Tècniques Estadístiques per la Qualitat', 'Mecànica de Fluids', 'Màquines Elèctriques', 'Simulació i Optimització', 'Organització i Gestió', 'PROJECTE II', 'Resistència de Materials', 'Control Automàtic', 'Electrònica', 'Gestió de Projectes', 'Sistemes de Fabricació', 'Termotècnia']
lmunicipi=llistamunicipis.lmunicipis()
lquatris=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','carrera']
quatris={'Q1': [240012, 240015, 240013, 240014,240011], 'Q2': [240022,240025,240021,240024,240023], 'Q3': [240031,240131,240132,240033,240133,240032], 'Q4':[240043,240041,240042,240044,240141], 'Q5': [240053,240051,240151,240052,240055], 'Q6': [240061,240161,240162,240062,240064,240063],'Q7': [240172,240072,240071,240073,240171]}

def ran1():
    in11=random.randint(0,10)
    in12=random.randint(0,10)
    in21=random.randint(0,10)
    in22=random.randint(0,10)
    while in12 < in11 or (in12-in11)>2:
        in12=random.randint(0,10)
    while in21>=(in11-2) and in21<=(in12):
        in21 = random.randint(0,10)
    if in21 > in12:
        while (in22 < in21) or (in22>=in11 and in22<=in12) or (in22-in21)>2 or (in22-in21)!=(in12-in11):
            in22=random.randint(0,10)
    elif in21 < (in11-2):
        while (in22 < in21) or (in22>in11 and in22<in12) or (in22-in21)!=(in12-in11) or in22>in12:
            in22=random.randint(0,10)
    return in11,in12,in21,in22

def ran2():
    q=random.choice(lquatris)
    apr=random.choice(('aprovada','suspesa'))
    l=[]
    m=[]

    if q=='carrera':
        materia=random.choice(lnommateries)
    else:
        n=len(quatris[q])
        num=random.randint(0,n-1)
        materia=canvia.canviacodianom(quatris[q][num])

    return materia,q,apr

def ran3():
    l = ['Carrera','Q1','Q2','Q3','Q4','Q5','Q6','Q7']
    i1 = random.choice(l)
    i2 = random.choice(l)
    while i2==i1:
        i2 = random.choice(l)
    return i1,i2

def ran4():
    ass=random.choice(lnommateries)
    num=random.randint(1,7)
    return ass, num

def ran5():
    q=random.choice(lquatris)
    a=random.randint(2010,2015)
    if a==2010:
        if q in 'Q3Q4Q5Q6Q7':
            q=random.choice(['Q1','Q2'])
    elif a==2011:
        if q in 'Q5Q6Q7':
            q=random.choice(['Q1','Q2','Q3','Q4'])
    elif a==2012:
        if q == 'Q7':
            q=random.choice(['Q1','Q2','Q3','Q4','Q5','Q6'])
    in1=random.randrange(40,80,5)
    in2=random.randrange(40,81,5)
    while in2<=in1 or abs(in2-in1)>20:
        in2=random.randrange(40,81,5)
    inter=(in1,in2)
    return q,a,inter

def ran6():
    lnommateries=['Càlcul I', 'Fonaments Informàtica', 'Mecànica Fonamental', 'Química I', 'Àlgebra Lineal', 'Càlcul II', 'Expressió Gràfica', 'Geometria', 'Química II', 'Termodinàmica Fonamental', 'Electromagnetisme', 'Equacions Diferencials', 'Informàtica', 'Materials', 'Mecànica', 'Mètodes Numèrics', 'Dinàmica de Sistemes', 'Economia i Empresa', 'Estadística', 'PROJECTE I', 'Teoria de Màquines i Mecanismes', 'Electrotècnia', 'Tecnologia del Medi Ambient i Sostenibilitat', 'Tecnologia i Selecció de Materials', 'Termodinàmica', 'Tècniques Estadístiques per la Qualitat', 'Mecànica de Fluids', 'Màquines Elèctriques', 'Simulació i Optimització', 'Organització i Gestió', 'PROJECTE II', 'Resistència de Materials', 'Control Automàtic', 'Electrònica', 'Gestió de Projectes', 'Sistemes de Fabricació', 'Termotècnia']
    a1 = random.choice(lnommateries)
    a2 = random.choice(lnommateries)
    while a2==a1:
        a2 = random.choice(lnommateries)
    return a1,a2

def ran7():
    lnotes=[9.5,10,10.5,11,11.5,12,12.5,13,13.5]
    nota=random.choice(lnotes)
    nsus=random.randint(1,5)
    return nota, nsus

def ran8():
    lpred=[]
    ass1=random.choice(lnommateries)
    for i in range(len(lquatris)-1):
        if canvia.canvianomacodi(ass1) in quatris[lquatris[i]]:
            ind=i
            break
    for j in range(ind,len(lquatris)-1):
        lpred+=quatris[lquatris[j]]
    ass2=canvia.canviacodianom(random.choice(lpred))
    ass3=canvia.canviacodianom(random.choice(lpred))
    while ass2==ass1 or ass2==ass3:
        ass2=canvia.canviacodianom(random.choice(lpred))
    while ass3==ass2 or ass3==ass1:
        ass3=canvia.canviacodianom(random.choice(lpred))
    return ass1,ass2,ass3

def ran9():
    l = ['Q1','Q2','Q3','Q4','Q5','Q6','Q7']
    p = random.randrange(35,86,5)
    t = random.choice(l)
    return p,t


def ran10():
    G=[10,20,30,40,50,60,70,80,90,100]
    G1=random.choice(G)
    G2=random.choice(G)
    while G1==G2:
        G2=random.choice(G)
    return G1,G2

def ran11():
    mun1=random.choice(lmunicipi)
    mun2=random.choice(lmunicipi)
    while mun1==mun2:
        mun2=random.choice(lmunicipi)
    return mun1,mun2

def ran12():
    l = ['Barcelona','Lleida','Girona','Tarragona']
    p1 = random.choice(l)
    p2 = random.choice(l)
    while p2==p1:
        p2 = random.choice(l)
    return p1,p2
