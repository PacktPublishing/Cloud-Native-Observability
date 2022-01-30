import logging
import os
import sqlite3

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
