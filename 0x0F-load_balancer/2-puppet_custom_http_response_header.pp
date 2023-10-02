exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "1ienv HOSTNAME;" /etc/nginx/nginx.conf; sudo sed -i "s/server_name _;/add_header X-Served-By $HOSTNAME;\n\tserver_name _;\n\trewrite ^\/redirect_me https:\/\/https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}

