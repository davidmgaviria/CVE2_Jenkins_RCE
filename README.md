# CVE2_Jenkins_RCE
 Repo for CVE S2 Team 1 -- working on a Jenkins exploit

# Setting Up Jenkins
- Run 'docker-compose build && docker-compose up -d' 
- Navigate to http://localhost:8080, you will be prompted for an admin password
- Open a shell in the jenkins docker container (NOT THE POSTGRES ONE)
    - docker exec -it <container_id> bash
    - cd to directory listeed on the Jenkins page, acquire the password
- Set up a basic admin account (remember the password) and install default plugins 


# Connecting to CLI via SSH
- open a terminal, run 'ssh jenkins@localhost'
    - password is jenkins (or whatever you set in your docker compose)