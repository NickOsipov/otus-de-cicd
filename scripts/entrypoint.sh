#!/bin/sh

echo "Starting Streamlit app..."

streamlit run src/main/app.py --server.port 8501 --server.address 0.0.0.0
