# htmlcssjs
PLH414 2017/2018

See branches

needs the following in your /etc/apache2/sites-available/000-default.conf

WSGIDaemonProcess htmlcssjs user=www-data group=www-data processes=1 threads=5
WSGIScriptAlias /htmlcssjs /var/www/htmlcssjs/app.wsgi
<Directory /var/www/htmlcssjs>
    WSGIProcessGroup htmlcssjs
    WSGIApplicationGroup %{GLOBAL}
    Require all granted
</Directory>
