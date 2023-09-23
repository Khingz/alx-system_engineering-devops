# Modifies ssh config files
file_line { 'use school private key':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}

file_line { 'disable password authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

