# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

exec { 'change config':
  command => 'sudo sed -i "s/holberton//" /etc/security/limits.conf',
  path    => '/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin',
}
