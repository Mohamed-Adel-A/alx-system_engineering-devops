# Apache is returning a 500 error
# fix it and then automate it using Puppet

exec { "fix Apache 500 error":
  provider => "shell",
  command  => 'sudo sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}