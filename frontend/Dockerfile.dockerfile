FROM python:3.6
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY * ./
RUN pip install -r requirements.txt
EXPOSE 5001
EXPOSE 8011
CMD [ "flask", "run", "--port=5001"]