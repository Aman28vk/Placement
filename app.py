from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

app = Flask(__name__, template_folder='templates')
model_name = open('model.pkl','rb')
model=pickle.load(model_name)
model_name2 = open('model2.pkl','rb')
model2=pickle.load(model_name2)


@app.route('/')
def home():
    return render_template("home.html")



@app.route('/send', methods=['GET','POST'])
def predict():
    if request.method == "POST" :
        Name = (request.form['name'])
        Gender = request.form['gender']
        ssc_p = request.form['ssc_p']
        hsc_p = request.form['hsc_p']
        hsc_s = request.form['hsc_s1']
        degree_p = request.form['degree_p']
        degree_t = request.form['degree_t1']
        workex = request.form['workex1']
        etest_p = request.form['etest_p']
        specialisation = request.form['specialisation1']
        mba_p = request.form['mba_p']
       
        
        if Gender == 'M':
            gender = 0
        else:
            gender = 1
    
        
        if degree_t == 'Sci and Tech':
            degree_t1 = 2
        elif degree_t == 'Comm and Mgmt':
            degree_t1 = 0
        else:
            degree_t1 = 1 
    
        if workex == 'Yes':
            workex1 = 1
        else:
            workex1 = 0
        
        if hsc_s == 'Commerce':
            hsc_s1 = 1
        elif hsc_s == 'Science':
            hsc_s1 = 2
        else:
            hsc_s1 = 0
        
        if specialisation == 'Mkt and HR':
            specialisation1 = 1
        else:
            specialisation1 = 0
    
        Pred_args=float(gender),float(ssc_p),float(hsc_p),float(hsc_s1),float(degree_p),float(degree_t1),float(workex1),float(etest_p),float(specialisation1),float(mba_p)
        pred_args=np.array(Pred_args) 
        #{pred_args.reshape(1,-1)} this will convert the one dimensional numpy array into 2 dimensional i.e. row and column
        #if we dont use{pred_args.reshape(1,-1)}  the above will only be a 1 dimensional array
        pred_args=pred_args.reshape(1,-1)
        
        
        y_pred=model.predict(pred_args)
        y_pred=y_pred[0]
        salary_pred=model2.predict(pred_args)
        if y_pred == 0:
            message1= "Hello! "+ Name
            message = "You Need to work Hard !!! Chances are less"
        else:
           message1= "Hello!" + Name
           message = "You are doing well!! You will get placements and your annual salary  will be " + str(salary_pred) +"lakh"
        

        return render_template('show.html', res= message1, res2=message)
           
    
    


if __name__ == '__main__':
    app.run(debug=True)