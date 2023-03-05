# Define classes to store 
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

data = {
    "asin": "TESTING123",
    "title": "Mark 1"
}

# By making our class inherit Cassandra's Model -> turn it into a table
class Product(Model): # -> table
    __keyspace__ = "scraper_app"
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()
    price_str = columns.Text()


class ProductScrapeEvent(Model): # -> table
    __keyspace__ = "scraper_app"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text()