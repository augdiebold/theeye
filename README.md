# The Eye - Job Application Test (Consumer Affairs)

This application is writen in python, using Django, Django Rest Framework, Postgresql and Celery with RabbitMq as broker.

Two endpoints are provided, one for receiving and list events sent to The Eye and another one to list errors from invalid requests.

The original briefing is available in the end of this document.

## Installation
```
git clone https://github.com/augdiebold/theeye.git
```
```
docker-compose up --build -d
```
### Create an User and generate the access token
```
docker-compose run web python manage.py createsuperuser --username youruser --email your@email.com
```
```
docker-compose run web python manage.py drf_create_token youruser
```


## Endpoints
- **Base URL** http://127.0.0.1:8000/api/

### Events
| METHOD  |  PATH  |  DESCRIPTION  |
| ------------------- | ------------------- | ------------------- |
|  GET |  /events |  List all events |
|  GET |  /events/{id} |  Return an event by its id |
|  POST |  /events |  Creates event |

### Errors
| METHOD  |  PATH  |  DESCRIPTION  |
| ------------------- | ------------------- | ------------------- |
|  GET |  /errors |  List all errors |
|  GET |  /errors/{id} | Return an error by its id |

## Swagger and Redocs

The Swagger and Redocs documentation are available in these two URIs path, respectively:
- /swagger
- /redoc

## Discussion
- Is assumed that the data field has no pre-defined format, in this case, it is validated if the payload is not empty and a JSON valid format.
- It is being saved one error for every incorrect field in the payload (i.e. if there are three invalid fields, three error objects will be created). I understand that this is a bottleneck in the project, however, it was designed this way to isolate the errors and benefits the error log analysis.
- To make sure "The Eye" does not leave the applications hanging, I used celery to run the data saving and validation tasks with RabbitMQ as a broker. 
