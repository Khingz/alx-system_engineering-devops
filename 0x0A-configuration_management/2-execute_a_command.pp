# Execute a command
exec {'Kill process':
  command => '/bin/pkill killmenow'
}

