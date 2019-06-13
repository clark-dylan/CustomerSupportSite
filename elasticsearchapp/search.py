from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Integer, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
import forum.models

connections.create_connection()

class QuestionsIndex(DocType):
    question_id = Integer()
    num_replies = Integer()
    title = Text()
    date_published = Date()

    class Meta:
        index = 'questions'


def bulk_indexing():
    QuestionsIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in forum.models.Questions.objects.all().iterator()))


def search_title(title):
    s = Search().query('match_phrase_prefix', title=title)
    response = s.execute()
    return response