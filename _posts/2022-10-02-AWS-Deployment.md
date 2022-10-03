---
toc: false
layout: post
description: AWS Deployment Steps 
categories: [Deployment, week6]
title: AWS Deployment
---

## This is my blogpost that shows details of AWS Deployment of Personal Flash Website. 

####  Here are the steps from git clone to build and run Flask locally on AWS after connecting to AWS E2C
```
cd /home/ubuntu/navan-flask
git clone https://github.com/NavanYatavelli/BeeFlask.git
```
####  Edit docker-compose.yml file 
<img src="{{site.baseurl}}/images/personal-flask-website.jpg" alt="personal-flask-website jpg">

#### Run and check if docker-compose process is running
```
sudo docker-compose up -d
sudo docker-compose ps
```

#### Acesss locally
```
curl localhost:8087
```
#### TBD - Image of the run

#### Configure nginx to redirect requests. Internet request 8081 port on maps to 8087 port on localhost
#### 18.216.138.52:8081 --> localhose:8087
```
sudo nano /etc/nginx/sites-available/navan-flask
```
#### TBD - Image of navan-flask

#### Accesss Flask Website - Browser
[Personal Flask Website](http://18.216.138.52:8081/)
<img src="{{site.baseurl}}/images/personal-flask-website.jpg" alt="personal-flask-website jpg">

#### Make change in github.com/../BeeFlask to this file /BeeFlask/templates/index.html
<img src="{{site.baseurl}}/images/deployment-github-updated.jpg" alt="personal-flask-website jpg">

#### Get latest from Github to AWS, rebuild and relaunch docker process
```
cd /home/ubuntu/navan-flask
git pull

//Check Docker process running (optional)
sudo docker-compose ps

// Kill the docker process
sudo docker-compose kill

//Rebuid Docker
sudo docker-compose build --no-cache

//Restart Docker process
sudo docker-compose up -d
```

#### Acesss locally
```
curl localhost:8087
```
#### TBD - Image of the run

#### Accesss Flask Website - Browser, shows updated
<img src="{{site.baseurl}}/images/deployment-browser-updated.jpg" alt="personal-flask-website jpg">



