# Digital-Job-Cards
When clonning this project, it first requires changing the ALLOWED_HOST in websitedjc/settings.py:

   ALLOWED_HOSTS = ['54.201.89.50'] to ALLOWED_HOSTS = [COMPUTER_IP]

Standing in the Dockerfile folder do:

1 - sudo docker build -t websitedjc:1.0 .

2 - sudo docker run --publish 8000:8000 --detach --name bb websitedjc:1.0
