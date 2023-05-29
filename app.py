import pandas as pd
import pyqrcode
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import matplotlib.pyplot as plt
from tkinter import *
import matplotlib as mpl


#input
def scelta1():
  nome1=input("Inserire il nome con cui hai salvato i dati del titolo: ")
  nome_tot1=nome1+".csv"
  data1=pd.read_csv(nome_tot1,header=0,parse_dates=["Date"])
  dataFR1=pd.DataFrame(data1)
  while list(dataFR1.columns)!=["Date","Open","High","Low","Close","Adj Close","Volume"]:
    print("Non sono presenti tutti i valori richiesti per l'analisi. Riprova inserendo questa volta i dati corretti!")
    nome1=input("Inserire il nome con cui hai salvato i dati del titolo: ")
    nome_tot1=nome1+".csv"
    data1=pd.read_csv(nome_tot1,header=0,parse_dates=["Date"])
    dataFR1=pd.DataFrame(data1)
  
  titolo1=input("Inserire il nome del titolo di cui sono stati appena inseriti i dati: ")
  
  print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
  colore1=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il primo titolo inserito:")
  while colore1 not in  "red, brown,green,olive,limegreen,blue,navy,darkcyan,lightsteelblue,pink,magenta,darkviolet":
    print("Non hai inserito un colore tra quelli selezionati. Riprova!")
    print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
    colore1=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il primo titolo inserito:")
  
  return dataFR1,titolo1,colore1

def scelta2():
  nome1=input("Inserire il nome con cui hai salvato i dati del primo titolo: ")
  nome_tot1=nome1+".csv"
  data1=pd.read_csv(nome_tot1,header=0,parse_dates=["Date"])
  dataFR1=pd.DataFrame(data1)


  nome2=input("Inserire il nome con cui hai salvato i dati del secondo titolo: ")
  nome_tot2=nome2+".csv"
  data2=pd.read_csv(nome_tot2,header=0,parse_dates=["Date"])
  dataFR2=pd.DataFrame(data2)
  
  condizione=True
  while condizione:
    if dataFR1["Date"].equals(dataFR2["Date"]) and list(dataFR1.columns)==["Date","Open","High","Low","Close","Adj Close","Volume"]:
      condizione=False
    else:
      print("Non sono presenti tutti i valori richiesti per l'analisi oppure non hai inserito lo stesso periodo di tempo per i due titolo.Riprova inserendo questa volta i dati corretti!")
      nome1=input("Inserire il nome con cui hai salvato i dati del primo titolo: ")
      nome_tot1=nome1+".csv"
      data1=pd.read_csv(nome_tot1,header=0,parse_dates=["Date"])
      dataFR1=pd.DataFrame(data1)

      nome2=input("Inserire il nome con cui hai salvato i dati del secondo titolo: ")
      nome_tot2=nome2+".csv"
      data2=pd.read_csv(nome_tot2,header=0,parse_dates=["Date"])
      dataFR2=pd.DataFrame(data2)      
  
  titolo1=input("Inserire il nome del primo titolo: ")
  titolo2=input("Inserire il nome del secondo titolo: ")

  print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
  colore1=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il primo titolo inserito: ")
  print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
  colore2=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il secondo titolo inserito: ")
  condizione=True
  while condizione:
    if colore1 in  "red, brown,green,olive,limegreen,blue,navy,darkcyan,lightsteelblue,pink,magenta,darkviolet" and colore2 in  "red,brown,green,olive,limegreen,blue,navy,darkcyan,lightsteelblue,pink,magenta,darkviolet":
         return dataFR1,dataFR2,titolo1,titolo2,colore1,colore2 
    else:
      print("Non hai inserito un colore tra quelli selezionati. Riprova!")
      print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
      colore1=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il primo titolo inserito: ")
      print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
      colore2=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il secondo titolo inserito: ")


def scelta3():
  nome1=input("Inserire il nome con cui hai salvato i dati del primo titolo: ")
  nome_tot1=nome1+".csv"
  data1=pd.read_csv(nome_tot1,header=0,parse_dates=["Date"])
  dataFR1=pd.DataFrame(data1)

  nome2=input("Inserire il nome con cui hai salvato i dati del secondo titolo: ")
  nome_tot2=nome2+".csv"
  data2=pd.read_csv(nome_tot2,header=0,parse_dates=["Date"])
  dataFR2=pd.DataFrame(data2)

  nome3=input("Inserire il nome con cui hai salvato i dati del terzo titolo: ")
  nome_tot3=nome3+".csv"
  data3=pd.read_csv(nome_tot3,header=0,parse_dates=["Date"])
  dataFR3=pd.DataFrame(data3)

  condizione=True
  while condizione:
    if dataFR1["Date"].equals(dataFR2["Date"]) and dataFR2["Date"].equals(dataFR3["Date"]) and list(dataFR1.columns)==["Date","Open","High","Low","Close","Adj Close","Volume"]:
      condizione=False
    else:
      print("Non sono presenti tutti i valori richiesti per l'analisi oppure non hai inserito lo stesso periodo di tempo per i due titolo.Riprova inserendo questa volta i dati corretti!")
      nome1=input("Inserire il nome con cui hai salvato i dati del primo titolo: ")
      nome_tot1=nome1+".csv"
      data1=pd.read_csv(nome_tot1,header=0,parse_dates=["Date"])
      dataFR1=pd.DataFrame(data1)

      nome2=input("Inserire il nome con cui hai salvato i dati del secondo titolo: ")
      nome_tot2=nome2+".csv"
      data2=pd.read_csv(nome_tot2,header=0,parse_dates=["Date"])
      dataFR2=pd.DataFrame(data2)    

      nome3=input("Inserire il nome con cui hai salvato i dati del terzo titolo: ")
      nome_tot3=nome3+".csv"
      data3=pd.read_csv(nome_tot3,header=0,parse_dates=["Date"])
      dataFR3=pd.DataFrame(data3)
  
  
  titolo1=input("Inserire il nome del primo titolo: ")
  titolo2=input("Inserire il nome del secondo titolo: ")
  titolo3=input("Inserire il nome del terzo titolo: ") 

  print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
  colore1=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il primo titolo inserito: ")
  print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
  colore2=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il secondo titolo inserito: ")
  print("SCELTA COLORE: red, brwon, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
  colore3=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il secondo titolo inserito: ")
  condizione=True
  while condizione:
    if colore1 in  "red,brown,green,olive,limegreen,blue,navy,darkcyan,lightsteelblue,pink,magenta,darkviolet" and colore2 in  "red,brown,green,olive,limegreen,blue,navy,darkcyan,lightsteelblue,pink,magenta,darkviolet" and colore3 in  "red,brown,green,olive,limegreen,blue,navy,darkcyan,lightsteelblue,pink,magenta,darkviolet":
         return dataFR1,dataFR2,dataFR3,titolo1,titolo2,titolo3,colore1,colore2,colore3
    else:
      print("Non hai inserito un colore tra quelli selezionati. Riprova!")
      print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
      colore1=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il primo titolo inserito: ")
      print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
      colore2=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il secondo titolo inserito: ")
      print("SCELTA COLORE: red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet")
      colore3=input("Scegli il colore (tra quelli indicati) per i grafici riguardanti il secondo titolo inserito: ")

#grafici 
def pie(data,colore,titolo):
   
   title="VOLUME"+" "+titolo.upper()
   pie = px.pie(data,title=title, values = data["Volume"],names = "Date",color_discrete_sequence=[colore])
   #pie.show()
   return pie


def grafico_candele(dati,titolo,colore):
#media dei prezzi appartenenti allo stesso giorno,escluso il volume
 prezzigiorno=dati[["Open","High","Low","Close","Adj Close"]]
 mean=prezzigiorno.mean(axis=1) #axis=1 significa che faccio la media per righe
 
 candela=make_subplots(rows=4,cols=1,specs=[[{"rowspan":3}],[None],[None],[{"rowspan":1}]]) #rowspan(raggruppo righe) significa che la prima figura occupa le prime tre righe e la seconda solo l'ultima
 candela.add_trace(go.Line(x=dati["Date"], y=mean, marker_color=colore))
 candela.add_trace(go.Candlestick(x=dati["Date"],open=dati["Open"],high=dati["High"],low=dati["Low"],close=dati["Close"],increasing_line_color= "gold", decreasing_line_color= "black"), row=1, col=1)
 candela.add_trace(go.Bar(x=dati["Date"],y=dati["Volume"], marker_color=colore),row=4,col=1)
 
 candela.update_layout(xaxis_rangeslider_visible=False, showlegend=False) #tolgo la riga di sotto e la legenda
 candela.update_layout(title=titolo.upper())
 #candela.show()
 return candela


def media_mobile1(dati1,colore1):
#media mobile per stimare la direzione corrente di una tendenza. Fornisce un'indicazione puù chiara della tendena generale
 media_mobile1=dati1["Adj Close"].rolling(2).mean() #media mobile considerando due valori alla volta
 dati1["Media Mobile"]=media_mobile1

 fig = px.line(dati1, x="Date",y="Media Mobile",title="MEDIA MOBILE", labels={"x":"Data", "y":"Media Mobile"},color_discrete_sequence=[colore1])
 #fig.show()
 return fig

def media_mobile2(dati1,dati2,colore1,colore2,titolo1,titolo2):
 media_mobile1=dati1["Adj Close"].rolling(2).mean() 
 media_mobile2=dati2["Adj Close"].rolling(2).mean()
 nom_tot1="MEDIA MOBILE"+" "+ titolo1.upper()
 nom_tot2="MEDIA MOBILE"+" "+ titolo2.upper()
 dati1[nom_tot1]=media_mobile1
 dati1[nom_tot2]=media_mobile2

 fig = px.line(dati1, x="Date",y=[nom_tot1,nom_tot2],title="MEDIA MOBILE", labels={"x":"Data", "y":[nom_tot1,nom_tot2],},color_discrete_sequence=[colore1,colore2])
 
 return fig


def media_mobile3(dati1,dati2,dati3,colore1,colore2,colore3,titolo1,titolo2,titolo3):
 media_mobile1=dati1["Adj Close"].rolling(2).mean() 
 media_mobile2=dati2["Adj Close"].rolling(2).mean()
 media_mobile3=dati3["Adj Close"].rolling(2).mean()
 nom_tot1="MEDIA MOBILE"+" "+ titolo1.upper()
 nom_tot2="MEDIA MOBILE"+" "+ titolo2.upper()
 nom_tot3="MEDIA MOBILE"+" "+ titolo3.upper()
 dati1[nom_tot1]=media_mobile1
 dati1[nom_tot2]=media_mobile2
 dati1[nom_tot3]=media_mobile3

 fig = px.line(dati1, x="Date",y=[nom_tot1,nom_tot2,nom_tot3],title="MEDIA MOBILE", labels={"x":"Data", "y":[nom_tot1,nom_tot2,nom_tot3]},color_discrete_sequence=[colore1,colore2,colore3])
 return fig

def rendimenti_percentuali1(dati1,colore1,titolo1):
  #calcolo i rendimenti percentuali
  Adj_Close=dati1["Adj Close"]
  OPEN=dati1["Open"]
  rendimento_assoluto=Adj_Close-OPEN
  rendimento_percentuale=(rendimento_assoluto/OPEN)*100
  tit1="RENDIMENTO (%)"+" "+titolo1.upper()
  dati1[tit1]=rendimento_percentuale

  tot1="OPEN"+" "+titolo1.upper()
  
  fig = make_subplots(rows=1, cols=2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati1["Open"],marker=dict(color=colore1,line=dict(color=colore1,width=8)),name=tot1,orientation="h"), 1, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit1],mode="lines+markers",line_color=colore1,name=tit1), 1, 2)
  fig.update_layout(title="RENDIMENTO PERCENTUALE")
  return fig

def rendimenti_percentuali2(dati1,dati2,colore1,colore2,titolo1,titolo2):
  Adj_Close=dati1["Adj Close"]
  OPEN=dati1["Open"]
  rendimento_assoluto1=Adj_Close-OPEN
  rendimento_percentuale1=(rendimento_assoluto1/OPEN)*100
  tit1="RENDIMENTO (%)"+" "+titolo1.upper()
  dati1[tit1]=rendimento_percentuale1

  Adj_Close2=dati2["Adj Close"]
  OPEN2=dati2["Open"]
  rendimento_assoluto2=Adj_Close2-OPEN2
  rendimento_percentuale2=(rendimento_assoluto2/OPEN)*100
  tit2="RENDIMENTO (%)"+" "+titolo2.upper()
  dati1[tit2]=rendimento_percentuale2

  tot1="OPEN"+" "+titolo1.upper()
  tot2="OPEN"+" "+titolo2.upper()

  fig = make_subplots(rows=2, cols=2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati1["Open"],marker=dict(color=colore1,line=dict(color=colore1,width=8)),name=tot1,orientation="h"), 1, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit1],mode="lines+markers",line_color=colore1,name=tit1), 1, 2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati2["Open"],marker=dict(color=colore2,line=dict(color=colore2,width=8)),name=tot2,orientation="h"), 2, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit2],mode="lines+markers",line_color=colore2,name=tit2), 2, 2)
  fig.update_layout(title="RENDIMENTO PERCENTUALE")
  #fig.show()
  return fig


def rendimenti_percentuali3(dati1,dati2,dati3,colore1,colore2,colore3,titolo1,titolo2,titolo3):
  Adj_Close=dati1["Adj Close"]
  OPEN=dati1["Open"]
  rendimento_assoluto1=Adj_Close-OPEN
  rendimento_percentuale1=(rendimento_assoluto1/OPEN)*100
  tit1="RENDIMENTO (%)"+" "+titolo1.upper
  dati1["Rendimento1(%)"]=rendimento_percentuale1

  Adj_Close2=dati2["Adj Close"]
  OPEN2=dati2["Open"]
  rendimento_assoluto2=Adj_Close2-OPEN2
  rendimento_percentuale2=(rendimento_assoluto2/OPEN2)*100
  tit2="RENDIMENTO (%)"+" "+titolo2.upper()
  dati1["Rendimento2(%)"]=rendimento_percentuale2
  
  Adj_Close3=dati3["Adj Close"]
  OPEN3=dati3["Open"]
  rendimento_assoluto3=Adj_Close3-OPEN3
  rendimento_percentuale3=(rendimento_assoluto3/OPEN3)*100
  tit3="RENDIMENTO (%)"+" "+titolo3.upper()
  dati1["Rendimento3(%)"]=rendimento_percentuale3

  tot1="OPEN"+" "+titolo1.upper()
  tot2="OPEN"+" "+titolo2.upper()
  tot3="OPEN"+" "+titolo2.upper()

  fig = make_subplots(rows=3, cols=2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati1["Open"],marker=dict(color=colore1,line=dict(color=colore1,width=8)),name=tot1,orientation="h"), 1, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit1],mode="lines+markers",line_color=colore1,name=tit1), 1, 2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati2["Open"],marker=dict(color=colore2,line=dict(color=colore2,width=8)),name=tot2,orientation="h"), 2, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit2],mode="lines+markers",line_color=colore2,name=tit2), 2, 2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati3["Open"],marker=dict(color=colore2,line=dict(color=colore2,width=8)),name=tot3,orientation="h"), 3, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit3],mode="lines+markers",line_color=colore2,name=tit2), 3, 2)
  fig.update_layout(title="RENDIMENTO PERCENTUALE")
  #fig.show()
  return fig


def OBV(dati1,colore1):
#L'indicatore tecnico On Balance Volume (OBV) è un indicatore di analisi tecnica che mette in relazione il volume con le variazioni di prezzo.il concetto di questo indicatore si basa sull'idea che quando c'è un volume di trading, il prezzo prima o poi ne risentirà. Il concetto di questo indicatore si basa sull'idea che quando c'è un volume di trading, il prezzo prima o poi ne risentirà. 
#If the close is above the prior close then: Current OBC = Previous OBC + Current Volume, If the closing price is below the prior close price then: Current OBV = Previous OBV - Current Volume, If the closing prices equals the prior close price then: Current OBV = Previous OBV (no change)
 OBV=[0]
 close=dati1["Close"]
 volume=dati1["Volume"]
 for i in range(1,len(close)):
   obv=0
   if close[i] > close[i-1]:
     obv = volume[i]+ obv
     OBV.append(obv)
   elif close[i] < close[i-1]:
     obv = obv - volume[i]
     OBV.append(obv)
   else:
      obv = obv
      OBV.append(obv)
 dati1["OBV"]=OBV #aggiungo la lista OBV al df

 title1="OBV"

 bar = go.Figure()
 bar.add_trace(go.Bar(y=dati1["OBV"],x=dati1["Date"],name=title1,marker=dict(color=colore1,line=dict(width=3))))
 bar.update_layout(title="OBV",barmode="group")
 #bar.show() 
 return bar

def OBV2(dati1,dati2,colore1,colore2,titolo1,titolo2):
 OBV=[0]
 close=dati1["Close"]
 volume=dati1["Volume"]
 for i in range(1,len(close)):
   obv=0
   if close[i] > close[i-1]:
     obv = volume[i]+ obv
     OBV.append(obv)
   elif close[i] < close[i-1]:
     obv = obv - volume[i]
     OBV.append(obv)
   else:
      obv = obv
      OBV.append(obv)
 dati1["OBV"]=OBV #aggiungo la lista OBV al df

 OBV2=[0]
 close2=dati2["Close"]
 volume2=dati2["Volume"]
 for i in range(1,len(close2)):
   obv2=0
   if close2[i] > close2[i-1]:
     obv2 = volume2[i]+ obv2
     OBV2.append(obv2)
   elif close2[i] < close2[i-1]:
     obv2 = obv2 - volume2[i]
     OBV2.append(obv2)
   else:
      obv2 = obv2
      OBV2.append(obv2)
 dati1["OBV2"]=OBV2

 title1="OBV"+" "+titolo1.upper()
 title2="OBV"+" "+titolo2.upper()
 
 bar = go.Figure()
 bar.add_trace(go.Bar(y=dati1["OBV"],x=dati1["Date"],name=title1,marker=dict(color=colore1,line=dict(width=3))))
 bar.add_trace(go.Bar(y=dati1["OBV2"],x=dati1["Date"],name=title2,marker=dict(color=colore2,line=dict( width=3))))
 bar.update_layout(title="OBV",barmode="group")
 #bar.show() 
 return bar
 
def OBV3(dati1,dati2,dati3,colore1,colore2,colore3,titolo1,titolo2,titolo3):
 OBV=[0]
 close=dati1["Close"]
 volume=dati1["Volume"]
 for i in range(1,len(close)):
   obv=0
   if close[i] > close[i-1]:
     obv = volume[i]+ obv
     OBV.append(obv)
   elif close[i] < close[i-1]:
     obv = obv - volume[i]
     OBV.append(obv)
   else:
      obv = obv
      OBV.append(obv)
 dati1["OBV"]=OBV 

 OBV2=[0]
 close2=dati2["Close"]
 volume2=dati2["Volume"]
 for i in range(1,len(close2)):
   obv2=0
   if close2[i] > close2[i-1]:
     obv2 = volume2[i]+ obv2
     OBV2.append(obv2)
   elif close2[i] < close2[i-1]:
     obv2 = obv2 - volume2[i]
     OBV2.append(obv2)
   else:
      obv2 = obv2
      OBV2.append(obv2)
 dati1["OBV2"]=OBV2

 OBV3=[0]
 close3=dati3["Close"]
 volume3=dati3["Volume"]
 for i in range(1,len(close3)):
   obv3=0
   if close3[i] > close3[i-1]:
     obv3 = volume3[i]+ obv3
     OBV3.append(obv3)
   elif close3[i] < close3[i-1]:
     obv3 = obv3 - volume3[i]
     OBV3.append(obv3)
   else:
      obv3 = obv3
      OBV3.append(obv3)
 dati1["OBV3"]=OBV3

 title1="OBV"+" "+titolo1.upper()
 title2="OBV"+" "+titolo2.upper()
 title3="OBV"+" "+titolo3.upper()
 

 bar = go.Figure()
 bar.add_trace(go.Bar(y=dati1["OBV"],x=dati1["Date"],name=title1,marker=dict(color=colore1,line=dict(width=3))))
 bar.add_trace(go.Bar(y=dati1["OBV2"],x=dati1["Date"],name=title2,marker=dict(color=colore2,line=dict( width=3))))
 bar.add_trace(go.Bar(y=dati1["OBV3"],x=dati1["Date"],name=title3,marker=dict(color=colore3,line=dict( width=3))))
 bar.update_layout(title="OBV",barmode="group")
 #bar.show()  
 return bar 


#La volatilità è la misura della quantità e la velocità con cui il prezzo si muove verso l'alto e verso il basso,le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato
def dispersione1(data,titolo,colore):

  close_mean=data["Close"].mean()
  data["Media chiusura"]=close_mean
  nome="CLOSE"+" "+titolo.upper()

  fig, ax = plt.subplots(figsize=(8,6))
  
  ax.plot(data["Date"], data["Close"],label="Close",color=colore,marker="o", ms = 5, mfc = "k") 
  ax.plot(data["Date"], data["Media chiusura"],label="Media chiusura",color=colore, linestyle="--") 
  ax.set_xticks(data['Date'])
  ax.set_xticklabels(data["Date"],rotation=90)
  ax.patch.set_edgecolor("k")
  ax.patch.set_linewidth(3)
  ax.set_title(nome) 
  ax.grid()
  ax.legend()
  plt.style.use('ggplot')
  mpl.rc('lines', linewidth=4, linestyle='-.')
  
  plt.show()
  return fig

def dispersione2(data1,titolo1,colore1,data2,titolo2,colore2):

  close_mean=data1["Close"].mean()
  nome1="Media chiusura"+" "+titolo1
  close1="Close"+" "+titolo1
  data1[nome1]=close_mean

  close_mean2=data2["Close"].mean()
  nome2="Media chiusura"+" "+titolo2
  close2="Close"+" "+titolo2
  data2[nome2]=close_mean2

  
  fig=plt.figure(figsize=(8,6))

  ax=plt.subplot(2,1,1) #con subplot(x,y,z) vado a stampare i grafici in matrice. x indica il nr di righe,y di colonne e z in quale posizione si trova il singolo grafico
  ax.plot(data1["Date"], data1[nome1], label=nome1, color=colore1, linestyle="--")
  ax.plot(data1["Date"], data1["Close"],label=close1, marker="o",color=colore1, ms = 5, mfc = "k")  
  ax.set_title(titolo1.upper())
  ax.patch.set_edgecolor("k")
  ax.patch.set_linewidth(3)
  ax.get_xaxis().set_visible(False) #lo nascondo
  
  ax=plt.subplot(2,1,2)
  ax.plot(data2["Date"], data2[nome2],label=nome2,color=colore2, linestyle="--")
  ax.plot(data2["Date"], data2["Close"],label=close2, marker="o",color=colore2, ms = 5, mfc = "k")  
  ax.set_title(titolo2.upper())
  ax.set_xticks(data2['Date'])
  ax.set_xticklabels(data2["Date"],rotation=90)
  ax.patch.set_edgecolor("k")
  ax.patch.set_linewidth(3)

  ax.set_title("DISPERSIONE PREZZI DI CHIUSURA DALLA MEDIA") 
  ax.legend()
  ax.grid()
  plt.tight_layout()
  plt.style.use('ggplot')
  mpl.rc('lines', linewidth=4, linestyle='-.')

  plt.show()
  return fig

def dispersione3(data1,titolo1,colore1,data2,titolo2,colore2,data3,titolo3,colore3):

  close_mean=data1["Close"].mean()
  nome1="Media chiusura"+" "+titolo1
  close1="Close"+" "+titolo1
  data1[nome1]=close_mean

  close_mean2=data2["Close"].mean()
  nome2="Media chiusura"+" "+titolo2
  close2="Close"+" "+titolo2
  data2[nome2]=close_mean2
  
  close_mean3=data3["Close"].mean()
  nome3="Media chiusura"+" "+titolo3
  close3="Close"+" "+titolo3
  data3[nome3]=close_mean3

  
  fig=plt.figure(figsize=(8,6))

  ax=plt.subplots(3,1,1) 
  ax.plot(data1["Date"], data1[nome1],label=nome1,color=colore1, linestyle="--")
  ax.plot(data1["Date"], data1["Close"],label=close1, marker="o",color=colore1, ms = 5, mfc = "k")  
  ax.set_title(titolo1.upper())
  ax.patch.set_edgecolor("k")
  ax.patch.set_linewidth(3)
  ax.get_xaxis().set_visible(False)
  
  ax=plt.subplots(3,1,2)
  ax.plot(data2["Date"], data2[nome2],label=nome2,color=colore2, linestyle="--")
  ax.plot(data2["Date"], data2["Close"],label=close2, marker="o",color=colore2, ms = 5, mfc = "k")  
  ax.set_title(titolo2.upper())
  ax.patch.set_edgecolor("k")
  ax.patch.set_linewidth(3)
  ax.get_xaxis().set_visible(False)
  
  ax=plt.subplots(3,1,3)
  ax.plot(data3["Date"], data3[nome3],label=nome3,color=colore3, linestyle="--")
  ax.plot(data3["Date"], data3["Close"],label=nome3, marker="o",color=colore3, ms = 5, mfc = "k")  
  ax.set_title(titolo3.upper())
  ax.set_xlabel("Data")
  ax.set_xticks(data3['Date'])
  ax.set_xticklabels(data3["Date"],rotation=90)
  ax.patch.set_edgecolor("k")
  ax.patch.set_linewidth(3)

  ax.set_title("DISPERSIONE PREZZI DI CHIUSURA DALLA MEDIA")  
  ax.legend()
  ax.grid()
  plt.tight_layout()
  plt.style.use('ggplot')
  mpl.rc('lines', linewidth=4, linestyle='-.')
  plt.show()
  return fig
 

def qr_code():
  
  qr=pyqrcode.create("https://it.finance.yahoo.com/")
  qread=qr.terminal("black")
  
  return qread


#web site contruction
import streamlit as st
import numpy as np 
import plost
from PIL import Image

# Page setting
st.set_page_config (layout="wide")
with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        st.title('Data Analysis')
        #Adding a sidebar to the app
        st.sidebar.title("Welcome!") 
        #case decision
        num=input("Inserisci il numero di titoli che vuoi confrontare (minimo 1, massimo 3): ")
        while num!="1" and num!="2" and num!="3":
            print("Inserimento non coerente. Ricorda devi inserire un valore compreso tra 1 e 3.")
            num=input("Inserisci il numero di titoli che vuoi confrontare: ")
        if num=="1":
            dataFR1,titolo1,colore1=scelta1()
            with st.container():
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              dataFrame=pd.DataFrame(
                dataFR1,
                columns=['Open','High','Close','Adj Close'])
              st.area_chart(dataFrame)
              st.write(media_mobile1(dataFR1,colore1))
              st.pyplot(dispersione1(dataFR1,titolo1,colore1))
              st.write(pie(dataFR1,colore1,titolo1))
              st.write(OBV(dataFR1,colore1))
              st.write(rendimenti_percentuali1(dataFR1,colore1,titolo1))
            
              with st.container():
                left_column, right_column=st.columns(2)
                with left_column:
                  #qr=qr_code()
                  st.write(qr_code())

        elif num=="2":
            dataFR1,dataFR2, titolo1, titolo2, colore1, colore2= scelta2()
            with st.container():
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              st.write(grafico_candele(dataFR2,titolo2,colore2))
              st.write(media_mobile2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.pyplot(dispersione2(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2))
              with st.container():
                left_column, right_column=st.columns(2)
                with left_column:
                  st.write(pie(dataFR1,colore1,titolo1))
                  with right_column:
                    st.write(pie(dataFR2,colore2,titolo2))
              st.write(OBV2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.write(rendimenti_percentuali2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              #qr=qr_code()
              st.write(qr_code())

        elif num=="3":
            dataFR1,dataFR2,dataFR3,titolo1,titolo2,titolo3,colore1,colore2,colore3=scelta3()
            with st.container():
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              st.write(grafico_candele(dataFR2,titolo2,colore2))
              st.write(grafico_candele(dataFR3,titolo3,colore3))
              st.write(media_mobile3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
              st.pyplot(dispersione3(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2,dataFR3,titolo3,colore3))
              with st.container():
                 col1, col2, col3=st.columns(3)
                 with col1:
                  st.write(pie(dataFR1,colore1,titolo1))
                 with col2:
                  st.write(pie(dataFR2,colore2,titolo2))
                 with col3:
                  st.write(pie(dataFR3,colore3,titolo3))
              st.write(OBV3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
              st.write(rendimenti_percentuali3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
              st.write(qr_code()) 
        # df=pd.DataFrame(df1)
        # print(df)
