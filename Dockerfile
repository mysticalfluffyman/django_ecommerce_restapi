FROM python:3.7
RUN pip install pipenv
COPY . /tmp/myapp
WORKDIR /tmp/myapp/
RUN cd /tmp/myapp/ && pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "class.wsgi:application"]