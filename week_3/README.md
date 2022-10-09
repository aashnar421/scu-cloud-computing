# How to run this app

## Setup PG (database)
First build in the /db directory

```docker build -t my_db .```

Then run the db

```docker run --name mydb --network mynetwork -p 5432:5432 -d my_db```

## Setup PG Admin
First build in the /dba directory

```docker build -t my_dba .```

Then run the dba

```docker run --name mydba --network mynetwork -p 8081:80 -d my_dba```


## Setup Django app

First build in the / directory

```docker build -t my_django .```

Then run the django app

```docker run -it -p 8000:8000 --network mynetwork -v "$(pwd)/app:/app" my_django /bin/bash```

## To login to django, use the following username/password:

username: root

email: a@a.com

password: pass