# RestFUL API model test

- Restful API model will be my standardized model for how restful API backends should work moving forward.

- This is a test run on making a fully functioning restful api with falcon, sqlalchemy, marshmellow and mysql. 

- The server will be compatible with either gunicorn or waitress

-----

## MECH:
- [X] - add a DB environment config file (allow different DB connectors) 
- [X] - make DB function call reusable 

-----

## project structure:

<br>

### :File system

<pre>
│   app.py
│   middleware.py
│   __init__.py
│
├───config
│       config.env
│
├───engine
│       db_con.py
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
        test-post.py

</pre>



<br>


### :API routes
<pre>
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