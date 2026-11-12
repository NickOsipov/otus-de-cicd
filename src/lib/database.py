from pathlib import Path

import duckdb
import pandas as pd
import streamlit as st

from config.variables import TIPS_URL

SQL_DIR = Path(__file__).resolve().parents[2] / "sql"


@st.cache_resource
def get_conn() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    conn.execute(f"CREATE TABLE tips AS SELECT * FROM read_csv('{TIPS_URL}')")
    return conn


def select(sql: str) -> pd.DataFrame:
    return get_conn().execute(sql).df()


def select_from_file(name: str) -> pd.DataFrame:
    sql = (SQL_DIR / f"{name}.sql").read_text()
    return select(sql)
