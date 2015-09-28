from datetime import datetime
from elasticsearch import Elasticsearch
import yaml


def carregar_configuracoes():
    with open("config.yaml", "r") as configuracoes:
        data = yaml.load(configuracoes)
    return data


if __name__ == "__main__":
    data = carregar_configuracoes()
    index = data.get('index')
    print index
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
