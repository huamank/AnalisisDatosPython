import pandas as pd
import sqlalchemy as db
from sqlalchemy import text
from utils import connection as con

conn_retail_db = con.connect_retail_db()
conn_dw_retail = con.connect_dw_retail()