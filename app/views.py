from flask import render_template
from app import app
from flask import request
#from app.scripts import calculs as cal

from app.scripts.pregunta1 import p1
from app.scripts.pregunta3 import p3
from app.scripts.pregunta6 import p6
from app.scripts.pregunta9 import p9
from app.scripts.pregunta12 import p12
from app.scripts.pregunta4 import p4
from app.scripts.pregunta7 import p7
from app.scripts.pregunta8 import p8
from app.scripts.pregunta10 import p10
from app.scripts.pregunta2 import p2
from app.scripts.pregunta5 import p5
from app.scripts.pregunta11 import p11
import app.scripts.randum as randum
import app.scripts.canvia as canvia

@app.route('/')
@app.route('/index')
def index():
    global nencerts
    nencerts=0
    global in11,in12,in21,in22,materia22,q22,apr,i1,i2,ass,num,q,a,inter,a1,a2,nota,nsus,ass1,ass2,ass3,p,t,g1,g2,mun1,mun2,pr1,pr2
    in11,in12,in21,in22 = randum.ran1()
    materia22,q22,apr= randum.ran2()
    i1,i2=randum.ran3()
    ass,num=randum.ran4()
    q,a,inter=randum.ran5()
    a1,a2=randum.ran6()
    nota,nsus=randum.ran7()
    ass1,ass2,ass3=randum.ran8()
    p,t=randum.ran9()
    g1,g2=randum.ran10()
    mun1,mun2=randum.ran11()
    pr1,pr2=randum.ran12()

    return render_template('principal.html')

@app.route('/esc')
def esc():
    return render_template('escollible.html')

@app.route('/inp1')
def pregunta1():

    return render_template('inp1.html',
                           in11=in11,in12=in12,in21=in21,in22=in22)

@app.route('/p1', methods=['POST'])
def preg1():
    bolea = request.form['bolea']
    in1 = (int(in11),int(in12))
    in2 = (int(in21),int(in22))
    d = p1(in1,in2)
    dades1 = d[1]
    dades2 = d[2]
    perc1= (dades1/d[3])*100
    perc2= (dades2/d[3])*100
    altres = 100-perc1-perc2
    if (str(d[0])==str(bolea)):
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/inp2'
    return render_template('resp1.html',
                           title='INTERVALS',
                           in1=in1,
                           in2=in2,
                           perc1=perc1,
                           perc2=perc2,
                           altres=altres,
                           dades1 = dades1,
                           dades2 = dades2,
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/esp1')
def escollible1():
    return render_template('esp1.html')

@app.route('/pe1', methods=['POST'])
def esc1():
    in11 = request.form['in11']
    in12 = request.form['in12']
    in21 = request.form['in21']
    in22 = request.form['in22']
    in1 = (int(in11),int(in12))
    in2 = (int(in21),int(in22))
    if in1==in2 or float(in11)>10 or float(in12)>10 or float(in21)>10 or float(in22)>10 or float(in11)<0 or float(in12)<0 or float(in21)<0 or float(in22)<0:
        botonet='/esp1'
        return render_template('fail.html',botonet=botonet)
    d = p1(in1,in2)
    dades1 = d[1]
    dades2 = d[2]
    perc1= (dades1/d[3])*100
    perc2= (dades2/d[3])*100
    altres = 100-perc1-perc2
    if d[0]:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/esc'
    boton2='/esp2'
    return render_template('resp1.html',
                           title='INTERVALS',
                           in1=in1,
                           in2=in2,
                           perc1=perc1,
                           perc2=perc2,
                           altres=altres,
                           dades1 = dades1,
                           dades2 = dades2,
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/inp2')
def pregunta2():

    if q22=='carrera':
         frase= ' de la carrera'
    else:
        frase = ' del ' + q22
    return render_template('inp2.html',
                           materia=materia22,f=frase,apr=apr)

@app.route('/p2', methods=['POST'])
def preg2():
    bolea = request.form['bolea']
    resposta,assig2,percent2,percass=p2(apr,q22,materia22)
    assig=[]
    perc=[]
    if q22=='carrera':
         frase1= ' la carrera'
         frase2 = 'de la carrera'
         assig=['Àlgebra Lineal', 'Càlcul I', 'Mecànica Fonamental', 'Química I', 'Fonaments Informàtica', 'Geometria', 'Càlcul II', 'Termodinàmica Fonamental', 'Química II', 'Expressió Gràfica', 'Electromagnetisme', 'Equacions Diferencials', 'Informàtica', 'Mètodes Numèrics', 'Materials', 'Mecànica', 'Economia i Empresa', 'Estadística', 'Dinàmica de Sistemes', 'Teoria de Màquines i Mecanismes', 'PROJECTE I', 'Tecnologia del Medi Ambient i Sostenibilitat', 'Termodinàmica', 'Electrotècnia', 'Tecnologia i Selecció de Materials', 'Tècniques Estadístiques per la Qualitat', 'Mecànica de Fluids', 'Organització i Gestió', 'Resistència de Materials', 'Màquines Elèctriques', 'Simulació i Optimització', 'PROJECTE II', 'Gestió de Projectes', 'Electrònica', 'Sistemes de Fabricació', 'Termotècnia', 'Control Automàtic']
         if apr=='aprovada':
             perc=[72.05882352941177, 68.77649909145973, 66.46670665866826, 76.76282051282051, 67.44784224064018, 72.06381534283774, 70.78537576167908, 67.79440468445023, 79.8132183908046, 78.16777816777817, 66.48022373152217, 74.42528735632183, 77.57601351351352, 86.08385370205174, 72.34660033167496, 52.138620043709025, 91.35432283858071, 90.72270630445925, 86.95434019066734, 72.81863864778437, 99.55357142857143, 82.05268935236005, 86.5680473372781, 68.17055032226078, 82.99595141700405, 94.44093493367025, 78.48266841072596, 89.36026936026936, 88.48396501457727, 89.06030855539971, 80.19607843137256, 99.6887159533074, 99.70958373668925, 86.06701940035273, 93.75, 77.92531120331951, 72.55779269202088]
         elif apr=='suspesa':
             perc=[27.941176470588232, 31.223500908540274, 33.53329334133174, 23.23717948717949, 32.552157759359815, 27.936184657162258, 29.214624238320923, 32.20559531554977, 20.186781609195407, 21.832221832221833, 33.51977626847783, 25.57471264367817, 22.423986486486484, 13.91614629794826, 27.653399668325036, 47.861379956290975, 8.645677161419286, 9.277293695540749, 13.045659809332662, 27.18136135221563, 0.4464285714285694, 17.947310647639952, 13.431952662721898, 31.82944967773922, 17.00404858299595, 5.559065066329751, 21.517331589274036, 10.639730639730644, 11.516034985422735, 10.939691444600285, 19.803921568627445, 0.3112840466926059, 0.2904162633107461, 13.932980599647266, 6.25, 22.07468879668049, 27.442207307979118]

    else:
        frase1= ' el ' + q22
        frase2='del '+q22
        for e in percass:
            assig.append(e[0])
            perc.append(e[1])
    if str(apr)=='aprovada':
        ap='aprovades'
        apr1= 'aprovada'

    else:
        ap='supeses'
        apr1 ='suspesa'
    if str(resposta)==str(bolea):
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'


    d = str(perc)
    dades = "name: 'percentatge',data:"+ d
    assign=str(assig)
    boton='/index'
    boton2='/inp3'

    return render_template('resp2.html',s=text, f=culor,
                            title='Percentatge de matèries '+ap+' durant'+frase1,
                            perce=percent2,materiabo=assig2,frase2=frase2,ap=ap,apr1=apr1,
                            assign = assign, dataseries= dades, boton=boton, boton2=boton2)


@app.route('/esp2')
def escollible2():
    return render_template('esp2.html')

@app.route('/pe2', methods=['POST'])
def esc2():
    apr = request.form['apr']
    q = request.form['q']
    materia = request.form['materia']
    codim=canvia.canvianomacodi(materia)
    lquatris={'Q1': [240012, 240015, 240013, 240014,240011], 'Q2': [240022,240025,240021,240024,240023], 'Q3': [240031,240131,240132,240033,240133,240032], 'Q4':[240043,240041,240042,240044,240141], 'Q5': [240053,240051,240151,240052,240055], 'Q6': [240061,240161,240162,240062,240064,240063],'Q7': [240172,240072,240071,240073,240171]}

    assig=[]
    perc=[]
    resposta,assig2,percent2,percass=p2(apr,q,materia)
    if q=='carrera':
         frase1= ' la carrera'
         frase2 = 'de la carrera'
         assig=['Àlgebra Lineal', 'Càlcul I', 'Mecànica Fonamental', 'Química I', 'Fonaments Informàtica', 'Geometria', 'Càlcul II', 'Termodinàmica Fonamental', 'Química II', 'Expressió Gràfica', 'Electromagnetisme', 'Equacions Diferencials', 'Informàtica', 'Mètodes Numèrics', 'Materials', 'Mecànica', 'Economia i Empresa', 'Estadística', 'Dinàmica de Sistemes', 'Teoria de Màquines i Mecanismes', 'PROJECTE I', 'Tecnologia del Medi Ambient i Sostenibilitat', 'Termodinàmica', 'Electrotècnia', 'Tecnologia i Selecció de Materials', 'Tècniques Estadístiques per la Qualitat', 'Mecànica de Fluids', 'Organització i Gestió', 'Resistència de Materials', 'Màquines Elèctriques', 'Simulació i Optimització', 'PROJECTE II', 'Gestió de Projectes', 'Electrònica', 'Sistemes de Fabricació', 'Termotècnia', 'Control Automàtic']
         if apr=='aprovada':
             perc=[72.05882352941177, 68.77649909145973, 66.46670665866826, 76.76282051282051, 67.44784224064018, 72.06381534283774, 70.78537576167908, 67.79440468445023, 79.8132183908046, 78.16777816777817, 66.48022373152217, 74.42528735632183, 77.57601351351352, 86.08385370205174, 72.34660033167496, 52.138620043709025, 91.35432283858071, 90.72270630445925, 86.95434019066734, 72.81863864778437, 99.55357142857143, 82.05268935236005, 86.5680473372781, 68.17055032226078, 82.99595141700405, 94.44093493367025, 78.48266841072596, 89.36026936026936, 88.48396501457727, 89.06030855539971, 80.19607843137256, 99.6887159533074, 99.70958373668925, 86.06701940035273, 93.75, 77.92531120331951, 72.55779269202088]
         elif apr=='suspesa':
             perc=[27.941176470588232, 31.223500908540274, 33.53329334133174, 23.23717948717949, 32.552157759359815, 27.936184657162258, 29.214624238320923, 32.20559531554977, 20.186781609195407, 21.832221832221833, 33.51977626847783, 25.57471264367817, 22.423986486486484, 13.91614629794826, 27.653399668325036, 47.861379956290975, 8.645677161419286, 9.277293695540749, 13.045659809332662, 27.18136135221563, 0.4464285714285694, 17.947310647639952, 13.431952662721898, 31.82944967773922, 17.00404858299595, 5.559065066329751, 21.517331589274036, 10.639730639730644, 11.516034985422735, 10.939691444600285, 19.803921568627445, 0.3112840466926059, 0.2904162633107461, 13.932980599647266, 6.25, 22.07468879668049, 27.442207307979118]



    else:
        if codim not in lquatris[q]:
            botonet='/esp2'
            return render_template('qassig.html',botonet=botonet)
        frase1= ' el ' + q
        frase2='del '+q
        for e in percass:
            assig.append(e[0])
            perc.append(e[1])
    if str(apr)=='aprovada':
        ap='aprovades'
        apr1= 'aprovada'

    else:
        ap='supeses'
        apr1 ='suspesa'
    if resposta:
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'


    d = str(perc)
    dades = "name: 'percentatge',data:"+ d
    assign=str(assig)

    boton='/esc'
    boton2='/esp3'
    return render_template('resp2.html',s=text, f=culor, title='Percentatge de matèries '+ap+' durant'+frase1,perce=percent2,materiabo=assig2,frase2=frase2,ap=ap,apr1=apr1, assign = assign, dataseries= dades, boton=boton, boton2=boton2)

@app.route('/inp3')
def pregunta3():
    if i1 =='Carrera':
         frase3= 'de la carrera'
    else:
        frase3= 'del '+i1

    if i2 =='Carrera':
        frase32='de la carrera '
    else:
        frase32='del '+i2
    return render_template('inp3.html',
                           i1=frase3,i2=frase32)


@app.route('/p3', methods=['POST'])
def preg3():
    bolea = request.form['bolea']
    d = p3(i1,i2)
    dad = str([float(d[1]),float(d[2])])
    dades = "name: 'mitjana', data:"+ dad
    assig = str([i1,i2])
    if i1 =='Carrera':
         frase3= 'de la carrera '
    else:
        frase3= 'del '+i1

    if i2 =='Carrera':
        frase32='de la carrera '
    else:
        frase32='del '+i2

    if (str(d[0])==str(bolea)):
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    d1='{0:.2f}'.format(d[1])
    d2='{0:.2f}'.format(d[2])
    boton='/index'
    boton2='/inp4'
    return render_template('resp3.html',
                           title='Mitjanes',
                           assig = assig,
                           dataseries=dades,
                           frase3=frase3,frase32=frase32,
                           dades1 = d1,
                           dades2 = d2,
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/esp3')
def escollible3():
    return render_template('esp3.html')

@app.route('/pe3', methods=['POST'])
def esc3():
    i1 = request.form['in1']
    i2 = request.form['in2']
    if i1==i2:
        botonet='/esp3'
        return render_template('fail.html',botonet=botonet)
    d = p3(i1,i2)
    dad = str([float(d[1]),float(d[2])])
    dades = "name: 'mitjana', data:"+ dad
    assig = str([i1,i2])
    if i1 =='Carrera':
         frase3= 'de la carrera '
    else:
        frase3= 'del '+i1

    if i2 =='Carrera':
        frase32='de la carrera '
    else:
        frase32='del '+i2

    if d[0]:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    d1='{0:.2f}'.format(d[1])
    d2='{0:.2f}'.format(d[2])
    boton='/esc'
    boton2='/esp4'
    return render_template('resp3.html',
                           title='Mitjanes',
                           assig = assig,
                           dataseries=dades,
                           frase3=frase3,frase32=frase32,
                           dades1 = d1,
                           dades2 = d2,
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/inp4')
def pregunta4():
    return render_template('inp4.html', ass=ass, num=num)

@app.route('/p4', methods=['POST'])
def preg4():
    bolea = request.form['bolea']
    resp4,numreal=p4(ass,int(num))
    encert=bolea==str(resp4)
    if encert:
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/inp5'
    return render_template('resp4.html',s=text,f=culor,ass=ass,numreal=numreal, boton=boton, boton2=boton2)

@app.route('/esp4')
def escollible4():
    return render_template('esp4.html')

@app.route('/pe4', methods=['POST'])
def esc4():
    assign=request.form['assignatura']
    nums = request.form['nums']
    resp4,numreal=p4(assign,int(nums))
    if resp4:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/esc'
    boton2='/esp5'
    return render_template('resp4.html',s=text,f=culor,ass=assign,numreal=numreal,boton=boton,boton2=boton2)

@app.route('/inp5')
def pregunta5():
    if q=='carrera':
         frase= 'de la carrera'
    else:
        frase = 'del ' + q
    in1=inter[0]
    in2=inter[1]
    return render_template('inp5.html', a=str(a),frase=frase,in1=str(in1),in2=str(in2))

@app.route('/p5', methods=['POST'])
def preg5():
    bolea = request.form['bolea']
    resposta, per=p5(q,a,inter)
    if q=='carrera':
         frase= 'de la carrera'
    else:
        frase = 'del ' + q
    percent=int(per)
    if str(resposta)==str(bolea):
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/inp6'
    return render_template('resp5.html', a=str(a),frase=frase,percent=percent,f=culor, s=text, boton=boton, boton2=boton2)

@app.route('/esp5')
def escollible5():
    return render_template('esp5.html')

@app.route('/pe5', methods=['POST'])
def esc5():
    a = request.form['a']
    q = request.form['q']
    in1 = request.form['in1']
    in2 = request.form['in2']
    if (a=='2010' and q in 'Q3Q4Q5Q6Q7') or (a=='2011' and q in 'Q5Q6Q7') or (a=='2012' and q == 'Q7'):
        botonet='/esp5'
        return render_template('faltadades.html',botonet=botonet)
    inter=(float(in1),float(in2))
    resposta,per=p5(q,a,inter)
    if q=='carrera':
         frase= 'de la carrera'
    else:
        frase = 'del ' + q
    percent=int(per)
    if resposta:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton = '/esc'
    boton2='/esp6'
    return render_template('resp5.html', a=str(a),frase=frase,percent=percent,f=culor, s=text, boton=boton, boton2=boton2)

@app.route('/inp6')
def pregunta6():
    return render_template('inp6.html',
                           a1=a1,a2=a2)

@app.route('/p6', methods=['POST'])
def preg6():
    bolea = request.form['bolea']
    d = p6(a1,a2)
    dad = str([float(d[1]),float(d[2])])
    dades = "name: 'percentatge suspesos', data:"+ dad
    assig = str([a1,a2])
    if (str(d[0])==str(bolea)):
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/inp7'
    return render_template('resp6.html',
                           title='Mitjanes',
                           assig = assig,
                           dataseries=dades,
                           in1=a1,
                           in2=a2,
                           dades1 = '{0:.2f}'.format(d[1]),
                           dades2 = '{0:.2f}'.format(d[2]),
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/esp6')
def escollible6():
    return render_template('esp6.html')

@app.route('/pe6', methods=['POST'])
def esc6():
    a1 = request.form['a1']
    a2 = request.form['a2']
    if a1==a2:
        botonet='/esp6'
        return render_template('fail.html',botonet=botonet)
    d = p6(a1,a2)
    dad = str([float(d[1]),float(d[2])])
    dades = "name: 'percentatge suspesos', data:"+ dad
    assig = str([a1,a2])
    if d[0]:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/esc'
    boton2='/esp7'
    return render_template('resp6.html',
                           title='Mitjanes',
                           assig = assig,
                           dataseries=dades,
                           in1=a1,
                           in2=a2,
                           dades1 = '{0:.2f}'.format(d[1]),
                           dades2 = '{0:.2f}'.format(d[2]),
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/inp7')
def pregunta7():
    return render_template('inp7.html', nota=nota, nsus=nsus)

@app.route('/p7', methods=['POST'])
def preg7():
    bolea=request.form['bolea']
    resp7,nsusreal=p7(nota,nsus)
    encert=bolea==str(resp7)
    if encert:
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    nsusreal= '{0:.2f}'.format(nsusreal)
    boton='/index'
    boton2='/inp8'
    return render_template('resp7.html',s=text,f=culor,nota=nota,nsusreal=nsusreal, boton=boton, boton2=boton2)

@app.route('/esp7')
def escollible7():
    return render_template('esp7.html')

@app.route('/pe7', methods=['POST'])
def esc7():
    nums=float(request.form['nums'])
    notasele = float(request.form['notasele'])
    if nums>10 or notasele>14:
        botonet='/esp7'
        return render_template('fail.html',botonet=botonet)
    if notasele>13.75:
        botonet='/esp7'
        return render_template('nop.html',botonet=botonet)
    resp7,numreal=p7(notasele,nums)
    if resp7:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    numreal= '{0:.2f}'.format(numreal)
    boton='/esc'
    boton2='/esp8'
    return render_template('resp7.html',s=text,f=culor,nota=notasele,nsusreal=numreal,boton=boton,boton2=boton2)

@app.route('/inp8')
def pregunta8():
    return render_template('inp8.html', ass1=ass1, ass2=ass2, ass3=ass3)

@app.route('/p8', methods=['POST'])
def preg8():
    bolea = request.form['bolea']
    resp13,prass2,prass3=p8(ass1,ass2,ass3)
    assig=str([ass2,ass3])
    dades1=prass2
    dades2=prass3
    d = str([prass2,prass3])
    dades = "name: 'Assignatura', data:"+ d
    encert=bolea==str(resp13)
    if encert:
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/inp9'
    return render_template('resp8.html',
                           title="Probabilitat de suspendre",
                           assig = assig,
                           dataseries=dades,
                           ass1=ass1,
                           ass2=ass2,
                           ass3=ass3,
                           prass2='{0:.2f}'.format(prass2),
                           prass3='{0:.2f}'.format(prass3),
                           dades1 = dades1,
                           dades2 = dades2,
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/esp8')
def escollible8():
    return render_template('esp8.html')

@app.route('/pe8', methods=['POST'])
def esc8():
    assignatura1 = request.form['assignatura1']
    assignatura2 = request.form['assignatura2']
    assignatura3 = request.form['assignatura3']
    if assignatura1==assignatura2 or assignatura1==assignatura3 or assignatura2==assignatura3:
        botonet='/esp8'
        return render_template('fail.html')
    resp8,prass2,prass3=p8(assignatura1,assignatura2,assignatura3)
    assig=str([assignatura2,assignatura3])
    dades1=prass2
    dades2=prass3
    d = str([prass2,prass3])
    dades = "name: 'Assignatura', data:"+ d
    if resp8:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/esc'
    boton2='/esp9'
    return render_template('resp8.html',
                           title="Probabilitat de suspendre",
                           assig = assig,
                           dataseries=dades,
                           ass1=assignatura1,
                           ass2=assignatura2,
                           ass3=assignatura3,
                           prass2='{0:.2f}'.format(prass2),
                           prass3='{0:.2f}'.format(prass3),
                           dades1 = dades1,
                           dades2 = dades2,
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/inp9')
def pregunta9():
    return render_template('inp9.html',
                           p=p,t=t)

@app.route('/p9', methods=['POST'])
def preg9():
    bolea = request.form['bolea']
    d = p9(p,t)
    if (str(d[0])==str(bolea)):
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/inp10'
    return render_template('resp9.html',
                           title='Mitjanes',
                           in1=p,
                           in2=t,
                           d = '{0:.2f}'.format(d[1]),
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/esp9')
def escollible9():
    return render_template('esp9.html')

@app.route('/pe9', methods=['POST'])
def esc9():
    p = float(request.form['p'])
    t = request.form['t']
    d = p9(p,t)
    if d[0]:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton = '/esc'
    boton2='/esp10'
    return render_template('resp9.html',
                           title='Mitjanes',
                           in1=p,
                           in2=t,
                           d = '{0:.2f}'.format(d[1]),
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/inp10')
def pregunta10():
    return render_template('inp10.html', g1=g1, g2=g2)

@app.route('/p10', methods=['POST'])
def preg10():
    bolea = request.form['bolea']
    resp10,aprg1,aprg2,llista1,llista2=p10(g1,g2)
    grups=str([g1,g2])
    dades1=aprg1
    dades2=aprg2
    d = str([aprg1,aprg2])
    dades = "name: 'Grup', data:"+ d
    encert=bolea==str(resp10)
    if encert:
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/inp11'
    return render_template('resp10.html',
                           title="Percentatge d'aprovats",
                           grups = grups,
                           dataseries=dades,
                           g1=g1,
                           g2=g2,
                           llista1=llista1,
                           llista2=llista2,
                           dades1 = '{0:.2f}'.format(dades1),
                           dades2 = '{0:.2f}'.format(dades2),
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/esp10')
def escollible10():
    return render_template('esp10.html')

@app.route('/pe10', methods=['POST'])
def esc10():
    grup1 = int(request.form['grup1'])
    grup2 = int(request.form['grup2'])
    if grup1==grup2:
        botonet="/esp10"
        return render_template('fail.html')
    resp10,aprg1,aprg2,llista1,llista2=p10(grup1,grup2)
    grups=str([grup1,grup2])
    dades1=aprg1
    dades2=aprg2
    d = str([aprg1,aprg2])
    dades = "name: 'Grup', data:"+ d
    if resp10:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/esc'
    boton2='/esp11'
    return render_template('resp10.html',
                           title="Percentatge d'aprovats",
                           grups = grups,
                           dataseries=dades,
                           g1=grup1,
                           g2=grup2,
                           llista1=llista1,
                           llista2=llista2,
                           dades1 = '{0:.2f}'.format(dades1),
                           dades2 = '{0:.2f}'.format(dades2),
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/inp11')
def pregunta11():
    return render_template('inp11.html', mun1=mun1,mun2=mun2)

@app.route('/p11', methods=['POST'])
def preg11():
    bolea = request.form['bolea']
    resposta, n1, n2=p11(mun1,mun2)
    if str(resposta)==str(bolea):
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/inp12'
    return render_template('resp11.html', mun1=mun1,mun2=mun2, n1=n1,n2=n2, s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/esp11')
def escollible11():
    return render_template('esp11.html')

@app.route('/pe11', methods=['POST'])
def esc11():
    mun1 = request.form['mun1']
    mun2 = request.form['mun2']
    if mun1==mun2:
        botonet='/esp11'
        return render_template('fail.html',botonet=botonet)
    resposta, n1, n2=p11(mun1,mun2)
    if resposta:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/esc'
    boton2='/esp12'
    return render_template('resp11.html', mun1=mun1,mun2=mun2, n1=n1,n2=n2, s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/inp12')
def pregunta12():
    return render_template('inp12.html',
                           pr1=pr1,pr2=pr2)

@app.route('/p12', methods=['POST'])
def preg12():
    bolea = request.form['bolea']
    d = p12(pr1,pr2)
    dad = str([float(d[1]),float(d[2])])
    dades = "name: 'percentatge', data:"+ dad
    assig = str([pr1,pr2])
    if (str(d[0])==str(bolea)):
        text = 'Correcte!'
        global nencerts
        nencerts += 1
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton='/index'
    boton2='/final'
    return render_template('resp12.html',
                           title='Mitjanes',
                           in1=pr1,
                           in2=pr2,
                           v1 = '{0:.2f}'.format(d[1]),
                           v2 = '{0:.2f}'.format(d[2]),
                           assig = assig,
                           dataseries=dades,
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/esp12')
def escollible12():
    return render_template('esp12.html')

@app.route('/pe12', methods=['POST'])
def esc12():
    pr1 = request.form['pr1']
    pr2 = request.form['pr2']
    if pr1 == pr2:
        botonet='/esp12'
        return render_template('fail.html',botonet=botonet)
    d = p12(pr1,pr2)
    dad = str([float(d[1]),float(d[2])])
    dades = "name: 'Percentatge', data:"+ dad
    assig = str([pr1,pr2])
    if d[0]:
        text = 'Correcte!'
        culor='green'
    else:
        text = "T'has equivocat!"
        culor ='red'
    boton = '/esc'
    boton2 = '/index'
    return render_template('resp12.html',
                           title='Províncies',
                           in1=pr1,
                           in2=pr2,
                           v1 = '{0:.2f}'.format(d[1]),
                           v2 = '{0:.2f}'.format(d[2]),
                           assig = assig,
                           dataseries=dades,
                           s=text, f=culor, boton=boton, boton2=boton2)

@app.route('/final')
def final():
    global nencerts
    resultat=''
    t2 = ''
    if nencerts >12:
        resultat='Felicitats! Has encertat ' + str(nencerts) + ' preguntes de 12'
        text = "El proper cop que facis trampes intenta que no es noti tant. Segur que ets alumne de l'ETSEIB?"
        t2 = ' Tens un 0 :)'
    if nencerts==12:
        resultat="Matrícula d'honor!"
        text = "Les llegendes deien que era impossible, però tu ho has aconseguit!"
        t2 = "Has fet trampes, no?"
        #text="No se t'escapa ni una! Es nota que estàs interessat en els afers de l'escola i ho tens tot controlat. Esperem que portis els estudis igual de bé, segueix així!"
    elif nencerts==11 or nencerts==10:
        resultat="Excel·lent!"
        text ="Felicitats! Domines a la perfecció la vida de l'ETSEIB i els seus mites. Si tan sols la carrera se't donés així de bé..."
        #text="Felicitats! Tens molt domini de la vida ETSEIB i els seus mites. Segueix treballant per emportar-te la matrícula, gairebé ho tens!  "
    elif nencerts==9 or nencerts==8:
        resultat="Notable!"
        text="Enhorabona! Has tret un notable sense haver-te hagut de gastar 599€ en una acadèmia!"
        t2="Perquè no t'hi has apuntat, oi?"
    elif nencerts==7 or nencerts==6:
        resultat="Aprovat!"
        text='Ni fu ni fa. Ni bé ni malament. Ni blanc ni negre. Ni carn ni peix. Resumint, que ets del "montón".'
        t2="Felicitats?"
    elif nencerts==5:
        resultat="Campana de Gauss!"
        text="Aprovat pels pèls! La llei del mínim esforç, et quedes a les portes de l'aprovat i la campana fa la resta. "
        t2="El proper cop no tindràs tanta sort :)"
    elif nencerts<5:
        resultat="Reavaluació!"
        text="Justament t'han sortit les preguntes que no t'havies estudiat, oi? Pots anar a revisió el diumenge que ve a la planta 23 a les 6:02 del matí, a veure si estem de bon humor i et pugem mitja dècima :)"
    return render_template('final.html', s=text,resultat=resultat, s2 = t2, nencerts=nencerts)
