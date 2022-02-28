FROM python:3.6
WORKDIR /frontapp
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY * ./
RUN pip install -r test-requirements.txt
CMD [ "cd", "tests"]
CMD [ "python", "-m", "pytest", "." ]