
Tout d'abord, nous configurons Django Project avec un connecteur MongoDB. Ensuite, nous créons l'application Rest Api, l'ajoutons avec Django Rest Framework au projet. Ensuite, nous définissons le modèle de données et le migrons vers la base de données. Ensuite, nous écrivons des vues d'API et définissons des routes pour gérer toutes (y compris la recherche personnalisée).



##### Architecture

Ce diagramme montre l'architecture de notre application Djang CRUD Rest Apis avec la base de données MongoDB:
![alt text](https://github.com/AchrefBenOmrane/DataGenius_gestion_caisse/blob/master/Back_end/django-mongodb-architecture.png?raw=true)
<b>
<ul>
<li>Les requêtes HTTP seront mises en correspondance par des modèles d'URL et transmises aux vues</li>
<li>Views traite les requêtes HTTP et renvoie les réponses HTTP (avec l'aide de Serializer)</li>
<li>Le sérialiseur sérialise / désérialise les objets de modèle de données</li>
<li>Les modèles contiennent des champs et des comportements essentiels pour les opérations CRUD avec la base de données MongoDB</li>
</ul>
</b>

##### Technologie
<ul>
<li>Python 3.7</li>
<li>Django 2.1.15</li>
<li>Django Rest Framework 3.11.0</li>
<li>djongo 1.3.1</li>
<li>django-cors-headers 3.2.1</li>
<li>MongoDB 3.4 or higher</li>
</ul>

Structure du projet
Voici la structure de répertoires de notre projet Django:

![alt text](https://github.com/AchrefBenOmrane/DataGenius_gestion_caisse/blob/master/Back_end/Structure.PNG?raw=true)
