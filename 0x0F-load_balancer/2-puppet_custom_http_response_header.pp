# Install packages

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;
                add_header X-Served-By ${HOSTNAME};
                }
              }",
}

file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/custom_header'],
}
