# create a manifest that kills a process named killmenow
exec { 'kill_processor':
  command => 'pkill killmenow',
}
