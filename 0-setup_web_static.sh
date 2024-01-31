#!/usr/bin/env bash
# install nginx if not installed, and set up webserver for deployment

# install nginx if not yet installed
if [ ! -x /usr/sbin/nginx ]
then
	sudo apt-get update
	sudo apt-get upgrade -y
	sudo apt-get install -y nginx
	sudo service nginx start
	sudo sh -c 'echo "Hello World!" > /var/www/html/index.html'
	if [ -f /var/www/html/index.nginx-debian.html ]
	then
		sudo rm var/www/html/index.debian.html
	fi
fi

# Create fle sytem
sudo mkdir --parents /data/web_static/shared/
sudo mkdir --parents /data/web_static/releases/test/

# Create file html for testing
sudo sh -c 'echo "It'\''s all working for me" > data/web_static/releases/test/index.html'

# Create symlink
sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Update nginx config to serve content of symbolic link to hbnb_static
sudo sed -i 'listen \[::\]:80 default_server/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart
