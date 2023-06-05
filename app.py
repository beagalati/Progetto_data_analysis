import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image

#file
def errore1():
      st.sidebar.write("Poiché non sono stati inseriti i valori corretti, sono stati forniti di default i dati mensili dell'anno 2022 del titolo 'FERRARI'.")
      nome_tot1="FERRARI.csv"
      data1=pd.read_csv(nome_tot1,parse_dates=["Date"])
      dataFR1=pd.DataFrame(data1)
      colore="red"
      titolo="FERRARI"
      return dataFR1,colore,titolo

def errore2():
    st.sidebar.write("Poiché non sono stati inseriti tutti i valori giusti, sono stati forniti di default i dati mensili dell'anno 2022 dei titoli 'FERRARI' e 'FORD'.")
    nome_tot1="FERRARI.csv"
    data1=pd.read_csv(nome_tot1,parse_dates=["Date"])
    dataFR1=pd.DataFrame(data1)
    colore1="red"
    titolo1="FERRARI"
    nome_tot2="FORD.csv"
    data2=pd.read_csv(nome_tot2,parse_dates=["Date"])
    dataFR2=pd.DataFrame(data2)
    colore2="blue"
    titolo2="FORD"
    return dataFR1,colore1,titolo1,dataFR2,colore2,titolo2

def errore3():
    st.sidebar.write("Poiché non sono stati inseriti tutti i valori giusti, sono stati forniti di default i dati mensili dell'anno 2022 dei titoli 'FERRARI', 'FORD' e 'ALFA ROMEO'.")
    nome_tot1="FERRARI.csv"
    data1=pd.read_csv(nome_tot1,parse_dates=["Date"])
    dataFR1=pd.DataFrame(data1)
    colore1="red"
    titolo1="FERRARI"
    nome_tot2="FORD.csv"
    data2=pd.read_csv(nome_tot2,parse_dates=["Date"])
    dataFR2=pd.DataFrame(data2)
    colore2="blue"
    titolo2="FORD"
    nome_tot3="ALFA_ROMEO.csv"
    data3=pd.read_csv(nome_tot3,parse_dates=["Date"])
    dataFR3=pd.DataFrame(data3)
    colore3="darkviolet"
    titolo3="ALFA ROMEO"
    return dataFR1,colore1,titolo1,dataFR2,colore2,titolo2,dataFR3,colore3,titolo3
  

def scelta1file(dati,titolo,colore):
  data1=pd.read_csv(dati,parse_dates=["Date"])
  dataFR1=pd.DataFrame(data1)
      
  check=True
  colori=True

  if list(dataFR1.columns)!=["Date","Open","High","Low","Close","Adj Close","Volume"]:
    check=False
    st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi dei dati nel file.")

  if colore not in ["red","brown","green","olive","limegreen","blue","darkcyan","lightsteelblue","pink","magenta","darkviolet"]:
    colori=False
    st.sidebar.write("Non hai inserito un colore tra quelli selezionati.")

  return check,colori,dataFR1,colore,titolo

def scelta2file(dati1,titolo1,colore1,dati2,titolo2,colore2):
  data1=pd.read_csv(dati1,parse_dates=["Date"])
  dataFR1=pd.DataFrame(data1)

  data2=pd.read_csv(dati2,parse_dates=["Date"])
  dataFR2=pd.DataFrame(data2)

  check1=True
  check2=True
  equal=True
  colori1=True
  colori2=True

   #sono presenti lo stesso numero di dati (equals)
  if list(dataFR1.columns)!=["Date","Open","High","Low","Close","Adj Close","Volume"]:
    check1=False
    st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi nel primo file. Ricorda devono essere presenti i valori relativi a 'Date,Open,High,Low,Clos,Adj Close,Volume'")
  if list(dataFR2.columns)!=["Date","Open","High","Low","Close","Adj Close","Volume"]:
    check2=False
    st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi nel secondo file. Ricorda devono essere presenti i valori relativi a 'Date,Open,High,Low,Clos,Adj Close,Volume'")

  if dataFR1["Date"].equals(dataFR2["Date"])=="False":
    equal=False
    st.sidebar.write("Non sono presenti lo stesso numero di valori nei due file")
  
  if colore1 not in ["red","brown","green","olive","limegreen","blue","darkcyan","lightsteelblue","pink","magenta","darkviolet"]:
    colori1=False
    st.sidebar.write("Il primo colore non è tra quelli selezionati." )
  if colore2 not in  ["red","brown","green","olive","limegreen","blue","darkcyan","lightsteelblue","pink","magenta","darkviolet"]:
    colori2=False
    st.sidebar.write("Il secondo colore non è tra quelli selezionati." )
  
  return check1,check2,equal,colori1,colori2,dataFR1,colore1,titolo1,dataFR2,colore2,titolo2 


def scelta3file(dati1,titolo1,colore1,dati2,titolo2,colore2,dati3,titolo3,colore3):
  data1=pd.read_csv(dati1,parse_dates=["Date"])
  dataFR1=pd.DataFrame(data1)

  data2=pd.read_csv(dati2,parse_dates=["Date"])
  dataFR2=pd.DataFrame(data2)

  data3=pd.read_csv(dati3,parse_dates=["Date"])
  dataFR3=pd.DataFrame(data3)

  check1=True
  check2=True
  check3=True
  equal1=True
  equal2=True
  equal3=True
  colori1=True
  colori2=True
  colori3=True

  if list(dataFR1.columns)!=["Date","Open","High","Low","Close","Adj Close","Volume"]:
    check1==False
    st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi nel primo file. Ricorda devono essere presenti i valori relativi a 'Date,Open,High,Low,Clos,Adj Close,Volume'")
  if list(dataFR2.columns)!=["Date","Open","High","Low","Close","Adj Close","Volume"]:
    check2==False
    st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi nel secondo file. Ricorda devono essere presenti i valori relativi a 'Date,Open,High,Low,Clos,Adj Close,Volume'")
  if list(dataFR3.columns)!=["Date","Open","High","Low","Close","Adj Close","Volume"]:
   check3==False
   st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi nel terzo file. Ricorda devono essere presenti i valori relativi a 'Date,Open,High,Low,Clos,Adj Close,Volume'")

  if dataFR1["Date"].equals(dataFR2["Date"])=="False":
    equal1=False
    st.sidebar.write("Non sono presenti lo stesso numero di valori nei primi due file")
  if dataFR2["Date"].equals(dataFR3["Date"])=="False":
    equal2=False
    st.sidebar.write("Non sono presenti lo stesso numero di valori negli ultimi due file")
  if dataFR1["Date"].equals(dataFR3["Date"])=="False":
    equal3=False
    st.sidebar.write("Non sono presenti lo stesso numero di valori nel primo e nel terzo file")
  
  if colore1 not in ["red","brown","green","olive","limegreen","blue","darkcyan","lightsteelblue","pink","magenta","darkviolet"]:
    colori1=False
    st.sidebar.write("Il primo colore non è tra quelli selezionati." )
  if colore2 not in ["red","brown","green","olive","limegreen","blue","darkcyan","lightsteelblue","pink","magenta","darkviolet"]:
    colori2=False
    st.sidebar.write("Il secondo colore non è tra quelli selezionati." )
  if colore3 not in ["red","brown","green","olive","limegreen","blue","darkcyan","lightsteelblue","pink","magenta","darkviolet"]:
    colori3=False
    st.sidebar.write("Il terzo colore non è tra quelli selezionati." )
 
  return check1, check2, check3, equal1, equal2, equal3, colori1, colori2, colori3,dataFR1,colore1,titolo1,dataFR2,colore2,titolo2,dataFR3,colore3,titolo3
  
 
  
#input
def scelta1(dati1):
  condizione=True
  while condizione:
    data1=pd.read_csv(dati1,parse_dates=["Date"])
    dataFR1=pd.DataFrame(data1)
    if list(dataFR1.columns)!=["Date","Open","High","Low","Close","Adj Close","Volume"]:
      st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi. Riprova, eliminando il file caricato e inserendo questa volta quello contenente i dati corretti!")
    else:
      condizione=False

  
  st.sidebar.subheader("NOME TITOLO")
  titolo1=st.sidebar.text_input("Inserisci il nome del titolo di cui sono stati appena inseriti i dati: ")
  
  st.sidebar.subheader("COLORE")
  colore1 = st.sidebar.color_picker("Scegli un colore per i grafici riguardanti il titolo", "#F90034")
  
  return dataFR1,titolo1,colore1

def scelta2(dati1,dati2):
  condizione=True
  while condizione:
    data1=pd.read_csv(dati1,parse_dates=["Date"])
    dataFR1=pd.DataFrame(data1)
    data2=pd.read_csv(dati2,parse_dates=["Date"])
    dataFR2=pd.DataFrame(data2)
    if dataFR1["Date"].equals(dataFR2["Date"]) and list(dataFR1.columns)==["Date","Open","High","Low","Close","Adj Close","Volume"]:
      condizione=False
    else:
      st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi oppure non hai inserito lo stesso periodo di tempo per i due titoli. Riprova, eliminando i file caricati e inserendo questa volta quelli contenenti i dati corretti!")

  st.sidebar.subheader("NOMI TITOLI")
  titolo1=st.sidebar.text_input("Inserisci il nome del primo titolo di cui sono stati appena inseriti i dati: ")
  titolo2=st.sidebar.text_input("Inserisci il nome del secondo titolo di cui sono stati appena inseriti i dati: ")
  
  st.sidebar.subheader("COLORI")
  colore1 = st.sidebar.color_picker("Scegli un colore per i grafici riguardanti il primo titolo", "#F90034")
  colore2 = st.sidebar.color_picker("Scegli un colore per i grafici riguardanti il secondo titolo", "#F90034")
  
  return dataFR1,dataFR2,titolo1,titolo2,colore1,colore2

def scelta3(dati1,dati2,dati3):
  condizione=True
  while condizione:
    data1=pd.read_csv(dati1,parse_dates=["Date"])
    dataFR1=pd.DataFrame(data1)
    data2=pd.read_csv(dati2,parse_dates=["Date"])
    dataFR2=pd.DataFrame(data2)
    data3=pd.read_csv(dati3,parse_dates=["Date"])
    dataFR3=pd.DataFrame(data3)
    if dataFR1["Date"].equals(dataFR2["Date"]) and dataFR2["Date"].equals(dataFR3["Date"]) and list(dataFR1.columns)==["Date","Open","High","Low","Close","Adj Close","Volume"]:
      condizione=False
    else:
      st.sidebar.write("Non sono presenti tutti i valori richiesti per l'analisi oppure non hai inserito lo stesso periodo di tempo per i due titoli. Riprova, eliminando i file caricati e inserendo questa volta quelli contenenti i dati corretti!")
  
  
  st.sidebar.subheader("NOMI TITOLI")
  titolo1=st.sidebar.text_input("Inserisci il nome del primo titolo di cui sono stati appena inseriti i dati: ")
  titolo2=st.sidebar.text_input("Inserisci il nome del secondo titolo di cui sono stati appena inseriti i dati: ")
  titolo3=st.sidebar.text_input("Inserisci il nome del terzo titolo di cui sono stati appena inseriti i dati: ")
  
  st.sidebar.subheader("COLORI")
  colore1 = st.sidebar.color_picker("Scegli un colore per i grafici riguardanti il primo titolo", "#F90034")
  colore2 = st.sidebar.color_picker("Scegli un colore per i grafici riguardanti il secondo titolo", "#F90034")
  colore3 = st.sidebar.color_picker("Scegli un colore per i grafici riguardanti il terzo titolo", "#F90034")
  
  return dataFR1,dataFR2,dataFR3,titolo1,titolo2,titolo3,colore1,colore2,colore3 
   
    

#grafici
def pie(data,colore,titolo):
   
   title="VOLUME"+" "+titolo.upper()
   pie = px.pie(data,title=title, values = data["Volume"],names = "Date",color_discrete_sequence=[colore], width=400)
   #pie.show()
   return pie

#media dei prezzi appartenenti allo stesso giorno,escluso il volume
def grafico_candele(dati,titolo,colore):
  prezzigiorno=dati[["Open","High","Low","Close","Adj Close"]]
  mean=prezzigiorno.mean(axis=1) #axis=1 significa che faccio la media per righe
 
  candela=make_subplots(rows=4,cols=1,specs=[[{"rowspan":3}],[None],[None],[{"rowspan":1}]]) #rowspan(raggruppo righe) significa che la prima figura occupa le prime tre righe e la seconda solo l'ultima
  candela.add_trace(go.Line(x=dati["Date"], y=mean, marker_color=colore))
  candela.add_trace(go.Candlestick(x=dati["Date"],open=dati["Open"],high=dati["High"],low=dati["Low"],close=dati["Close"],increasing_line_color= "gold", decreasing_line_color= "tan"), row=1, col=1)
  candela.add_trace(go.Bar(x=dati["Date"],y=dati["Volume"], marker_color=colore),row=4,col=1)
 
  candela.update_layout(xaxis_rangeslider_visible=False, showlegend=False) #tolgo la riga di sotto e la legenda
  candela.update_layout(title=titolo.upper())
  return candela


def media_mobile1(dati1,colore1):
  media_mobile1=dati1["Adj Close"].rolling(2).mean() #media mobile considerando due valori alla volta
  dati1["Media Mobile"]=media_mobile1

  fig = px.line(dati1, x="Date",y="Media Mobile",title="MEDIA MOBILE DEL PREZZO DI CHIUSURA AGGIUSTATO", labels={"x":"Data", "y":"Media Mobile"},color_discrete_sequence=[colore1])
  return fig

def media_mobile2(dati1,dati2,colore1,colore2,titolo1,titolo2):
  media_mobile1=dati1["Adj Close"].rolling(2).mean() 
  media_mobile2=dati2["Adj Close"].rolling(2).mean()
  nom_tot1="MEDIA MOBILE"+" "+ titolo1.upper()
  nom_tot2="MEDIA MOBILE"+" "+ titolo2.upper()
  dati1[nom_tot1]=media_mobile1
  dati1[nom_tot2]=media_mobile2

  fig = px.line(dati1, x="Date",y=[nom_tot1,nom_tot2],title="MEDIA MOBILE DEL PREZZO DI CHIUSURA AGGIUSTATO", labels={"x":"Data", "y":[nom_tot1,nom_tot2]},color_discrete_sequence=[colore1,colore2])
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

  fig = px.line(dati1, x="Date",y=[nom_tot1,nom_tot2,nom_tot3],title="MEDIA MOBILE DEL PREZZO DI CHIUSURA AGGIUSTATO", labels={"x":"Data", "y":[nom_tot1,nom_tot2,nom_tot3]},color_discrete_sequence=[colore1,colore2,colore3])
  return fig


def rendimenti_percentuali1(dati1,colore1,titolo1):
  #calcolo i rendimenti percentuali
  ADJ_CLOSE=dati1["Adj Close"]
  OPEN=dati1["Open"]
  rendimento_assoluto=ADJ_CLOSE-OPEN
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
  ADJ_CLOSE=dati1["Adj Close"]
  OPEN=dati1["Open"]
  rendimento_assoluto1=ADJ_CLOSE-OPEN
  rendimento_percentuale1=(rendimento_assoluto1/OPEN)*100
  tit1="RENDIMENTO (%)"+" "+titolo1.upper()
  dati1[tit1]=rendimento_percentuale1

  ADJ_CLOSE2=dati2["Adj Close"]
  OPEN2=dati2["Open"]
  rendimento_assoluto2=ADJ_CLOSE2-OPEN2
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
  return fig
  

def rendimenti_percentuali3(dati1,dati2,dati3,colore1,colore2,colore3,titolo1,titolo2,titolo3):
  ADJ_CLOSE=dati1["Adj Close"]
  OPEN=dati1["Open"]
  rendimento_assoluto1=ADJ_CLOSE-OPEN
  rendimento_percentuale1=(rendimento_assoluto1/OPEN)*100
  tit1="RENDIMENTO (%)"+" "+titolo1.upper()
  dati1[tit1]=rendimento_percentuale1

  ADJ_CLOSE2=dati2["Adj Close"]
  OPEN2=dati2["Open"]
  rendimento_assoluto2=ADJ_CLOSE2-OPEN2
  rendimento_percentuale2=(rendimento_assoluto2/OPEN2)*100
  tit2="RENDIMENTO (%)"+" "+titolo2.upper()
  dati1[tit2]=rendimento_percentuale2
  
  ADJ_CLOSE3=dati3["Adj Close"]
  OPEN3=dati3["Open"]
  rendimento_assoluto3=ADJ_CLOSE3-OPEN3
  rendimento_percentuale3=(rendimento_assoluto3/OPEN3)*100
  tit3="RENDIMENTO (%)"+" "+titolo3.upper()
  dati1[tit3]=rendimento_percentuale3

  tot1="OPEN"+" "+titolo1.upper()
  tot2="OPEN"+" "+titolo2.upper()
  tot3="OPEN"+" "+titolo3.upper()

  fig = make_subplots(rows=3, cols=2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati1["Open"],marker=dict(color=colore1,line=dict(color=colore1,width=8)),name=tot1,orientation="h"), 1, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit1],mode="lines+markers",line_color=colore1,name=tit1), 1, 2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati2["Open"],marker=dict(color=colore2,line=dict(color=colore2,width=8)),name=tot2,orientation="h"), 2, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit2],mode="lines+markers",line_color=colore2,name=tit2), 2, 2)
  fig.append_trace(go.Bar(y=dati1["Date"],x=dati3["Open"],marker=dict(color=colore3,line=dict(color=colore3,width=8)),name=tot3,orientation="h"), 3, 1)
  fig.append_trace(go.Scatter(x=dati1["Date"], y=dati1[tit3],mode="lines+markers",line_color=colore3,name=tit3), 3, 2)
  fig.update_layout(title="RENDIMENTO PERCENTUALE")
  return fig

#If the close is above the prior close then: Current OBC = Previous OBC + Current Volume, If the closing price is below the prior close price then: Current OBV = Previous OBV - Current Volume, If the closing prices equals the prior close price then: Current OBV = Previous OBV (no change)
def OBV(dati1,colore1):
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
  return bar 

def dispersione1(data,titolo,colore):
  close_mean=data["Close"].mean()
  nome="MEDIA CLOSE"+" "+titolo.upper()
  data[nome]=close_mean

  fig, ax = plt.subplots(figsize=(8,6))
  
  ax.plot(data["Date"], data[nome],label="MEDIA CLOSE",color=colore, linestyle="--") 
  ax.plot(data["Date"], data["Close"],label="CLOSE",color=colore,marker="o", ms = 5, mfc = "k") 
  ax.set_xlabel("Data")
  ax.set_xticklabels(data["Date"],rotation=90)
  ax.patch.set_edgecolor("k")
  ax.patch.set_linewidth(3)
  ax.set_title("VOLATILITÀ DEL PREZZO DI CHIUSURA") 
  ax.legend()
  #plt.show()
  return fig

def dispersione2(data1,titolo1,colore1,data2,titolo2,colore2):
  close_mean=data1["Close"].mean()
  nome1="MEDIA CLOSE"+" "+titolo1.upper()
  close1="CLOSE"+" "+titolo1.upper()
  data1[nome1]=close_mean

  close_mean2=data2["Close"].mean()
  nome2="MEDIA CLOSE"+" "+titolo2.upper()
  close2="CLOSE"+" "+titolo2.upper()
  data2[nome2]=close_mean2

  fig=plt.figure(figsize=(8,6))

  ax1=plt.subplot(2,1,1) #con subplot(x,y,z) vado a stampare i grafici in matrice. x indica il nr di righe,y di colonne e z in quale posizione si trova il singolo grafico
  ax1.plot(data1["Date"], data1[nome1], label=nome1, color=colore1, linestyle="--")
  ax1.plot(data1["Date"], data1["Close"],label=close1, marker="o",color=colore1, ms = 5, mfc = "k")  
  ax1.patch.set_edgecolor("k")
  ax1.patch.set_linewidth(3)
  ax1.get_xaxis().set_visible(False) #lo nascondo
  ax1.legend()
  
  ax2=plt.subplot(2,1,2)
  ax2.plot(data2["Date"], data2[nome2],label=nome2,color=colore2, linestyle="--")
  ax2.plot(data2["Date"], data2["Close"],label=close2, marker="o",color=colore2, ms = 5, mfc = "k")  
  ax2.set_xticklabels(data2["Date"],rotation=90)
  ax2.patch.set_edgecolor("k")
  ax2.patch.set_linewidth(3)
  ax2.legend()

  ax1.set_title("VOLATILITÀ DEL PREZZO DI CHIUSURA") 
  plt.tight_layout()
  plt.show()
  return fig

def dispersione3(data1,titolo1,colore1,data2,titolo2,colore2,data3,titolo3,colore3):
  close_mean=data1["Close"].mean()
  nome1="MEDIA CLOSE"+" "+titolo1.upper()
  close1="CLOSE"+" "+titolo1.upper()
  data1[nome1]=close_mean

  close_mean2=data2["Close"].mean()
  nome2="MEDIA CLOSE"+" "+titolo2.upper()
  close2="CLOSE"+" "+titolo2.upper()
  data2[nome2]=close_mean2
  
  close_mean3=data3["Close"].mean()
  nome3="MEDIA CLOSE"+" "+titolo3.upper()
  close3="CLOSE"+" "+titolo3.upper()
  data3[nome3]=close_mean3

  fig=plt.figure(figsize=(8,6))

  ax1=plt.subplot(3,1,1) 
  ax1.plot(data1["Date"], data1[nome1],label=nome1,color=colore1, linestyle="--")
  ax1.plot(data1["Date"], data1["Close"],label=close1, marker="o",color=colore1, ms = 5, mfc = "k")  
  ax1.patch.set_edgecolor("k")
  ax1.patch.set_linewidth(3)
  ax1.get_xaxis().set_visible(False)
  ax1.legend()
  
  ax2=plt.subplot(3,1,2)
  ax2.plot(data2["Date"], data2[nome2],label=nome2,color=colore2, linestyle="--")
  ax2.plot(data2["Date"], data2["Close"],label=close2, marker="o",color=colore2, ms = 5, mfc = "k")  
  ax2.patch.set_edgecolor("k")
  ax2.patch.set_linewidth(3)
  ax2.get_xaxis().set_visible(False)
  ax2.legend()
  
  ax3=plt.subplot(3,1,3)
  ax3.plot(data3["Date"], data3[nome3],label=nome3,color=colore3, linestyle="--")
  ax3.plot(data3["Date"], data3["Close"],label=close3, marker="o",color=colore3, ms = 5, mfc = "k")  
  ax3.set_xlabel("Data")
  ax3.set_xticklabels(data3["Date"],rotation=90)
  ax3.patch.set_edgecolor("k")
  ax3.patch.set_linewidth(3)
  ax3.legend()

  ax1.set_title("VOLATILITÀ DEL PREZZO DI CHIUSURA")  
  plt.tight_layout()
  plt.show()
  return fig

 
def mappa1():
  map1 = go.Figure(go.Scattermapbox(mode = "markers",lon = ["10.866667"], lat = ["44.53333"],text=["Maranello (FERRARI)"],marker={"size": 15,"opacity":0.5, "color": ["red"]}))
  map1.update_layout(mapbox = {'style': "stamen-terrain"}, margin = {'l':0, 'r':0, 'b':0, 't':0})
  return map1

def mappa2():
  map2 = go.Figure(go.Scattermapbox(mode = "markers",lon = ["10.866667","-83.1763"], lat = ["44.53333","42.3223"],text=["Maranello (FERRARI)","Deaborn (FORD)"],marker={"size": 15,"opacity":0.5, "color": ["red","blue"]}))
  map2.update_layout(mapbox = {'style': "stamen-terrain"}, margin = {'l':0, 'r':0, 'b':0, 't':0})
  return map2

def mappa3():
  map3 = go.Figure(go.Scattermapbox(mode = "markers",lon = ["10.866667","-83.1763","9.1859243"], lat = ["44.53333","42.3223","45.4654219"],text=["Maranello (FERRARI)","Deaborn (FORD)","Milano (ALFA ROMEO)"],marker={"size": 15,"opacity":0.5, "color": ["red","blue","darkviolet"]}))
  map3.update_layout(mapbox = {'style': "stamen-terrain"}, margin = {'l':0, 'r':0, 'b':0, 't':0})
  return map3



#invocazioni e codice
st.set_page_config (layout="wide")
with open('style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
  st.title('Data Analysis')
        #Adding a sidebar to the app
  st.sidebar.title("Welcome!")   
  st.sidebar.write("WELCOME TO DATA ANALYSIS, il programma il cui obiettivo è quello di fornire un'analisi dei dati forniti dall'utente.")
  st.sidebar.write(" ")
  st.sidebar.write(" ")
  st.sidebar.subheader("INFORMAZIONI DATI RICHIESTI")
  st.sidebar.write("ATTENZIONE: nei dataset caricati devono essere contenuti i dati riguardanti OPEN, CLOSE, ADJ CLOSE, HIGH, LOW, VOLUME, solo così l'analisi sarà il quanto più esaustiva possibile.")
  st.sidebar.write("SUGGERIMENTO: è consigliato prendere i dati storici da Yahoo Finance.")
  st.sidebar.write(" ")
  st.sidebar.write(" ")
  st.sidebar.subheader("QR CODE")
  st.sidebar.write("Hai dubbi sul dataset oppure vuoi scaricarne dei nuovi?")
  image = Image.open("qrcode.jpg")
  st.sidebar.image(image, width=100) 
  st.sidebar.caption("Scansiona questo codice per essere reindirizzato a Yahoo Finance")  
  st.sidebar.write(" ")
  st.sidebar.write(" ") 
  st.sidebar.subheader("FILE|INPUT") 
  scelta= st.sidebar.selectbox("Se vuoi inserire i dati da input digita 'INPUT', se vuoi caricarli da file digita 'FILE': ", options=["INPUT","FILE"],key="scelta")
  
  if scelta=="FILE":
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.subheader("ISTRUZIONI")
    st.sidebar.write("Prima di iniziare, alcune informazioni.")
    st.sidebar.write("Nel file 'INPUT.txt' inserisci i seguenti valori, ricordandoti di seguire il seguente ordine di impostazione e di separare i valori tramite virgola, senza lasciare spazi vuoti (ATTENZIONE: le virgole vanno utilizzate solo come delimitatori tra un valore e l'altro): numero titoli da confrontare (minimo 1, massimo 3), nome del titolo, colore scelto per quel titolo tra le seguenti opzioni red, brown, green, olive, limegreen, blue, navy, darkcyan, lightsteelblue, pink, magenta, darkviolet.") 
    st.sidebar.caption("ATTENZIONE: il numero di titoli da confrontare va inserito una sola volta all'inizio!")
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.subheader("CARICAMENTO INPUT.TXT")
    inp= st.sidebar.file_uploader("Carica il file 'INPUT.txt' compilato")
    if inp is not None:
      inp=pd.read_csv("INPUT.txt") #con open non andava
      l=inp.columns
      st.sidebar.write(" ")
      st.sidebar.write(" ")
      if l[0]=="1":
        if len(l)==3:
          st.sidebar.subheader("CARICAMENTO DATASET")
          dati= st.sidebar.file_uploader("Carica il dataset in csv", type=["csv"])
          if dati is not None:
            titolo=l[1]
            colore=l[2].strip()
            try:  check,colori,dataFR1,colore1,titolo1=scelta1file(dati,titolo,colore)
            except ValueError: 
              st.write("Non sono presenti tutti i valori richiesti per l'analisi, riprova eliminando i dati caricati e inserendo quelli corretti")
            
            if check==True and colori==True:
              st.write(dataFR1)
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
              st.divider()
              st.write(media_mobile1(dataFR1,colore1))
              st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
              st.divider()
              st.write(pie(dataFR1,colore1,titolo1))
              st.divider()
              st.pyplot(dispersione1(dataFR1,titolo1,colore1))
              st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
              st.divider()
              st.write(OBV(dataFR1,colore1))             
              st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
              st.divider()
              st.write(rendimenti_percentuali1(dataFR1,colore1,titolo1))
              st.write("Il rendimento di un'azione indica il guadagno o la perdita prodotti da un investimento in un'azione. ")  
            else:
              dataFR1,colore1,titolo1=errore1()
              st.write(titolo1)
              image= Image.open('ferrari_logo.png')
              st.image(image, width= 150)
              st.write(dataFR1)
              st.divider()
              st.write(mappa1())
              st.divider()
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
              st.divider()
              st.write(media_mobile1(dataFR1,colore1))
              st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
              st.divider()
              st.write(pie(dataFR1,colore1,titolo1))
              st.divider()
              st.pyplot(dispersione1(dataFR1,titolo1,colore1))
              st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
              st.divider()
              st.write(OBV(dataFR1,colore1))             
              st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
              st.divider()
              st.write(rendimenti_percentuali1(dataFR1,colore1,titolo1))
              st.write("Il rendimento di un'azione indica il guadagno o la perdita prodotti da un investimento in un'azione. ")                
              
        else:
          st.sidebar.subheader("ERRORE!")
          st.sidebar.write("Non hai inserito tutti i dati richiesti.")
          dataFR1,colore1,titolo1=errore1()
          st.write(titolo1)
          image= Image.open('ferrari_logo.png')
          st.image(image, width= 150)
          st.write(dataFR1)
          st.divider()
          st.write(mappa1())
          st.divider()
          st.write(grafico_candele(dataFR1,titolo1,colore1))
          st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
          st.divider()
          st.write(media_mobile1(dataFR1,colore1))
          st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
          st.divider()
          st.pyplot(dispersione1(dataFR1,titolo1,colore1))
          st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
          st.divider()
          st.write(pie(dataFR1,colore1,titolo1))
          st.divider()
          st.write(OBV(dataFR1,colore1))
          st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
          st.divider()
          st.write(rendimenti_percentuali1(dataFR1,colore1,titolo1))
          st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")
        

      elif l[0]=="2":
        if len(l)==5:
          titolo1=l[1]
          colore1=l[2].strip()
          titolo2=l[3]
          colore2=l[4].strip()
          st.sidebar.subheader("CARICAMENTO PRIMO DATASET")
          dati1= st.sidebar.file_uploader("Carica il primo dataset")
          st.sidebar.subheader("CARICAMENTO SECONDO DATASET")          
          dati2= st.sidebar.file_uploader("Carica il secondo dataset")
          if dati1 is not None and dati2 is not None:
            
            try: check1,check2,equal,colori1,colori2,dataFR1,colore1,titolo1,dataFR2,colore2,titolo2=scelta2file(dati1,titolo1,colore1,dati2,titolo2,colore2)
            except ValueError: 
              st.write("Non sono presenti tutti i valori richiesti per l'analisi, riprova eliminando i dati caricati e inserendo quelli corretti")
            
            if check1==True and check2==True and equal==True and colori1==True and colori2==True:
              with st.container():
                col1, col2=st.columns(2)
                with col1:
                  st.write(titolo1)
                  st.write(dataFR1)
                with col2:
                  st.write(titolo2)
                  st.write(dataFR2)
              st.divider()
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              st.write(grafico_candele(dataFR2,titolo2,colore2))
              st.divider()
              st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
              st.write(media_mobile2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
              st.divider()
              st.pyplot(dispersione2(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2))
              st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
              st.divider()
              with st.container():
                col1,col2=st.columns(2)
                with col1:
                  st.write(pie(dataFR1,colore1,titolo1))
                with col2:
                  st.write(pie(dataFR2,colore2,titolo2))
              st.divider()
              st.write(OBV2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
              st.divider()
              st.write(rendimenti_percentuali3(dataFR2, colore2, titolo2))
              st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")
            else:
              dataFR1,colore1,titolo1,dataFR2,colore2,titolo2=errore2()
              with st.container():
                col1, col2=st.columns(2)
                with col1:
                  image= Image.open('ferrari_logo.png')
                  st.image(image, width= 150)
                with col2:
                  image=Image.open('Ford_logo.png')
                  st.image(image, width=150)
              with st.container():
                col1, col2=st.columns(2)
                with col1:
                  st.write(titolo1)
                  st.write(dataFR1)
                with col2:
                  st.write(titolo2)
                  st.write(dataFR2)
              st.divider()
              st.write(mappa2())
              st.divider()
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              st.write(grafico_candele(dataFR2,titolo2,colore2))
              st.divider()
              st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
              st.write(media_mobile2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
              st.divider()
              st.pyplot(dispersione2(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2))
              st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
              st.divider()
              with st.container():
                col1,col2=st.columns(2)
                with col1:
                  st.write(pie(dataFR1,colore1,titolo1))
                with col2:
                  st.write(pie(dataFR2,colore2,titolo2))
              st.divider()
              st.write(OBV2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
              st.divider()
              st.write(rendimenti_percentuali3(dataFR2, colore2, titolo2))
              st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")
               
    
        else:
            st.subheader("ERRORE!")
            st.sidebar.write("Non hai inserito tutti i dati richiesti.")
            dataFR1,colore1,titolo1,dataFR2,colore2,titolo2=errore2()
            with st.container():
              col1, col2=st.columns(2)
              with col1:
                image= Image.open('ferrari_logo.png')
                st.image(image, width= 150)
              with col2:
                image=Image.open('Ford_logo.png')
                st.image(image, width=150)
              col1, col2=st.columns(2)
              with col1:
                st.write(titolo1)
                st.write(dataFR1)
              with col2:
                st.write(titolo2)
                st.write(dataFR2)
              st.divider()
              st.write(mappa2())
              st.divider()
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              st.write(grafico_candele(dataFR2,titolo2,colore2))
              st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
              st.divider()
              st.write(media_mobile2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
              st.divider()
              st.pyplot(dispersione2(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2))
              st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
              st.divider()
              with st.container():
                left_colum, right_column=st.columns(2)
                with left_colum:
                  st.write(pie(dataFR1,colore1,titolo1))
                with right_column:
                  st.write(pie(dataFR2,colore2,titolo2))
              st.divider()
              st.write(OBV2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
              st.divider()
              st.write(rendimenti_percentuali2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
              st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")

      elif l[0]=="3":
          if len(l)==7:
            titolo1=l[1]
            colore1=l[2].strip()
            titolo2=l[3]
            colore2=l[4].strip()
            titolo3=l[5]
            colore3=l[6].strip()
            st.sidebar.subheader("CARICAMENTO PRIMO DATASET")
            dati1= st.sidebar.file_uploader("Carica il primo dataset")
            st.sidebar.subheader("CARICAMENTO SECONDO DATASET")           
            dati2= st.sidebar.file_uploader("Carica il secondo dataset")
            st.sidebar.subheader("CARICAMENTO TERZO DATASET")
            dati3= st.sidebar.file_uploader("Carica il terzo dataset")
            if dati1 is not None and dati2 is not None and dati3 is not None:
                
              try: check1, check2, check3, equal1, equal2, equal3, colori1, colori2, colori3,dataFR1,colore1,titolo1,dataFR2,colore2,titolo2,dataFR3,colore3,titolo3=scelta3file(dati1,titolo1,colore1,dati2,titolo2,colore2,dati3,titolo3,colore3)
              except ValueError: 
                st.write("Non sono presenti tutti i valori richiesti per l'analisi, riprova eliminando i dati caricati e inserendo quelli corretti")
              
              if check1==True and check2==True and check3==True and equal1==True and equal2==True and equal3==True and colori1==True and colori2==True and colori3==True:
                with st.container():
                  col1, col2, col3= st.columns(3)
                  with col1:
                    st.write(titolo1)
                    st.write(dataFR1)
                  with col2:
                    st.write(titolo2)
                    st.write(dataFR2)
                  with col3:
                    st.write(titolo3)
                    st.write(dataFR3)
                st.divider()
                st.write(grafico_candele(dataFR1,titolo1,colore1))
                st.write(grafico_candele(dataFR2,titolo2,colore2))
                st.write(grafico_candele(dataFR3,titolo3,colore3))
                st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
                st.divider()
                st.write(media_mobile3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
                st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
                st.divider()
                st.pyplot(dispersione3(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2,dataFR3,titolo3,colore3))
                st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
                st.divider()
                with st.container():
                  col1, col2=st.columns(2)
                  with col1:
                    st.write(pie(dataFR1,colore1,titolo1))
                  with col2:
                    st.write(pie(dataFR2,colore2,titolo2))
                with st.container():
                  col1, col2, col3=st.columns(3)
                  with col1:
                    st.write(" ")
                  with col2:
                    st.write(pie(dataFR3,colore3,titolo3))
                  with col3:
                    st.write(" ")
                st.divider()
                st.write(OBV3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
                st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
                st.divider()
                st.write(rendimenti_percentuali3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
                st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")
              else:
                print("SONO QUI ERRORE 3")
                dataFR1,colore1,titolo1,dataFR2,colore2,titolo2,dataFR3,colore3,titolo3=errore3()

                with st.container():
                  col1, col2, col3=st.columns(3)
                  with col1:
                    image= Image.open('ferrari_logo.png')
                    st.image(image, width= 150)
                  with col2:
                    image=Image.open('Ford_logo.png')
                    st.image(image, width=150)
                  with col3:
                    image= Image.open('alfaromeo_logo.png')
                    st.image(image, width=150)
                  col1, col2, col3=st.columns(3)
                  with col1:
                    st.write(titolo1)
                    st.write(dataFR1)
                  with col2:
                    st.write(titolo2)
                    st.write(dataFR2)
                  with col3:
                    st.write(titolo3)
                    st.write(dataFR3)
                  st.divider()
                  st.write(mappa3())
                  st.divider()
                  st.write(grafico_candele(dataFR1,titolo1,colore1))
                  st.write(grafico_candele(dataFR2,titolo2,colore2))
                  st.write(grafico_candele(dataFR3,titolo3,colore3))
                  st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
                  st.divider()
                  st.write(media_mobile3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
                  st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
                  st.divider()
                  st.pyplot(dispersione3(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2,dataFR3,titolo3,colore3))
                  st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
                  st.divider()
                  with st.container():
                    col1, col2= st.columns(2)
                    with col1:
                      st.write(pie(dataFR1,colore1,titolo1))
                    with col2:
                      st.write(pie(dataFR2,colore2,titolo2))
                    with st.container():
                      col1, col2, col3=st.columns(3)
                      with col1:
                        st.write(" ")
                      with col2:
                        st.write(pie(dataFR3,colore3,titolo3))
                      with col3:
                        st.write(" ")
                    st.divider()
                    st.write(OBV3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
                    st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
                    st.divider()
                    st.write(rendimenti_percentuali3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
                    st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")              
        
          else:
            st.sidebar("ERRORE!")
            st.sidebar.write("Non hai inserito tutti i dati richiesti.")
            dataFR1,colore1,titolo1,dataFR2,colore2,titolo2,dataFR3,colore3,titolo3=errore3()
            with st.container():
              col1, col2, col3=st.columns(3)
              with col1:
                image= Image.open('ferrari_logo.png')
                st.image(image, width= 150)
              with col2:
                image=Image.open('Ford_logo.png')
                st.image(image, width=150)
              with col3:
                image= Image.open('alfaromeo_logo.png')
                st.image(image, width=150)
              col1, col2, col3=st.columns(3)
              with col1:
                st.write(titolo1)
                st.write(dataFR1)
              with col2:
                st.write(titolo2)
                st.write(dataFR2)
              with col3:
                st.write(titolo3)
                st.write(dataFR3)
              st.divider()
              st.write(mappa3())
              st.divider()
              st.write(grafico_candele(dataFR1,titolo1,colore1))
              st.write(grafico_candele(dataFR2,titolo2,colore2))
              st.write(grafico_candele(dataFR3,titolo3,colore3))
              st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
              st.divider()
              st.write(media_mobile3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
              st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
              st.divider()
              st.pyplot(dispersione3(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2,dataFR3,titolo3,colore3))
              st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
              st.divider()
              with st.container():
                col1, col2= st.columns(2)
                with col1:
                  st.write(pie(dataFR1,colore1,titolo1))
                with col2:
                  st.write(pie(dataFR2,colore2,titolo2))
              with st.container():
                col1, col2, col3=st.columns(3)
                with col1:
                  st.write(" ")
                with col2:
                  st.write(pie(dataFR3,colore3,titolo3))
                with col3:
                  st.write(" ")
              st.divider()
              st.write(OBV3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
              st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
              st.divider()
              st.write(rendimenti_percentuali3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
              st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")


      else:
        st.sidebar.subheader("ERRORE!")
        st.sidebar.write("Non hai inserito un numero compreso tra 1 e 3.")
        st.sidebar.write("Per garantire il funzionamento del programma sono stati forniti di default i dati mensili dell'anno 2022 dei titoli 'FERRARI', 'FORD' e 'ALFA ROMEO'.")
        dataFR1,colore1,titolo1,dataFR2,colore2,titolo2,dataFR3,colore3,titolo3=errore3()
        with st.container():
          col1, col2, col3=st.columns(3)
          with col1:
            image= Image.open('ferrari_logo.png')
            st.image(image, width= 150)
          with col2:
            image=Image.open('Ford_logo.png')
            st.image(image, width=150)
          with col3:
            image= Image.open('alfaromeo_logo.png')
            st.image(image, width=150)
          col1, col2, col3=st.columns(3)
          with col1:
            st.write(titolo1)
            st.write(dataFR1)
          with col2:
            st.write(titolo2)
            st.write(dataFR2)
          with col3:
            st.write(titolo3)
            st.write(dataFR3)
        st.write(mappa3())
        st.divider()
        st.write(grafico_candele(dataFR1,titolo1,colore1))
        st.write(grafico_candele(dataFR2,titolo2,colore2))
        st.write(grafico_candele(dataFR3,titolo3,colore3))
        st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
        st.divider()
        st.write(media_mobile3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
        st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
        st.divider()
        st.pyplot(dispersione3(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2,dataFR3,titolo3,colore3))
        st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
        st.divider()
        with st.container():
          col1, col2=st.columns(2)
          with col1:
            st.write(pie(dataFR1,colore1,titolo1))
          with col2:
            st.write(pie(dataFR2,colore2,titolo2))
        with st.container():
          col1, col2, col3=st.columns(3)
          with col1:
            st.write(" ")
          with col2:
            st.write(pie(dataFR3,colore3,titolo3))
          with col3:
            st.write(" ")
        st.divider()
        st.write(OBV3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
        st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
        st.divider()
        st.write(rendimenti_percentuali3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
        st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")
  
  
  
  elif scelta=="INPUT":
    st.sidebar.write(" ")
    st.sidebar.write(" ")
    st.sidebar.subheader("NUMERO TITOLI DA CONFRONTARE")
    num = st.sidebar.radio("Scegli il numero di titoli che vuoi confrontare ", options=["1","2","3"])
    if num=="1":
      st.sidebar.subheader("CARICAMENTO DATASET")
      dati1= st.sidebar.file_uploader("Carica il primo dataset")
      if dati1 is not None:
        try: dataFR1,titolo1,colore1=scelta1(dati1)
        except ValueError: 
          st.write("Non sono presenti tutti i valori richiesti per l'analisi, riprova eliminando i dati caricati e inserendo quelli corretti")
        st.write(dataFR1)
        st.write(grafico_candele(dataFR1,titolo1,colore1))
        st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
        st.divider()
        st.write(media_mobile1(dataFR1,colore1))
        st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
        st.divider()
        st.pyplot(dispersione1(dataFR1,titolo1,colore1))
        st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
        st.divider()
        st.write(pie(dataFR1,colore1,titolo1))
        st.divider()
        st.write(OBV(dataFR1,colore1))
        st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
        st.divider()
        st.write(rendimenti_percentuali1(dataFR1,colore1,titolo1))
        st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")

    elif num=="2":
      st.sidebar.subheader("CARICAMENTO DATASET")
      dati1=st.sidebar.file_uploader("Carica il primo dataset")
      dati2=st.sidebar.file_uploader("Carica il secondo dataset")
      if dati1 is not None and dati2 is not None:
        try: dataFR1,dataFR2, titolo1, titolo2, colore1, colore2= scelta2(dati1,dati2)
        except ValueError: 
            st.write("Non sono presenti tutti i valori richiesti per l'analisi, riprova eliminando i dati caricati e inserendo quelli corretti")

        with st.container():
          col1, col2=st.columns(2)
          with col1:
            st.write(titolo1)
            st.write(dataFR1)
          with col2:
            st.write(titolo2)
            st.write(dataFR2)
          st.write(grafico_candele(dataFR1,titolo1,colore1))
          st.write(grafico_candele(dataFR2,titolo2,colore2))
          st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
          st.divider()
          st.write(media_mobile2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
          st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
          st.divider()
          st.pyplot(dispersione2(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2))
          st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
          st.divider()
          with st.container():
            col1, col2=st.columns(2)
            with col1:
              st.write(pie(dataFR1,colore1,titolo1))
            with col2:
              st.write(pie(dataFR2,colore2,titolo2))
          st.divider()
          st.write(OBV2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
          st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
          st.divider()
          st.write(rendimenti_percentuali2(dataFR1,dataFR2,colore1,colore2,titolo1,titolo2))
          st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")

    elif num=="3":
      st.sidebar.subheader("CARICAMENTO DATASET")
      dati1=st.sidebar.file_uploader("Carica il primo dataset")
      dati2=st.sidebar.file_uploader("Carica il secondo dataset")
      dati3=st.sidebar.file_uploader("Carica il terzo dataset")
      if dati1 is not None and dati2 is not None and dati3 is not None:
        try:  dataFR1,dataFR2,dataFR3,titolo1,titolo2,titolo3,colore1,colore2,colore3=scelta3(dati1,dati2,dati3)
        except ValueError: 
            st.write("Non sono presenti tutti i valori richiesti per l'analisi, riprova eliminando i dati caricati e inserendo quelli corretti")
        with st.container():
          col1, col2, col3=st.columns(3)
          with col1:
            st.write(titolo1)
            st.write(dataFR1)
          with col2:
            st.write(titolo2)
            st.write(dataFR2)
          with col3:
            st.write(titolo3)
            st.write(dataFR3)
        st.write(grafico_candele(dataFR1,titolo1,colore1))
        st.write(grafico_candele(dataFR2,titolo2,colore2))
        st.write(grafico_candele(dataFR3,titolo3,colore3))
        st.write("Il grafico a candele è un grafico finanziario che mostra i movimenti di prezzo dei titoli in una seduta. Ha la forma di una candela, la cui parte superiore indica il prezzo di apertura (open) e quella inferiore quello di chiusura (close). Le sporgenze indicano invece il prezzo più alto e più basso della seduta in esame. In particolare, in questo grafico, le candele oro indicano una crescita del titolo nel corso della seduta (Close>Open), mentre quelle marroni una diminuzione (Close<Open).")
        st.divider()
        st.write(media_mobile3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
        st.write("La media mobile è usata per apprezzare la direzione corrente di una tendenza.")
        st.divider()
        st.pyplot(dispersione3(dataFR1,titolo1,colore1,dataFR2,titolo2,colore2,dataFR3,titolo3,colore3))
        st.write("La volatilità esprime le deviazioni (gli scarti) tra prezzo effettivo e prezzo medio per ogni periodo considerato.")
        st.divider()
        with st.container():
          col1, col2= st.columns(2)
          with col1:
            st.write(pie(dataFR1,colore1,titolo1))
          with col2:
            st.write(pie(dataFR2,colore2,titolo2))
        with st.container():
            col1, col2, col3=st.columns(3)
            with col1:
              st.write(" ")
            with col2:
              st.write(pie(dataFR3,colore3,titolo3))
            with col3:
              st.write(" ")
        st.divider()
        st.write(OBV3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
        st.write("L' On Balance Volume (OBV) è un indicatore che mette in relazione il volume con le variazioni di prezzo, poiché quando c'è un volume di trading, il prezzo prima o poi ne risentirà. ")
        st.divider()
        st.write(rendimenti_percentuali3(dataFR1,dataFR2,dataFR3,colore1,colore2,colore3,titolo1,titolo2,titolo3))
        st.write("Il rendimento di un’azione indica il guadagno o la perdita prodotti da un investimento in un’azione. ")
    
  


 

    



  