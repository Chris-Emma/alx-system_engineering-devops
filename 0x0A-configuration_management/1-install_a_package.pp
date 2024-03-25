# Using Puppet, install flask from pip3.
# manifest installs Flask -v 2.1.0 using pip3

package { 'flask':
	ensure => '2.1.0',
	provider => 'pip3',
}
