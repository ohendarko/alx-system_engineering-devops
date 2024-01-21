# Puppet manifest for SSH client configuration

file { '/home/ubuntu/.ssh/config':
  ensure  => present,
  content => "\
Host 460690-web-01
    HostName 54.145.240.142
    User ubuntu
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
    PubkeyAuthentication yes
",
  owner   => ubuntu,
  group   => ubuntu,
  mode    => '0600',
}
