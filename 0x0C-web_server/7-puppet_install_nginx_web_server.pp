# Install Nginx web server (w/ Puppet)

exec {'install':
  provider => shell,
  command  => '
  sudo apt-get update -y;
  sudo apt-get install nginx -y;
  sudo ufw allow "Nginx HTTP";
  echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html;
  sudo sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default
  sudo service nginx start',
}
