import logging
import os
import sqlite3
from opentelemetry import trace
from opentelemetry.exporter.jaeger.proto.grpc import JaegerExporter
from opentelemetry.instrumentation.sqlite3 import SQLite3Instrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def configure_opentelemetry():
    SQLite3Instrumentor().instrument()
    exporter = JaegerExporter(insecure=True)
    provider = TracerProvider(
        resource=Resource.create({"service.name": "sqlite_example"})
    )
    provider.add_span_processor(BatchSpanProcessor(exporter))
    trace.set_tracer_provider(provider)


configure_opentelemetry()


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info("creating database")
con = sqlite3.connect("example.db")
cur = con.cursor()

logger.info("adding table")
cur.execute(
    """CREATE TABLE clouds
               (category text, description text)"""
)

logger.info("inserting values")
cur.execute("INSERT INTO clouds VALUES ('stratus','grey')")
con.commit()
con.close()

logger.info("deleting database")
os.remove("example.db")
