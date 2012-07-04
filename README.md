# Setup

To setup the database, go to manage.py  folder and give manage.py executable permission then:

```
mysql --user=root --password=root --execute="CREATE DATABASE apache2db; ALTER DATABASE \
  apache2db DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci; \
  CREATE USER 'apache2db'@'localhost' IDENTIFIED BY 'apache2db'; \
  GRANT ALL ON apache2db.* TO 'apache2db'@'localhost';"
./manage.py syncdb
```

Import the access log gile accessssub1 in raw folder to the db, and then run the server on 127.0.0.1:8001:
```
./manage.py import_alog raw/accesssub1
./manage.py runserver 127.0.0.1:8001
```

View the hits per day at: [http://127.0.0.1:8001/analytics/hits?use_tabs=1]()

remove use_tabs for csv.

To make more analytics look at analytics.view and hits.html.  With the url to access analytics.view defined in analytics.url.

