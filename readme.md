# RestFUL API model test

- Standardized model for RESTful API
- Template design of fully functioning restful api.
        - falcon, sqlalchemy, marshmellow, mysql. 

- The server will be compatible with either gunicorn or waitress

-----

## MECH:
- [X] - add a DB environment config file (allow different DB connectors) 
- [X] - make DB function call reusable 
- [X] - make OS agnostic

-----

## project structure:

<br>

### :File system
<pre>
│   app.py
│   middleware.py
│   __init__.py
│
├───engine
│       db_con.py
│       _config.env
│       __init__.py           
│
├───models
│       vault1_model.py
│       __init__.py
│   
├───resources
│       vault1_resource.py
│       __init__.py
│   
├───schemas
│       vault1_schema.py
│   
└───utils
        post_data.py
        req_data.py
</pre>



<br>


### :API routes


<pre>
> falcon-inspect-app app:api

Falcon App (WSGI)
• Routes:
    ⇒ /vault1 - Vault1_resource:
       ├── GET - on_get
       └── POST - on_post
• Middleware (Middleware are independent):
    → Middleware.process_request

        ├── Process route responder

    ↢ Middleware.process_response
</pre>



----
----
