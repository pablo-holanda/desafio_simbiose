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
    index = data.get('index.es')
    doc_type = data.get('doc.type.es')
    tempo_checagem = data.get('tempo.checagem')


if __name__ == "__main__":
    print("Iniciado o sistema! \nCarregando as configurações contidas em config.yaml")
    data = carregar_configuracoes()
    print ("\n************************************************\n\nindex -> %s\ndoc_type -> %s\ntempo de checagem -> %s"
           "\n\n************************************************" % (index_es, doc_type_es, tempo_checagem))

    es = Elasticsearch()

    while True:
        res = es.get(index=index_es, doc_type=doc_type_es)
        print(res['created'])
        sleep(tempo_checagem)
# es = lasticsearch()
#
# doc = {
#     'author': 'coisa',
#     'text': 'coisa coisada',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index", doc_type='tweet', id=2, body=doc)
# print(res['created'])
#
# res = es.get(index="test-index", doc_type='tweet', id=2)
# print(res['_source'])
#
# es.indices.refresh(index="test-index")
#
# res = es.search(index="test-index", body={"query": {"match_all": {}}})
# print("Got %d Hits:" % res['hits']['total'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
