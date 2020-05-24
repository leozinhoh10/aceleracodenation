from datetime import datetime, timedelta
from operator import itemgetter

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

custo_por_numero=[]
fim_chamada=[]
inicio_chamada=[]
diferen=[]
lista_final=[]
telefones = []
numeros_custos={}
resultado={}



















#print(f'a ligação custou: {custo_chamada}')
def classify_by_phone_number(records):
    #criar lista com todos as ligações e custo
    for i in records:
        numeros_custos['source']=i['source']
        diferen=(datetime.fromtimestamp(i['end']) - datetime.fromtimestamp(i['start']))
        if 6<=datetime.fromtimestamp(i['start']).hour<22:
            minutos=divmod(diferen.seconds, 60)
            valor=(minutos[0]*0.09+0.36)
            numeros_custos['total']=valor
        else:
            numeros_custos['total']=0.36
        lista_final.append(numeros_custos.copy())

#procurar os telefones sem repeticao


    for numero in lista_final:
        if numero['source'] not in telefones:
            telefones.append(numero['source'])


    for telefone in telefones:
        valor_total=0
        for i in lista_final:
            if telefone == i['source']:
                valor_total+=i['total']
        custo_por_numero.append(valor_total)


    for k in range(6):
        resultado[f'{telefones[k]}']=custo_por_numero[k]

    ranking=sorted(resultado.items(), key=itemgetter(1), reverse=True)

    resultado_final=list()
    dict={}
    for k in ranking:
        dict['source']=k[0]
        dict['total']=round(k[1],2)
        resultado_final.append(dict.copy())

    return resultado_final
