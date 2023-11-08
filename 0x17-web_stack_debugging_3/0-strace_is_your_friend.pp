# Apache is returning a 500 error fix it and then automate it using Puppet

exec { 'fix Apache 500 error':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/'
}
