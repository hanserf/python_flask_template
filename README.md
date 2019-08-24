# python_flask_template
A framework for Python app development using setuptools and bdist_wheel for making a pip package.
Illustrated by running a flask application at localhost and a process of the multiprocessor class in the background.
This framework may be used in ex. logging applications og signal processing where you want to display processed data in a web application running @ localhost.


# Requirements
``` bash
sudo apt-get install\
virtualenv \
python3 \
git \
sqlite3\
```

# Python friendly editor
* Code - VSCode stripped down. if sourcing virtualenv before launcing code ```code .``` Code will install python intellisense and linter automatically for your virtual environment. 
* Pycharms - Huge but good, takes some space and fiddle to setup, but very good. Has intellisense and will force you to lint your code properly by displaying warnings when you are not compliant with best practices

# Preparation for development:
generate a virtual environment and source it.
``` bash
virtualenv -p python3 venv
source venv/bin/activate
pip install setuptools twine
```

# Install application:
``` bash
python3 setup.py install
```
# Run application
``` bash
python3 /app/main.py
```
# Development
This is a reference for development.
By copying this into your your git application you are complying to the licence.
This is a refence implementation by the author and it is relased as is without any warranty.
May be used freely, but not without acknowledging its source, the author and www.embida.no  
