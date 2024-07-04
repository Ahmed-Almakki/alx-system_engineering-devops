#!/usr/bin/env bash
# make changes to our configuration file

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Turn off password':
  path  => '/etc/ssh/ssh_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication',
}

file_line { 'Identfy file':
  path  => '/etc/ssh/ssh_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#IdentityFile',
}
