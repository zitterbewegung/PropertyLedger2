# PropertyLedger2
Property Ledger
Docker setup
 11  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
   12  sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
   13  sudo apt-get update
   14  apt-cache policy docker-ce
   15  sudo apt-get install -y docker-ce
   16  sudo usermod -aG docker ${USER}
   17  su - ${USER}
   18  sudo
   19  sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
