# we are getting a huge amount of failed requests

exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}

exec { 'nginx':
  command => 'nginx -s stop && nginx',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
