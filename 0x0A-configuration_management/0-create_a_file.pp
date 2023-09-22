file {'/tmp/school':
  ensure  => 'file',
  content => 'I love Puppet',
  owner   => 'root',
  mode    => '0644'
}
