from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import getDatas
from datetime import datetime
import plotly.graph_objects as go

# Create your views here.

@login_required
def index(request):
    cot, status = getDatas.getCotacaoStatus()
    if status == "CLOSED":
        mercado = "Mercado Fechado"
    else:
        mercado = "Mercado Aberto"
    df = getDatas.getCotacaoYahoo()
    filtro = datetime.today().strftime("%Y-%m-%d")
    newdf = df[df.index == filtro]
    reference = float(newdf.open)
    fig1 = go.Figure(go.Indicator(
            mode = "number+delta",
            value = cot,
            #reference = cot['bid'] + abs(cot['varBid'])
            number = {'prefix': "R$", "valueformat": ".4f"},
            #delta = {'position': "top", 'reference': cot['bid'] + abs(cot['varBid']), "valueformat": ".4f"},
            delta = {'position': "top", 'reference': reference , "valueformat": ".4f"},
             title = {"text": "Dolar"},
            #delta = cot['pctChange'],
            #domain = {'x': [0, 1], 'y': [0, 1]}
            ))
    fig1.update_layout(paper_bgcolor = "lightgray", title=f"Cotações: {mercado}",)
    graf1 = fig1.to_html()

    trace1 = {
        'x': df.index,
        'open': df.open,
        'close': df.close,
        'high': df.high,
        'low': df.low,
        'type': 'candlestick',
        'showlegend': False
    }
    data = [trace1]
    layout = go.Layout()
    fig = go.Figure(data=data, layout=layout)
    graf = fig.to_html()

    context = {
        'graf1': graf1,
        'graf': graf

    }
    return render(request, 'cotacaoapp/index.html', context)