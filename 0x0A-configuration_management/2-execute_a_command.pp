# Using Puppet, create a manifest that
# kills a process named killmenow.
# Must use the exec Puppet resource
# Must use pkill
exec { 'pkill':
    command  => 'pkill killmenow',
    provider => 'shell',
}
