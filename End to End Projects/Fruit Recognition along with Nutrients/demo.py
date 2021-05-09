import os
from uuid import uuid4
import PIL

from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # dirname--root  # abspath--entire path

classes = ['Banana','Corn','Cucumber','Grapes','Guava','Lemon','Orange','Papaya','Pomegranate','Sweet Potato']

@app.route("/")
def index():
    return render_template("check.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/') 
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print("request",request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
        #import tensorflow as tf
        import numpy as np
        from keras.preprocessing import image

        from keras.models import load_model
        new_model = load_model('fruit_file.h5')
        new_model.summary()
        test_image = image.load_img('images\\'+filename,target_size=(50,50))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = new_model.predict(test_image)
        result1 = result[0]
        for i in range(10):
    
            if result1[i] == 1.:
                break;
        prediction = classes[i]


    return render_template("res.html",image_name=filename, text=prediction)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=True)
