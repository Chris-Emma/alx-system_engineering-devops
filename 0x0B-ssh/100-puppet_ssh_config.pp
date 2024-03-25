# Puppet script to create ssh config file
file_line { 'Turning off password authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PaswwordAuthentication no',
}

file_line { 'The identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line	 => '    IdentifyFile ~/.ssh/school',
{ 
