FROM python:3.6
WORKDIR /frontapp
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY * ./
RUN pip install -r requirements.txt
EXPOSE 5001
CMD [ "python", "app.py" ]