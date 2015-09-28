# -*- coding: utf-8 -*-
from datetime import datetime
from elasticsearch import Elasticsearch
import yaml
from time import sleep

index_es = ''
doc_type_es = ''
tempo_checagem = 0.0


def carregar_configuracoes():
    global index_es, doc_type_es, tempo_checagem
    with open("config.yaml", "r") as configuracoes:
        data = yaml.load(configuracoes)
    index_es = data.get('index.es')
    doc_type_es = data.get('doc.type.es')
    tempo_checagem = data.get('tempo.checagem')


if __name__ == "__main__":
    print("Iniciado o sistema! \nCarregando as configurações contidas em config.yaml")
    data = carregar_configuracoes()
    print ("\n************************************************\n\nindex -> %s\ndoc_type -> %s\ntempo de checagem -> %s"
           "\n\n************************************************" % (index_es, doc_type_es, tempo_checagem))

    es = Elasticsearch()

    while True:
        es.indices.refresh(index=index_es)
        # res = es.get(index=index_es, doc_type=doc_type_es, id=2)
        # print(res['_source'])
        res = es.search(index=index_es, doc_type=doc_type_es, body={"query": {"match_all": {}}})
        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
        sleep(tempo_checagem)
