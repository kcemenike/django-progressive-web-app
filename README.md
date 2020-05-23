# Building a Progressive Web App with django

This project is a simple PWA using Django and the PWA library  
It uses serviceworker.js and IndexedDB to handle offline requests to the application  

For more customisation features, please visit the django-pwa repository on github

## Requirements
- A django app (with django >= 1.1)  
- django-pwa (Install from pip)  

## Changes from the usual django application

- Add 'pwa' to applications list in `settings.py`  
- Add serviceworker.js with functions for `install` and `fetch`
- Add idb.js  
- Add idbop.js  
- Add script reference to html templates
    ```
    <script type="text/javascript" src="{% static 'js/idb.js' %}"></script>
    <script type="text/javascript" src="{% static 'js/idbop.js' %}"></script>
    ```
