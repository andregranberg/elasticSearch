from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])
index_name = "news_articles"

news_articles = {
    "title": "added article",
    "text": "this is an article added with the add_article.py script"
}

es.index(index=index_name, body=news_articles)
