execfile('./variables.py');

def serverStatus(server):
  cd('/ServerLifeCycleRuntimes/' + server.getName() )
  return cmo.getState()


connect(wls_uid, wls_password, 't3://'+wls_adminServer+':'+wls_adminServerPort);

svrs = cmo.getServers()
domainRuntime()
for server in svrs:
  if server.getName() != 'AdminServer':
    serverState = serverStatus(server)
    serverConfig()
    machine = server.getMachine();
    print server.getName() + " is " + serverState + " on " + machine.getName()
    domainRuntime()

    if serverState == "RUNNING":
      if machine.getName() == wls_nm_hostname:
        try:
         shutdown(server.getName(),'Server','true',1000,force='true', block='true')
         serverState = serverStatus(server)
         print "Now " + server.getName() + " is " + serverState + " on " + machine.getName()
        except:  
         print "Unable to stop server " + server.getName() + ". Please consult the server's log file: " 
         print " " + wls_domainDir + "/servers/" + server.getName() + "/logs/" + server.getName() + ".out"
disconnect()

exit()
