import duckdb

from src.lib import database


def _conn() -> duckdb.DuckDBPyConnection:
    conn = duckdb.connect(":memory:")
    conn.execute("""
        CREATE TABLE tips AS
        SELECT * FROM (VALUES
            (10.0, 2.0),
            (20.0, 4.0)
        ) t(total_bill, tip)
        """)
    return conn


def test_select(monkeypatch):
    monkeypatch.setattr(database, "get_conn", _conn)

    df = database.select("SELECT COUNT(*) AS n FROM tips")

    assert df.loc[0, "n"] == 2


def test_select_from_file(monkeypatch):
    monkeypatch.setattr(database, "get_conn", _conn)

    df = database.select_from_file("kpi")

    assert df.loc[0, "visits"] == 2
    assert df.loc[0, "total_bill"] == 30.0
    assert df.loc[0, "avg_tip"] == 3.0
