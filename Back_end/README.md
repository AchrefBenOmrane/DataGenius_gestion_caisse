
First, we setup Django Project with a MongoDB Connector. Next, we create Rest Api app, add it with Django Rest Framework to the project. Next, we define data model and migrate it to the database. Then we write API Views and define Routes for handling all CRUD operations (including custom finder).



##### Architecture

This diagram shows the architecture of our Django CRUD Rest Apis App with MongoDB database:
![alt text](https://github.com/AchrefBenOmrane/DataGenius_gestion_caisse/blob/master/Back_end/django-mongodb-architecture.png?raw=true)
<b>
<ul>
<li>HTTP requests will be matched by Url Patterns and passed to the Views</li>
<li>Views processes the HTTP requests and returns HTTP responses (with the help of Serializer)</li>
<li>Serializer serializes/deserializes data model objects</li>
<li>Models contains essential fields and behaviors for CRUD Operations with MongoDB Database</li>
</ul>
</b>

##### Technology
<ul>
<li>Python 3.7</li>
<li>Django 2.1.15</li>
<li>Django Rest Framework 3.11.0</li>
<li>djongo 1.3.1</li>
<li>django-cors-headers 3.2.1</li>
<li>MongoDB 3.4 or higher</li>
</ul>

Project structure
This is the directory structure of our Django Project:

![alt text](https://github.com/AchrefBenOmrane/DataGenius_gestion_caisse/blob/master/Back_end/Structure.PNG?raw=true)
