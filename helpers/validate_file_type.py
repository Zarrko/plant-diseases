""" allow specific file types """
ALLOWED_EXTENSIONS = set(['png', 'jpeg', "jpg"])

def allowed_file(filename):
  return '.' in filename and \
          filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS