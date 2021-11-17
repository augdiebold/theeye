# The Eye - Job Application Test (Consumer Affairs)

This application is writen in python, using Django, Django Rest Framework, Postgresql and Celery with RabbitMq as broker.

Two endpoints are provided, one for receiving and list events sent to The Eye and another one to list errors from invalid requests.

The original briefing is available at the end of this document.

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

---------------------------------------------------

# The Eye

## Story

You work in an organization that has multiple applications serving websites, but it's super hard to analyze user behavior in those, because you have no data.

In order to be able to analyze user behavior (pages that are being accessed, buttons that are being clicked, forms that are being submitted, etc..), your team realized you need a service that aggregates that data.

You're building "The Eye", a service that will collect those events from these applications, to help your org making better data-driven decisions.

## Workflow

* We don't want you to be a code monkey, some things will not be 100% clear - and that's intended. We want to understand your assumptions and approaches you've taken during the implementation - if you have questions, don't hesitate to ask
* Your commit history matters, we want to know the steps you've taken throughout the process, make sure you don't commit everything at once
* In the README.md of your project, explain what conclusions you've made from the entities, constraints, requirements and use cases of this test

## Entities

```
Application
    |
    |
  Event ---- Session
```

* An Event has a category, a name and a payload of data (the payload can change according to which event an Application is sending)
* Different types of Events (identified by category + name) can have different validations for their payloads
* An Event is associated to a Session
* Events in a Session should be sequential and ordered by the time they occurred
* The Application sending events is responsible for generating the Session identifier 
* Applications should be recognized as "trusted clients" to "The Eye"
* Appllications can send events for the same session 

Example of events:
```json
{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "pageview",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}

{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "page interaction",
  "name": "cta click",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
    "element": "chat bubble"
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}

{
  "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
  "category": "form interaction",
  "name": "submit",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/",
    "form": {
      "first_name": "John",
      "last_name": "Doe"
    }
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}
```

## Constraints & Requirements

* "The Eye" will be receiving, in average, ~100 events/second, so consider not processing events in real time
* When Applications talk to "The Eye", make sure to not leave them hanging
* Your models should have proper constraints to avoid race conditions when multiple events are being processed at the same time

## Use cases:

**You don't need to implement these use cases, they just help you modelling the application**

* Your data & analytics team should be able to quickly query events from:
  * A specific session
  * A specific category
  * A specific time range

* Your team should be able to monitor errors that happen in "The Eye", for example:
  * An event that is sending an unexpected value in the payload
  * An event that has an invalid timestamp (i.e.: future)


## Pluses - if you wanna go beyond

* Your application is documented
* Your application is dockerized
* A reusable client that talks to "The Eye"
