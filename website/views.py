from flask import Blueprint, render_template,request,redirect,url_for,jsonify,session
#from flask_login import  login_required, current_user
views= Blueprint('views',__name__)
from website import authenticate
import pyrebase
import random






# Configure Firebase
global config
config = {
  "apiKey": "AIzaSyA7GweUH8Z8Dy_eWJVz2ohpfMaKK-XNTs8",
  "authDomain": "qrbasedordering.firebaseapp.com",
  "databaseURL": "https://qrbasedordering-default-rtdb.firebaseio.com",
  "projectId": "qrbasedordering",
  "storageBucket": "qrbasedordering.appspot.com",
  "messagingSenderId": "364448122744",
  "appId": "1:364448122744:web:476bff4d8e32a9ecc26a8d",
  "measurementId": "G-3HVXNBTYDH"
}

firebase = pyrebase.initialize_app(config)


#creating Order function
def placeOrder(iname,price,qty):
    db = firebase.database()
    title=iname
    price=price
    qty=qty
    orderID = session.get('OrderID')
    data={"item":title,"price":price,"Quantity":qty}
    db.child("Orders").child(orderID).child("items").set(data)




def generate_random_number():
    unique_number = random.randint(100, 999)
    return unique_number







@views.route('/dbupd', methods=['POST'])
def update_database():
    tamt = request.form.get('tamt')
    qty=request.form.get('qty')
    itemName=title
    placeOrder(itemName,tamt,qty)
    return render_template("payment.html",tamt=tamt)





@views.route("/qrpage")
def index():
    return render_template("index.html")


@views.route("/payment")
#@login_required
def payment():
    return render_template("payment.html")



@views.route("/cart")
def cart_func():
    image=request.args.get('image')
    global title
    title=request.args.get('title')
    price=request.args.get('price')
    print(title)
    no=generate_random_number()
    session['OrderID']=no
    return render_template("newOrder.html",title=title,price=price,no=no)








'''@views.route('/qrpage')
def index():
  return  render_template("index.html")

@views.route('/generate', methods=['POST'])
def generate():
    # Get the data from the form
    data = request.form['data']

    # Generate the QR code image
    img = qrcode.make(data)

    # Serve the image as a PNG file
    return serve_pil_image(img)
   



# Define a function to serve a PIL image as a PNG file
def serve_pil_image(pil_img):
    from io import BytesIO
    from flask import send_file
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')'''
    
