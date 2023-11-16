# we are getting a huge amount of failed requests

exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
