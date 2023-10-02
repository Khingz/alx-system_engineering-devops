# Installs a Nginx server with custom HTTP header

exec {'package update':
  provider => shell,
  command  => 'sudo apt-get -y update',
}

exec {'Nginx Install':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  require  => Exec['package update'],
}

exec {'Add env':
  provider => shell,
  command  => 'sudo sed -i "1ienv HOSTNAME;" /etc/nginx/nginx.conf;',
  require  => Exec['Nginx Install'],
}

exec { 'add header':
  provider    => shell,
  command     => 'sudo sed -i "s|index index.html index.htm;|index index.html index.htm;\n\tadd_header X-Served-By \$HOSTNAME;|" /etc/nginx/sites-available/default
',
  require      => Exec['Add env'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  require  => Exec['add header'],
}

