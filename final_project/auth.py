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
    c_pwd=request.form.get('p-c')
    
    if not (str(pwd) == str(c_pwd)):
        flash(' passwords dont match ','warning')
        print(' passwords dont match ')
        return redirect(url_for('auth.signup')) 

    # import re
    # checkpwd=re.match(r'[A-Za-z0-9@#$%^&+=]{6,}', str(pwd)) 
    # if checkpwd is None:
    #     flash("password doesn't meet the req",'warning')
    #     print(" passwords doesn't meet the req")
    #     return redirect(url_for('auth.signup'))

    print("password" ,pwd,email)

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
        
        max_vals=[9.000e+01,7.500e+01 ,1.970e+01 ,2.110e+03 ,2.000e+03, 4.929e+03, 9.600e+00,
 5.500e+00 ,2.800e+00 ]
        age=float(request.form.get('age'))/max_vals[0]
        totalBil=float(request.form.get('totalBil'))/max_vals[1]
        directBil=float(request.form.get('directBil'))/max_vals[2]
        totalPro=float(request.form.get('totalPro'))/max_vals[3]

        albumin=float(request.form.get('albumin'))/max_vals[4]
        ag=float(request.form.get('a/g'))/max_vals[5]
        sgpt=float(request.form.get('sgpt'))/max_vals[6]
        sgot=float(request.form.get('sgot'))/max_vals[7]
        alkphos=float(request.form.get('alkphos'))/max_vals[8]
        
        male=1
        female=1
        gender_option=request.form.get("gender")
        if gender_option is "male":
            male=1
            female=0
        else:
            male=0
            female=1
        


    # order of cols for model
    #     ['total Bilirubin', 'direct Bilirubin', 'total proteins', 'albumin',
    #    'A/G ratio', 'SGPT', 'SGOT', 'Alkphos']


        print("keys:",request.form.keys)

        print(age, totalBil,totalPro,albumin,ag,sgpt,sgot,totalPro,alkphos)

        import pickle
        from numpy import array

        from  os import getcwd
        cwd = getcwd()
        print(cwd)
        from flask import current_app
        app_name=current_app.name

        selectedModel=request.form.get('model')

        print(selectedModel,"\n",type(selectedModel))
        if not str(selectedModel).__contains__("_ga") and not "model_nn":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([totalBil,directBil,totalPro,albumin,ag,sgpt,sgot,alkphos]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))

        elif str(selectedModel) == "model_logreg_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([age, totalBil, directBil, totalPro, albumin,ag, alkphos, female, male]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))
        
        elif selectedModel == "model_nb_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([directBil, totalPro, albumin, sgpt,sgot,alkphos, female, male]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))
            

        elif selectedModel == "model_df_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([age, totalBil, directBil, ag,female]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))

        elif selectedModel == "model_adb_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([age, ag,sgpt,sgot, alkphos, female]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))

      

        elif selectedModel == "model_rf_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([age, totalBil, directBil, totalPro, albumin,ag]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))

        elif selectedModel == "model_svc_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([age, directBil, totalPro, albumin,ag, sgpt,sgot,alkphos, female]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))
        
        elif selectedModel == "model_evc_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([age, directBil, totalPro, albumin,sgpt]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))

        elif selectedModel == "model_vc_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([age, directBil, totalPro, albumin,sgpt]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)
            redirect(url_for('main.index'))
        
        elif selectedModel == "model_adb_ga":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict(array([age,ag, sgpt,sgot,alkphos, female]).reshape(1,-1))
            print("prediction is ",(prediction))
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
            from flask import flash
            flash("prediction is "+str(boolean),"success")
            

            dat=request.form.values()
            for i in dat:
                print(i)    
            redirect(url_for('main.index'))
        
        elif selectedModel == "model_nn":
            rf=pickle.load(open(str(cwd)+"/"+str(app_name)+"/"+str(selectedModel),"rb"))
            prediction=rf.predict_classes(array([age,totalBil,directBil,totalPro,albumin,ag,sgpt,sgot,alkphos,female,male]).reshape(1,-1))
            print("prediction is ",prediction)
            boolean=bool(prediction)
            print("bool prediction is ",boolean)
            
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
