# mvc_template
A simple PySide/sqlite3 Model-View-Controller pattern MVC template. Very basic functionality.

## Usage

> \ run.py

Launch the application.

> controller  \ __init__.py

The controller creates an instance of the model and view classes. Should take user input, retrieve data from the model, and pass that to the view to present to the UI.

> model \ __init__.py

Retrieves/inserts/deletes data as instructed by the controller. Very basic sqlite3 methods included, easily swapped out for any other database ORM.

> view \ __init__.py

The presentation layer. Inherit the Qt ui file, configure widgets, format data retrieved by the controller for display.

> view \ ui \ main.ui

Template Qt Designer ui form.

> view \ ui \ build_ui.bat

Shortcut batch to convert Qt Designer ui file to .py.
