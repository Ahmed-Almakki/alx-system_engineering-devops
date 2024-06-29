# install flask from pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3'],
}

package { 'Python':
  ensure   => '3.8.10',
} 
package { 'Werkzeug':
  ensure => '2.1.1',
  require  => Package['python3'],
}
