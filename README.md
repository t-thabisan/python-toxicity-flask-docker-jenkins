# python-toxicity-flask-docker-jenkins

This project was carried out as part of the M2 course - DATA ENGINEERING II.

**Authors** :
- THAVANESAN Thabisan
- TANG Hugo 
- BUTERY Hugo

**Date :** 07/03/22

**Promotion :** M2 LSI 2 - APP - BIG DATA

**User Stories** : 
- The application is a toxicity monitor, where the user inputs a piece of text, and the application 
should be able to infer if the text is toxic or not.
- The text language used must be English
- The application should have a web interface with an input form and a submit button, where 
users can input their potentially toxic text, and hit submit, then the statistics about the text’s 
toxicity are displayed.
- Every functional part of the application must be tested for proper functionality.
- The application must be able to handle 100 requests per minute.
- The application must be easily deployable.
- The application must be properly monitored after deployment, we want to be able to quickly 
find any issue that might cause performance problems or down time.


# Getting Started

**Step 1:**  Make sure git is installed on your os. If not, you can check this link :
`https://git-scm.com/book/en/v2/Getting-Started-Installing-Git`

**Step 2:**  Clone the project into your local machine using the following command :
`git clone https://github.com/t-thabisan/python-toxicity-flask-docker-jenkins.git`

### Prerequisites

**1. Docker**

Make sure you have Docker installed. If not, you can follow the below link for official documentation  :
`https://docs.docker.com/get-docker/`

### Installing

**Step 1:**  Go to the directory where the project was cloned in previous step.
```
cd python-toxicity-flask-docker-jenkins
```
**Step 2:**  Make sure Docker is up and running. 

**Step 3:**  Run
```
docker-compose up
```
That will start the app (frontend & backend).

**Step 4:**  Open up the browser and paste the below url

```
http://localhost:5001/
```
You will be redirected to a form in which you have to put a sentence and submit to have the result.
(The server part is running on http://localhost:5000/api/)

# Toxicity analysis model

For this project we toxic-bert library as our machine learning model.

Paper available at : `https://huggingface.co/unitary/toxic-bert`

# Architecture

### General Architecture
    ├── frontend 			   <- the source code of the frontend
    ├── backend 			   <- the source code of the backend
    ├── docker-compose.yaml    <- YAML file to configure our app (front/back) using the dockerfiles in the frontend and backend directory, to be launchable with docker-compose up
    ├── README.md              <- The README used as a report of the project and for developers using this project
    ├── prometheus.yml         <- basic configuration of prometheus
	├── rules.yml              <- contain the necessary rule statements to include in Prometheus
    
### Frontend/Backend Architecture
We decide to use a MVC architecture to structure our frontend/backend project. 
Note that in the frontend, the */view* folder of a traditionnal MVC architecture is replaced by a */templates* folder because we using flask and flask requires a */templates* folder where it search the views. Anyway, it works the same way as a view folder. 

#### Frontend 

    ├── app				
    │   ├── controller 			<- contains the controller that intercept the request, call the model and return the result using a template
    │   ├── routes				<- contains a blueprint configuration that defined a link beetween a callable ressource (url) and the a controller function  
    │   ├── templates			<- contains the views which are html pages
    │   ├── tests				<- contains all the tests organized with the corresponding folder of MVC architecture (controller, model, routes and integration testing the views)
    │   └── app.py				<- the index : create app, register blueprint and launch the app
    ├── docker-compose.yaml    	<- YAML file to configure our frontend app using dockerfile to be launchable with docker-compose up
    ├── Dockerfile.dockerfile  	<- text file that contain the commands to assemble the frontend image that will be used to deploy container
    ├── requirements.txt      	<- Dependences to install, used by dockerfile
    
#### Backend

    ├── app				
    │   ├── controller 			<- contains the controller that intercept the request, call the model and return the result using a template
    │   ├── model       		<- contains the model that calls the toxic-bert library and check the toxicity of an input
    │   ├── routes				<- contains a blueprint configuration that defined a link beetween a callable ressource (url) and the a controller function  
    │   ├── tests				<- contains all the tests organized with the corresponding folder of MVC architecture (controller, model, routes and integration testing the views)
    │   └── app.py				<- the index : create app, register blueprint and launch the app
    ├── docker-compose.yaml    	<- YAML file to configure our backend app using dockerfile to be launchable with docker-compose up
    ├── Dockerfile.dockerfile  	<- text file that contain the commands to assemble the backend image that will be used to deploy container
    ├── requirements.txt      	<- Dependences to install, used by dockerfile
 
# The ressources 

#### Frontend
This app has the bellow ressources : 
-  http://localhost:5001/ : redirect to /toxicity ressource
-  http://localhost:5001/toxicity/: the form in which you can fill a sentence and submit to mesure the toxicity

You can also use the following ressource to check a sentence without using the form : 
- http://localhost:5001/toxicity/result?sentence=X : where X is the sentence to check

#### Backend
You can access to the backend service with the following ressource : 
http://localhost:5000/api/toxicity?sentence=X : where X is the sentence to check

# The tests

### Tests folder architecture

    ├── tests
    │   ├── controller 	<- test the controller returns using resources url and not blueprint configuration
    │   ├── model		<- test the model capacity to return a valid result from an input sentence
    │   ├── routes 		<- test the controller returns using blueprint ressources
    │   ├── integration <- test the global app returns and check the result of the view

### Requirements

Make sure you have Pytest, BeautifulSoup and requests installed. If not you can install it using the following commands :

`pip install pytest`

`pip install detoxify`

`pip install requests`

  
### Run the tests

Before running the test, in order to be able to execute unit tests, install requirements.txt packages. Use the following command :

`pip install -r requirements.txt`

You can run the tests using the following command from the root folder *python-toxicity-flask-docker-jenkins/* :

`python -m pytest .`

# The DevOps tools
## Git

We used github as our repository and version control, the public link is : `https://github.com/t-thabisan/python-toxicity-flask-docker-jenkins`

## Trello

We used trello as our task manager, link to our board is : `https://trello.com/b/OXyJHHUW/dataengineeringproject2`