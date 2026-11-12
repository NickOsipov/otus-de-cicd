FROM python:3.12.8-slim-bookworm

ENV APP_HOME=/app
ENV PYTHONPATH=$APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src $APP_HOME/src
COPY sql $APP_HOME/sql
COPY config $APP_HOME/config
COPY tests $APP_HOME/tests
COPY scripts $APP_HOME/scripts
RUN chmod +x $APP_HOME/scripts/*.sh

EXPOSE 8501

CMD ["bash", "/app/scripts/entrypoint.sh"]