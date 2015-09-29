# -*- coding: utf-8 -*-
from datetime import datetime
from elasticsearch import Elasticsearch
import yaml
from time import sleep
import signal, sys

index_es = ''
doc_type_es = ''
ultima_checagem_es = ''
tempo_checagem = 0.0


def carregar_configuracoes():
    global index_es, doc_type_es, tempo_checagem, ultima_checagem_es
    with open("config.yaml", "r") as configuracoes:
        data = yaml.load(configuracoes)
    index_es = data.get('index.es')
    doc_type_es = data.get('doc.type.es')
    tempo_checagem = data.get('tempo.checagem')
    ultima_checagem_es = data.get('last.check.es')


def signal_handler(signal, frame):
    print('Você apertou Ctrl+C!')
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print("Iniciado o sistema! \nCarregando as configurações contidas em config.yaml")
    data = carregar_configuracoes()
    print ("\n************************************************\n\nindex -> %s\ndoc_type -> %s\ntempo de checagem -> %s"
           "\n\n************************************************" % (index_es, doc_type_es, tempo_checagem))

    es = Elasticsearch()

    while True:
        es.indices.refresh(index=index_es)
        res = es.search(index=index_es, doc_type=doc_type_es, body={"query": {"range": {"timestamp": {"gt": ultima_checagem_es}}}})
        ultima_checagem_es = datetime.now()
        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
        sleep(tempo_checagem)
