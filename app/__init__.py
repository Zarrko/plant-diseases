import os
from flask import Flask, flash, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
import firebase_admin
from firebase_admin import credentials, storage

from instance.config import app_config
from helpers.validate_file_type import allowed_file

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred,  {
    'storageBucket': 'plant-diseases-zd.appspot.com'
})
bucket = storage.bucket()

UPLOAD_FOLDER = 'images'

def create_app(config_mode):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_mode])
  app.config.from_pyfile('config.py')
  app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

  @app.route('/', methods=['GET', 'POST'])
  def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            blob = bucket.blob(filename)
            # blob.upload_from_file(file_obj=file)
        if file and  not allowed_file(file.filename):
           flash('please select an image')

    return render_template('upload.html')

  return app
