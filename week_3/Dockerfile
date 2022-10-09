FROM python

COPY requirements.txt /tmp/ 
RUN pip3 install -r /tmp/requirements.txt

VOLUME /app
WORKDIR /app 

EXPOSE 8000

#after building and running, copy the following into terminal: django-admin startproject app2
#then python app/app2/manage.py runserver 0.0.0.0:8000 (this is done in app2)
#python /app/app/manage.py createsuperuser
# email aaddress: a@a.com
# password - nothing
#this should open up a db/sqlite3 database in the app2 folder
#
