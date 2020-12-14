
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

<ul>
<li>gestion_caisse / apps.py: déclare la classe TutorialsConfig (sous-classe de django.apps.AppConfig) qui représente l'application Rest CRUD Apis et sa configuration.</li>
<li>caisse_project / settings.py: contient les paramètres de notre projet Django: moteur de base de données MongoDB, liste INSTALLED_APPS avec le framework Django REST, application gestion_caisse, CORS et MIDDLEWARE.</li>
<li>gestion_caisse / models.py: définit la classe de modèle de données Tutorial (sous-classe de django.db.models.Model).</li>
<li>migrations / 0001_initial.py: est créé lorsque nous effectuons des migrations pour le modèle de données, et sera utilisé pour générer la collection de base de données MongoDB.</li>
<li>gestion_caisse / serializers.py: gère la sérialisation et la désérialisation avec la classe TutorialSerializer (sous-classe de rest_framework.serializers.ModelSerializer).</li>
<li>gestion_caisse / views.py: contient des fonctions pour traiter les requêtes HTTP et produire des réponses HTTP (en utilisant TutorialSerializer).</li>
<li>gestion_caisse / urls.py: définit les modèles d'URL ainsi que les fonctions de requête dans les vues.</li>
<li>caisse_project / urls.py: a également des modèles d'URL qui incluent gestion_caisse.urls, ce sont les configurations d'URL racine.</li>
 </ul>
