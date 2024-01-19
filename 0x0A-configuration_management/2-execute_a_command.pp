# 2-execute_a_command.pp

exec { 'kill':
  command   => 'pkill -f killmenow',
  path      => ['/usr/bin', '/usr/sbin'],
  returns   => ['0', '1'],
  logoutput => true,
}