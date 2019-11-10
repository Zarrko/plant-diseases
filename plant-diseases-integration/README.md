# Plant Diseases Integration API
Handles Prediction of Plant Images by the Model

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Pre-requisites
Any editor of your choice can be used for this application.

1. [Python](https://www.python.org)

   This project has been built with Python 3.7. Ensure that you install this version of Python as outlined in the
   link provided [here](https://www.python.org/downloads/)

2. [Pip](https://pip.pypa.io/en/stable/)

   This is a package manager for Python applications and will be useful when handling dependencies
   for this application. Installations instructions can be found in the link int the title.

3. [venv](https://docs.python.org/3/library/venv.html)
    
    The venv module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories.
    
### Running The Application
I am no Flask Guru, but this is how I run the application locally. (Any Suggestions to improve this are highly recommended).

1. Create Env for this Project. See `venv` above. This is a one time thing. Then `source venv/bin/activate`. Install all Dependencies

2. Run `/app/__init__.py`

3. Create an `.env` file on Project Root and add `FLASK_ENV=development`

4. If Using PyCharm, mark `plant-diseases-integration` as `sources-root`. (Help Wanted on how to run the Project without an IDE i.e On Terminal)

5. Test as follows on Insomnia. 
    
    ```
   Example Payload
       {
            "path": "/Downloads/maize_rust.png"
       }
   
   URL (POST)
   http://127.0.0.1:5000/images
   ```   

### Pending Items
This Project is still in its early stages and may significantly change with time

1. Model Improvements
    
    Based on insights from testing results, adjust model

2. Database Integration
    
    Integrate with a Database for Image Storage Purposes. 

3. Tests
    
    Add Tests to the Project. 


## Built With

1. [Python](https://www.python.org/) - Source language
2. [Flask](http://flask.pocoo.org/) - Python Web Framework
