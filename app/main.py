from fastapi import FastAPI
from typing import List
from cassandra.cqlengine.management import sync_table
from . import (
    db,
    config,
    models,
    schema
)

settings = config.get_settings()
Product = models.Product
ProductScrapeEvent = models.ProductScrapeEvent

app = FastAPI()

session = None

@app.on_event("startup")
def on_startup():
    global session
    session = db.get_session()
    sync_table(models.Product)
    sync_table(models.ProductScrapeEvent)


@app.get("/")
def read_index():
    return {"hello": "world"}

@app.get("/products", response_model=List[schema.ProductListSchema])
def products_list_view():
    return list(Product.objects.all())

@app.get("/products/{asin}")
def products_detail_view(asin):
    data = dict(Product.objects.get(asin=asin))
    events = list(ProductScrapeEvent.objects().filter(asin=asin))
    print(events)
    events = [schema.ProductScrapeEventDetailSchema(**x) for x in events]
    print(events)
    data["events"] = events
    return data
