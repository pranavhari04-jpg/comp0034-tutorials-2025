# 4. Streamlit app directory structure

Streamlit apps are run as a script. This does not prevent code being structured into other modules
or packages. As your app grows consider writing code as functions that can be moved to other
modules, e.g. `helpers.py` or `utils.py`. You can also place any static files such as images in
another directory.

```text
project_folder_name/
 ├── .venv/
 ├── src/
     └── paralympics
        ├── __init__.py
        ├── app.py          # Main streamlit app script
        ├── helpers.py          # Main streamlit app script
        └── .streamlit/     
            └── config.toml # Streamlit config e.g. to alter colours and styles
├── .gitignore
├── pyproject.toml
└── README.md
```

If you create a multipage app then this is the folder structure
for [tutorial app](https://docs.streamlit.io/develop/tutorials/multipage) in the
streamlit documentation:

```text
app_package/
├── admin
│   ├── admin_1.py
│   └── admin_2.py
├── images
│   ├── horizontal_blue.png
│   └── icon_blue.png
├── request
│   ├── request_1.py
│   └── request_2.py
├── respond
│   ├── respond_1.py
│   └── respond_2.py
├── settings.py
└── streamlit_app.py
```

[Next activity](5-coursework.md)