
# Production Deployment of the IM-Viz Web-app


# Basics 

The following manual assumes you have a Debian derivative installed. 

install apache2
enable apache2 serving public_html by running the command:
```
a2enmod userdir  
```


check if systemd is installed:
```
dpkg -l | grep systemd
```
if not installed run:
```
sudo apt-get install systemd
```

to be able to use netstat:
```
sudo apt-get install net-tools 
```

then check open ports with: 
```
sudo netstat -tulpn | grep LISTEN
sudo ss -tulpn | grep LISTEN
sudo lsof -i -P -n | grep LISTEN
```

install curl 

# set up a firewall with ufw

source: How To Set Up a Firewall with UFW on Debian 9
https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-debian-9

install ufw:
`sudo apt install ufw`


`sudo ufw default deny incoming
 sudo ufw default allow outgoing
`

allow ssh: 
`sudo ufw allow ssh`



enable http port 80 for unencrypted traffic:
`sudo ufw allow 80`

enable http port 443 for encrypted traffic:
`sudo ufw allow 443`

enable ufw:
`sudo ufw enable`

check open ports using ufw:
`sudo ufw status`

# get the files onto the server

either using Git or just copying the zip via ssh copy
Using Git has the advantage of easily updating files after another release


# Run the Front-end

install npm and node.js on the server (see main README file)

run the following command within the vue folder (i.e. *im-app*) to create the *dist* directory
 under the vue folder:
`npm run build`

install apache2 
`sudo apt install apache2`

enable modules
`sudo a2enmod authz_host`

enable the rewrite engine:
`sudo a2enmod rewrite`


navigate to: 
`/var/html/`

create folder:
`sudo mkdir -p /var/www/imviz-app/public_html`

then copy the files from the *dist* directory to the apache public_html folder designated for it: 
`~/im-viz/im-app/dist`
to 
`/var/www/imviz-app/public_html`


(optional) modify the access to the app within the apache configuration apache2.conf in `/etc/apache2/`:
*For example:* 
<Directory /www/imviz-app/public_html>
    Require host example.com
    Require ip 192.168.0.1
    # OR to allow ALL access (i.e. public access)
    # Require all granted
    FallbackResource /
    ErrorDocument 401 /errors/error401.html
</Directory>


check if apache user is available: 
`getent passwd | grep www-data`

check what users belong to group: 
`getent group www-data`

change user rights and user ownership (always do this when redeploying):

`sudo chown -R www-data:www-data /var/www/imviz-app`


`sudo chmod -R 755 /var/www`

create and configure  virtual host file:
Used manual:
https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-20-04

copy default virtual hosts file:
`sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/imviz-app.conf`

change it to:
`
<VirtualHost *:80>

    ServerAdmin admin@your_domain_1
    ServerName imviz-app
    ServerAlias www.SERVERALIAS.XYZ
    DocumentRoot /var/www/imviz-app/public_html
    DocumentRoot /var/www/html
</VirtualHost>
`

enable the virtual file with:
`sudo a2ensite imviz-app.conf`

disable the default:
`sudo a2dissite 000-default.conf`

enable proxy settings: 
`
    sudo a2enmod proxy
    sudo a2enmod proxy_http
    sudo a2enmod proxy_balancer
`
enable header setting:
`sudo a2enmod headers`


enable ssl:
`sudo a2enmod ssl`

test for configuration errors:
`sudo apache2ctl configtest`

then reload apache2:
`sudo systemctl daemon-reload`
`sudo systemctl reload apache2`

or even better restart:
`sudo systemctl restart apache2`

then test the status:
`sudo systemctl status apache2`

check if curl GET is possible with: 
`curl - imviz-app.localhost`

# Run the Back-end 

first run: `sudo apt-get install update`
install python version 10: `sudo apt-get install python3.10` 
**install** `pyhton3-venv`
**install the graphviz executables**: 
`sudo apt-get install graphviz graphviz-dev`

Export path to current shell: 
`export PATH="/usr/local/opt/graphviz/bin:$PATH" `

navigate to `im-viz/pythonproject/venv_linux/bin` and execute the *activate* file

run the *setup.py* file in the folder `im-viz/pythonproject/setup.py`

install the pm4py modified project (if failed with setup.py):
`pip install -e git+https://github.com/badrecursionbrb/pm4py-core.git#egg=pm4py`

test gunicorn with: 
`$ gunicorn --bind 0.0.0.0:5000 gunicorn_app:flask_app`

then deactivate the virtual environment with:
`$ deactivate`

 


https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

The content of the imviz.service file should be located under /etc/systemd/system/ with the following
content: 
```
[Unit]
Description=Gunicorn instance to serve imviz
After=network.target

[Service]
User=YOURUSER
Group=www-data
WorkingDirectory=/home/YOURUSER/im-viz/pythonproject
Environment="PATH=/home/YOURUSER/im-viz/pythonproject/venv_linux/bin"
access_log_format ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"

#ExecStart=/home/YOURUSER/im-viz/pythonproject/venv_linux/bin/gunicorn --workers 5 --bind 127.0.0.1:8080 --log-config log.conf -m 007 gunicorn_app:flask_app
ExecStart=/home/YOURUSER/im-viz/pythonproject/venv_linux/bin/gunicorn --workers 5 --bind 0.0.0.0:8080 --log-config log.conf -m 007 gunicorn_app:flask_app


[Install]
WantedBy=multi-user.target

```

add a logging config file for gunicorn logfile rotation:
`
[loggers]
keys=root, gunicorn.error, gunicorn.access

[handlers]
keys=console, error_file, access_file

[formatters]
keys=generic, access

[logger_root]
level=INFO
handlers=console

[logger_gunicorn.error]
level=INFO
handlers=error_file
propagate=1
qualname=gunicorn.error

[logger_gunicorn.access]
level=INFO
handlers=access_file
propagate=0
qualname=gunicorn.access

[handler_console]
class=StreamHandler
formatter=generic
args=(sys.stdout, )

[handler_error_file]
class=logging.handlers.TimedRotatingFileHandler
formatter=generic
args=('/var/log/gunicorn/gunicorn-error.log', 'midnight', 1, 90, 'utf-8')

[handler_access_file]
class=logging.handlers.TimedRotatingFileHandler
formatter=access
args=('/var/log/gunicorn/gunicorn-access.log', 'midnight', 1, 90, 'utf-8')

[formatter_generic]
format=%(asctime)s [%(process)d] [%(levelname)s] %(message)s
datefmt=%Y-%m-%d %H:%M:%S
class=logging.Formatter

[formatter_access]
format=%(message)s
class=logging.Formatter
`


then edit the user privileges using chmod to: 
```
-rwxr-xr-- 1 for imviz.service
i.e. chmod 751 imviz.service
```

run again: 
`sudo apt-get update`
`sudo apt-get upgrade`

then run:
`sudo systemctl start imviz.service`
`sudo systemctl enable imviz`
`sudo systemctl status imviz`

test if the back-end is working appropriately with the following curl command: 
```
 curl -H "Content-Type: application/json" --request POST --data '{"logstring": "<a,b,c,e,f>10;<a,d,b,c,d,e,f>10;<a,d,c,e,c,e,f>10;<a,d,e,c,d,e,f>10;<a,d,c,d,e,f>10;"}' localhost:8000/get_visualization_data_logstring?algorithm="im_standard"

```



