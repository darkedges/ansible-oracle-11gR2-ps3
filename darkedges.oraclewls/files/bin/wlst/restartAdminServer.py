execfile('./variables.py');

print 'Connect to the Node Manager';
nmConnect(wls_uid, wls_password, wls_nm_hostname, wls_nm_listenPort, wls_domain, wls_domainDir, wls_nm_listenPortType);
serverStatus = nmServerStatus('AdminServer')

if serverStatus == 'RUNNING':
	print 'Stopping the Admin Server';
	nmKill('AdminServer');

print 'Starting the Admin Server';
nmStart('AdminServer');

print 'Disconnecting from Node Manager';
exit()
