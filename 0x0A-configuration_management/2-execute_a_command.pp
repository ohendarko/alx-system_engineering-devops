# A manifest that kills a process named killmenow

exec { 'kill_killlmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true
}
