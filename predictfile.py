import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

from keras.models import Sequential, load_model
import keras, sys
from PIL import Image
import numpy as np 


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])
classes = ['monkey', 'boar', 'crow']

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
image_size = 50

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            model = load_model('./CNNLossAcc/animal_cnn100.h5')

            image = Image.open(filepath)
            image = image.convert('RGB')
            image = image.resize((image_size, image_size))
            data = np.asarray(image)
            X = []
            X.append(data)
            X = np.array(X)
            
            result = model.predict([X])[0]
            predicted = result.argmax()
        
            percentage = int(result[predicted] * 100)

            outputresult = classes[predicted] + str(percentage) + ' %'
            ret = '''<!doctype html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Upload & Classify!</title></head>
    <link rel="stylesheet" href="style.css" type="text/css">
    <body>
    <div style="text-align:center;">
    ''' + '<p>Uploaded Image: ' + filename + '<br>' + '<img src="' + filepath + '" class="output"> </p><br>' + '<p>' + 'result: ' + outputresult +     '''
    </div>
    </form>
    </body>
    </html>'''
            return ret


            # return redirect(url_for('uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Upload & Classify!</title></head>
    <body>
    <h1>Upload & Classify!</h1>
    <form method = post enctype = multipart/form-data>
    <p><input type=file name=file>
    <input type=submit value=Upload>
    </form>
    </body>
    </html>
    '''

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
