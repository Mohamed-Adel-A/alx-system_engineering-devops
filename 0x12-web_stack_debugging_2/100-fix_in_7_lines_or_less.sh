#!/usr/bin/env bash
# in 7 lines or less
sudo sed -i "s/#user www-data/user nginx/" /etc/nginx/nginx.conf
sudo sed -i "s/80/8080/" /etc/nginx/sites-enabled/default
sudo chmod 777 /etc/nginx/nginx.conf
pkill apache2
sudo -u nginx service nginx start
