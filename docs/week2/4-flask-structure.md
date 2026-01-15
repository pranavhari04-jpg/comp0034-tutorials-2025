# 4. Flask app directory structure

## Moving to a package structure

The example in week 1 was of a Flask app with a basic structure. A single Python file contained the
code to create an instance of a Flask app and define the app's routes, with the page as an HTML
file in the `templates` folder.

As the app grows, this structure will become inflexible and create a monolithic file that breaks the
principles of a good design.

A more
typical [Flask application structure is to define packages](https://flask.palletsprojects.com/en/stable/patterns/packages/).

The file and folder structure could look something like this:

```text
/your_project_name
    /.instance
        database.db  # Flask instance folder with a database
    /flask_app_name
        __init__.py # Function that creates and configures the Flask app plus any extensions
        config.py   # Config values for the Flask app
        models.py   # Python classes that map to the SQL database tables
        routes.py   # Flask routes
        utils.py    # Helper functions used in the routes
        /static
            /css    # e.g. Bootstrap css files
            /js     # e.g. Bootstrap JavaScript files
        /templates
            layout.html  # Base template with the HTML head, body and Jinja placeholders
            index.html   # Template for the home page
            ... any other HTML templates
    /tests
    .venv/
    pyproject.toml
    .gitignore
    README.md
```

This is not the only structure you can use. You may see examples that separate the app
into packages and/or use [Flask Blueprints](https://flask.palletsprojects.com/en/stable/blueprints/)
to modularise the functionality.

## Modify the paralympics app to use the Application Factory pattern

Remember the design patterns lecture in COMP0035?

Flask uses a pattern called
the [application factory](https://flask.palletsprojects.com/en/stable/patterns/appfactories/) for
creating and configuring Flask apps.

Like a factory production line, you create the Flask app object, then you pass it along a production
line adding extra "features" to it as needed. You can dynamically decide on what to add as you
create the app. You are likely to need to be able to do this for some of the packages that you will
use to create your app.

### Step 1: Write the `create_app()` function

Add code to the package's `__init__.py` to create and configure the app instance.

When a package is imported, the `__init__.py` is implicitly executed and any objects it defines are
bound to the package namespace.

Add a function that must be named `create_app`.

The [Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/factory/#application-setup)
has a version. The following is a simplified version with minimal code.

```python
from config import DevConfig
from flask import Flask


def create_app(config_class=DevConfig):
    # create and configure the Flask app
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # register the routes using a blueprint
    from paralympics.main import bp
    app.register_blueprint(bp)

    return app
```

The above uses a Blueprint which you do not currently have. Ignore the error for now as you will change this in step 3.

## Step 2: Configure the Flask app

Some of the package extensions you will use rely on configuration values. Flask has several ways you
can [define configuration parameters](https://flask.palletsprojects.com/en/stable/config/) for the
Flask app. You can use any method.

The approach here uses the configuration class method.

Create a new module in the package folder called `config.py`.

Inside `config.py` create the following class:

```python
class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'dev'


class ProductionConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
```

`SECRET_KEY` is a configuration parameter used by Flask and extensions to keep data safe. In a
production app you would not want that to be in GitHub and visible to others.

It should either be generated with a random value when deploying the app or kept in a .env file.

For the coursework it's fine to leave the key in the config file.

Generate a secret key from the Terminal command line.

Type `python3` or `python` and press enter.

At the `>>>` prompt type `import secrets` and press enter.

Then type `secrets.token_urlsafe(16)` and press enter.

You should see a string of 16 characters. Copy this and use it to replace the word 'dev' in
the SECRET_KEY line in the `create_app()` function.

![Create a SECRET_KEY](../img/secret_key.png)

### 3. Delete Flask app code from main.py

Delete the code to create the Flask app instance from `main.py`.

Delete the code to run the app. 

Add code to create a Blueprint.

Change the routes to the blueprint instead of `app`.

`main.py` should now only contain this code.


```python
from flask import Blueprint, render_template

# Create the blueprint
bp = Blueprint('main', __name__)

# Change @app.route to @bp.route
@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/locations')
def locations():
    return render_template('locations.html')


@bp.route('/participants')
def participants():
    return render_template('participants.html')


@bp.route('/trends')
def trends():
    return render_template('trends.html')
```

You also need to edit `navbar.html` as the route references have changed:

```html
<!-- Change this: -->
<a class="nav-link" href="{{ url_for('index') }}">Home</a>

<!-- To this: -->
<a class="nav-link" href="{{ url_for('main.index') }}">Home</a>
```

Change all four of the routes to add 'main'.

### Run the Flask app

Check that your Flask app still runs. The run command is now: `flask --app src.paralympics run --debug`

[Next activity](5-coursework.md)