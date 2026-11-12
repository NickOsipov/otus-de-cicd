import streamlit as st

from src.lib.database import select_from_file

st.set_page_config(page_title="Tips DB", layout="wide")
st.title("Restaurant tips")
st.caption("Таблица tips создана в DuckDB из CSV и читается SQL-запросами.")

kpi = select_from_file("kpi")

c1, c2, c3 = st.columns(3)
c1.metric("Визитов", int(kpi.loc[0, "visits"]))
c2.metric("Сумма счетов", f"{kpi.loc[0, 'total_bill']:,.2f}")
c3.metric("Средний чаевые", f"{kpi.loc[0, 'avg_tip']:.2f}")

by_day = select_from_file("by_day")
by_size = select_from_file("by_size")

left, right = st.columns(2)
with left:
    st.subheader("Средний чаевые по дням")
    st.bar_chart(by_day.set_index("day"))
with right:
    st.subheader("Доля чаевых по размеру компании")
    st.line_chart(by_size.set_index("size"))

st.subheader("Данные")
st.dataframe(select_from_file("tips"), use_container_width=True, hide_index=True)
