import os

from flask import render_template, request
from werkzeug.utils import redirect
from app import application,APP_ROOT
from app.process import predict_img


@application.route('/')
def home():
    return render_template('index.html',title='Home' , results='happiness bar')



@application.route("/predict")
def predict():
    return render_template("predict.html",title="Predict")

@application.route("/",methods=["GET","POST"])
def upload():
    target = os.path.join(APP_ROOT, 'temp/')
    if request.method == 'POST':
        file = request.files['img'] # 'img' is the id passed in input file form field
        filename = file.filename
        file.save("".join([target, filename])) #saving file in temp folder
        print("upload Completed") #terminal message
        # print("filename:" , filename ,"---- file:" , file , "\n redirect: " , '/prediction/{}'.format(filename))

        
        return render_template('index.html',results=prediction(filename)) 
        # return redirect('/{}'.format(filename))
        
''' for separate route instead of the home use :
 @app.route("/<filename>",methods=["GET","POST"]) '''

def prediction(filename):
    #imported process.py
    print("inside prediction filename: " , filename )
    x=predict_img(filename) #imported from process file
    print(filename , "---" , x)
    return x
    # return render_template('index.html',results=x)
