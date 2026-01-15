# 3. Flask layout

For the Flask version of this activity you will create a multipage app. It is possible to create a
single-page app in Flask, but it is a little tricky to do without JavaScript. JavaScript code does
not contribute to the marks awarded in the coursework so is avoided in the tutorial activities.

The app will have the following pages:

- 'Home' page with the questions
- Trends chart page
- Participants chart page
- Paralympics locations page

Next week you will create charts. The charts will include:

- A line chart with a dropdown to select variants ("sports", "events", "counties", "participants")
- A bar chart showing the change in male/female participants in summer and winter Paralympics. This
  has a checkbox selector for Winter and/or Summer.
- A map with points showing where each of the Paralympics has been held. This displays statistics
  about each event when hovered over the map points.

## Flask templates use HTML and Jinja

Flask returns pages from a route using the `render_template` function.

`render_template('index.html')` takes an HTML file as the first parameter.

By default, Flask looks for these `.html` files in a folder named `templates` in the application
package.

Templates can also contain Jinja template syntax. Jinja is a template engine. Templates for are used
for web pages that receive dynamic content from a web server (Flask in this case) and render it as
a static page in the web browser.

Jinja defines elements in a template that can be populated with values from Flask app Python code.

## Introduction to Jinja

### Syntax

Jinja templates can be HTML files that include Jinja syntax in them.

The types of Jinja syntax you may want to use include:

- `{% ... %}` for statements such as `block` and `extends`; control structures `for` and `if`; and
  macros. [Macros](https://jinja.palletsprojects.com/en/3.1.x/templates/#macros) can be used to
  write reusable
  functions.
- `{{ ... }}` for expressions and variables
- `{# ... #}` for comments

Examples of the syntax:

```jinja
{# To inherit all the layout from another template, in this case 'layout.html' #}
{% extends 'layout.html' %} 

{# To define an area, a 'block', in a template where the content will be dynamically provided for each page created from the template #}
{% block blockname %} 
    {# Here is where the dynamic contents will appear #}
{% endblock %}

{# For loop #}
{% for user in users %} 
	<p>{{ user.username|e }}</p> 
{% endfor %}
```

### Template inheritance

Jinja provides template inheritance. This allows you to build a base, or parent, template that
contains the common elements of your app and defines blocks that child templates can override. 
Changes to the parent are inherited by all its children, so you only need to manage the code in one 
place.

In your Flask app you will create a **parent template** that contains the default HTML page
structure, the CSS, etc. and **child templates** inherit this and apply any content or elements they
need.

### Escaping user input

In Flask, Jinja is configured to auto-escape any data that is rendered in HTML templates. This means
that it's safe to render user input. Any characters they've entered that could mess with the HTML,
such as `<` and `>` will be escaped with safe values that look the same in the browser but don't
cause unwanted effects.

This will be important if you plan to allow users to input text in some way in your application as
it prevents them from entering HTML that could harm your application.

### Documentation

You may need to refer to other Bootstrap and Jinja documentation to complete the activities:

- [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Jinja template designer documentation](https://jinja.palletsprojects.com/en/stable/templates/)
- [Flask tutorial on templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)
- [VS Code documentation on templates](https://code.visualstudio.com/docs/python/tutorial-flask#_create-multiple-templates-that-extend-a-base-template)
- [Primer on Jinja templating](https://realpython.com/primer-on-jinja-templating/)

## Create the Flask parent template

1. Create a Flask app project in your IDE
2. Create a basic Flask app
3. Create an HTML file with the overall HTML page structure and save to the `templates` folder
4. Add the CSS links to the `<head>`, and optionally JavaScript links in the `<head>` or `<body>`
5. Add Jinja block template areas that child templates can use
6. Create child templates for each page
7. Create routes that render the pages
8. Add a Bootstrap styled navigation bar with links to the pages

### 1. Create a basic Flask app
In `main.py` add:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure you can run the app. 

Refer to week 1 tutorials if you don't remember the basic code to create and run a Flask app.

### 2. Create a Flask app project in your IDE

1. Create a new Python project in your IDE (VS Code, Pycharm).
2. Add .gitnore, README.md and pyproject.toml (covered in COMP0035)
3. Create and activate a Python virtual environment.
4. Install `pip install flask`
5. Create an `src` directory
6. Inside the `src` directory, create a Python package for the app code e.g. `paralympics`
7. Inside the `paralympics` package create a Python file for the app e.g. `main.py`
8. Inside the `paralympics` package create a folder called `templates` and another called `static`
9. Install the code itself as an editable package (relies on pyproject.toml) `pip install -e .`

You will have a project folder that looks like this:

```text
project_folder_name/
 ├── .venv/
 ├── src/
     └── paralympics
        ├── __init__.py
        ├── app.py   # Flask app file
        ├── static/  # Static files such as CSS, images, JavaScript
        └── templates/ # HTML files
├── .gitignore
├── pyproject.toml
├── README.md
```

### 3. Create an HTML file with the base structure

Create a file called `base.html` or `layout.html` and save it to the `templates` folder.

It should contain:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>

</body>
</html>
```
### 4. Add the CSS

[Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/#quick-start) explains how to use their CDN-hosted version or download the files and add to your own code.

Some Bootstrap utilities use JavaScript so you need their CSS and JavaScript.

The CDN version of the files can be added to your template as follows:

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <!-- ADD THE META VIEWPORT AND CSS LINK -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css"
          rel="stylesheet"
          integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB"
          crossorigin="anonymous">
</head>
<body>
<!-- ADD THE JAVASCRIPT AT THE END OF THE BODY -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI"
        crossorigin="anonymous"></script>
</body>
</html>
```

You need an active internet connection while your app is running to use this method. An alternative
that doesn't rely on an internet connection is to download the CSS files from Bootstrap and add them
to your Flask project.

Flask apps have a folder named **static** for files that don't change while the app is
running, such as CSS, JavaScript, and images.

To reference the **static** folder in Flask, you use a Flask function `url_for` which you add using
syntax for a Jinja expression. 

The code structure is:

```jinja
<head>
   <link rel="stylesheet" href="{{ url_for('static', filename='boostrap.css') }}">
</head>
```

`static` is the folder name, the `filename` should include both the .css file name and any
subfolder structure below static. For example, if in a folder `static/css/mystyles.css` you would
use: `<link rel="stylesheet" href="{{ url_for('static', filename='/css/mystyles.css') }}">`

### 5. Add Jinja block template areas that child templates can use

Add a block to the head section that allows the title to be changed: 

```html
<title>Paralympics - {% block title %}{% endblock %}</title>
```

Add a block named 'content' to the start of the `<body>` that allows the content to be changed. 
Bootstrap expects 
elements to be wrapped in a container. An HTML `<div>` is "division" element and is primarily used 
as a container to create sections or divisions in a web page. This is useful as you can target the 
`div` to apply styles, or locate sections on the page.

```html

<div id="content" class="container-fluid">

    {% block content %}{% endblock %}

</div>
```

### 6. Create child templates for each page

Child templates inherit from the parent (base). You place page-specific values in the 'title' and 
'content' blocks that you defined in the base.

An example of the template code for the home page:

```html
{% extends 'base.html' %}

{% block title %}Questions{% endblock %}

{% block content %}
    <p>Placeholder for the home page which will have the questions.</p>
{% endblock %}
```

Create an HTML template for each of the following pages:

- 'Home' page with the questions
- Trends chart page
- Participants chart page
- Paralympics locations page

### 7. Create routes that render the pages
Add code to create the Flask app and generate the pages for each route to `main.py`. This was covered in week 1 activities.

[Routing](https://flask.palletsprojects.com/en/stable/quickstart/#routing) is explained in the Flask documentation which you should read.

A route is defined with

- Flask app route decorator with the URL and the HTTP methods it supports (GET, POST, DELETE etc)
- A function to run that returns an HTML page or other content

Flask also has a concept called Blueprints which, among other things, can associate routes with
a particular aspect of the app. This app will only have one Blueprint, 'main'.

Add the Blueprint and define the routes. All the routes are currently 'GET' routes which is the
default so you don't need to specify it.

Modify the index route created earlier to return `render_template("index.html")`:

```python
from flask import Blueprint, Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
```

Add routes for the other three pages.

### 8. Add a Bootstrap styled navigation bar with links to the pages

Create a new HTML file called navbar.html. 

Add Bootstrap code to create a navbar.

[Bootstrap](https://getbootstrap.com/docs/5.3/components/navbar/) has examples of different styles, you can choose any.

The following is adapted from the documentation:

```html
<nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Paralympics</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link" href="#">Home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Trends</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Participants</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Locations</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```

You need to specify the URLs to use for each of `href=` as '#' just refers to the current page.

To do this, use Jinja which allows you to add the Flask 'url_for()' function. You refer to the page
using the name of the route function from main.py. For example

```html
href="{{ url_for('index') }}"
```

Modify all the `href`s in the navbar code.

Modify the base template to add the navbar before the body before the content div.

```html
<header>
    {% include 'navbar.html' %}
</header>
```

### Run the Flask app
You have written a lot of code before being in a position to run the app to check your work.

You may need to debug if the app does not work.

Run the app e.g. `flask --app src.paralympics run --debug`

Go to the URL that is shown in the terminal e.g. <http://127.0.0.1:5000>

Check the pages can all be displayed.

[Next activity](4-flask-structure.md)

