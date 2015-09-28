# -*- coding: utf-8 -*-
from datetime import datetime
from elasticsearch import Elasticsearch
import yaml

index = ''
doc_type = ''


def carregar_configuracoes():
    global index, doc_type
    with open("config.yaml", "r") as configuracoes:
        data = yaml.load(configuracoes)
    index = data.get('index')
    doc_type = data.get('doc.type')

if __name__ == "__main__":
    print("Iniciado o sistema! \nCarregando as configurações contidas em config.yaml")
    data = carregar_configuracoes()
    print ("\n************************************************\n\nindex - %s\ndoc_type - %s\n\n***********************"
           "*************************" % (index, doc_type))
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
