# 1-install_a_package.pp

# Ensure pip3 is present
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install a compatible version of Werkzeug
package { 'Werkzeug':
  ensure   => 'X.X.X',
  provider => 'pip3',
}