FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir \
    jupyterlab \
    pandas \
    seaborn \
    psycopg2-binary \
    sqlalchemy \
    python-dotenv

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token="]