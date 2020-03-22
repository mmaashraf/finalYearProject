from flask import Blueprint,render_template,redirect,url_for,request,flash
from . import db


from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user
from flask_login import logout_user, login_required

# from models import User

auth=Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    

    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    from .models import User

    user = User.query.filter_by(email=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials

    login_user(user, remember=remember)    

    
    return redirect(url_for('main.profile'))

@auth.route("/signup")
def signup():
    return render_template("signup.html")

@auth.route("/signup",methods=['POST'])
def signup_post():

    email=request.form.get('email')
    name=request.form.get('name')
    pwd=request.form.get('password')

    from .models import User


    user=User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    new_user=User(email=email,name=name,password=generate_password_hash(pwd, method='sha256'))

    db.session.add(new_user)
    db.session.commit()


    return redirect(url_for('auth.login'))

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route("/predict",methods=['GET','POST'])
def predict():
    if request.method=='POST':
        print("need to use ml model ")
        
        max_vals=[7.500e+01 ,1.970e+01 ,2.110e+03 ,2.000e+03, 4.929e+03, 9.600e+00,
 5.500e+00 ,2.800e+00 ]

        totalBil=float(request.form.get('totalBil'))/max_vals[0]
        directBil=float(request.form.get('directBil'))/max_vals[1]
        totalPro=float(request.form.get('totalPro'))/max_vals[2]

        albumin=float(request.form.get('albumin'))/max_vals[3]
        ag=float(request.form.get('a/g'))/max_vals[4]
        sgpt=float(request.form.get('sgpt'))/max_vals[5]
        sgot=float(request.form.get('sgot'))/max_vals[6]
        alkphos=float(request.form.get('alkphos'))/max_vals[7]
        


    # order of cols for model
    #     ['total Bilirubin', 'direct Bilirubin', 'total proteins', 'albumin',
    #    'A/G ratio', 'SGPT', 'SGOT', 'Alkphos']




        print(totalBil,totalPro,albumin,ag,sgpt,sgot,totalPro,alkphos)

        import pickle
        from numpy import array

        rf=pickle.load(open("/home/ashraf/Desktop/final_project/model_rf","rb"))
        prediction=rf.predict(array([totalBil,directBil,totalPro,albumin,ag,sgpt,sgot,alkphos]).reshape(1,-1))
        print("prediction is ",(prediction))
        boolean=bool(prediction)
        from flask import flash
        flash("prediction is "+str(boolean),"success")
        

        dat=request.form.values()
        for i in dat:
            print(i)
        redirect(url_for('main.index'))
        
    return render_template("form.html")

# @auth.route("/value",methods=['POST'])
# def value():
#     val=request.form.get('albumin')
#     print(val)
#     return redirect(url_for('main.login'))
