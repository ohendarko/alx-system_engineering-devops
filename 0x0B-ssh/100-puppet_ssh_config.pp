exec { 'turn-off-password-auth':
  command     => '/bin/sed -i "s/^PasswordAuthentication.*/PasswordAuthentication no/" /etc/ssh/sshd_config',
  refreshonly => true,
}

file { '/root/.ssh':
  ensure  => directory,
}

file { '/root/.ssh/config':
  ensure  => present,
  content => "IdentityFile ~/.ssh/school\n",
}

exec { 'reload-ssh':
  command     => '/bin/systemctl reload sshd',
  refreshonly => true,
}
