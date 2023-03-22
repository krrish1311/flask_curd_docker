FROM python
RUN pip install flask
RUN pip install psycopg2
COPY app.py .
CMD flask run --host=0.0.0.0 --port=7845
