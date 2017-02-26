# from forms import SignupForm, LoginForm
import MySQLdb
from flask import Flask, render_template, request, session
app = Flask(__name__)

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('user_name', None)
    return redirect(url_for('index'))

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    prevdonation = request.args.get('prevdonation')
    if prevdonation == None:
        return render_template('home.html')

    if prevdonation == "Yes":
        return render_template("home1.html")
    else:
        return render_template("home2.html")

@app.route('/home1', methods=['GET','POST'])

def home1():
    prevdonation = request.args.get('prevdonation')
    global blood_type 
    global zipcode
    zipcode = request.args.get('zipcode')
    blood_type = request.args.get('bloodType')
    print blood_type
    print zipcode
    if prevdonation == "Yes":
        return render_template("home1.html")
    else:
        return render_template("home2.html")

@app.route('/home2', methods=['GET','POST'])
def home2():
    global blood_type 
    blood_type = request.args.get('bloodType')
    print blood_type
    return render_template('home2.html')

@app.route('/home3', methods=['GET','POST'])
def home3():
    health = request.args.get('generalHealth')
    # if health == None:
    #     return render_template('noneligible.html')
    print health

    if health == "Yes":
        return render_template("home3.html")
    else:
        return render_template("noneligible.html") 


@app.route('/hospitalsignup', methods=['GET','POST'])
def hospitalsignup():
    return render_template('hospitalsignup.html')

@app.route('/eligibility', methods=['GET','POST'])
def eligibility():
    age = int(request.args.get('age'))
    gender = request.args.get('gender')
    weight = int(request.args.get('weight'))
    height = int(request.args.get('height'))
    print age
    print gender
    print type(weight)
    print weight > 110
    print 34 > 110
    print weight == 34
    print weight < 110

    if weight < 110:
        return render_template('noneligible.html')
    else: 
        if age >= 16 and age <= 18: 
            if gender == "Male" :
                if height >= 60 :
                    return render_template('eligibility.html')
                elif height == 59 :
                    if weight >= 114:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
                elif height == 58 :
                    if weight >= 118:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
            elif gender == "Female": 
                if height >= 66 : 
                    return render_template('eligibility.html')
                elif height == 65 :
                    if weight >= 115:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
                elif height == 64 :
                    if weight >= 120:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
                elif height == 63 :
                    if weight >= 124:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
                elif height == 62 :
                    if weight >= 129:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
                elif height == 61 :
                    if weight >= 133:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
                elif height == 60 :
                    if weight >= 138:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
                elif height == 59 :
                    if weight >= 142:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
                elif height == 58 :
                    if weight >= 146:
                        return render_template('eligibility.html')
                    else:
                        return render_template('noneligible.html')
        elif age > 18:
            return render_template('eligibility.html')



@app.route('/hospitalsearch', methods=['GET','POST'])
def hospitalsearch():
    global zipcode
    global blood_type
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="", db="blood_donation")         

    cur = db.cursor()

    cur.execute("SELECT * FROM inventory LEFT JOIN hospitals on inventory.id = hospitals.id WHERE zipcode="+zipcode)

    need = False
    index=0
    if blood_type == "O+":
        index=1
    elif blood_type == "O-":
        index=2
    elif blood_type == "A+": 
        index=3
    elif blood_type == "A-": 
        index=4
    elif blood_type == "B+": 
        index=5
    elif blood_type == "B-":
        index=6
    elif blood_type == "AB+": 
        index=7
    elif blood_type == "AB-":
        index=8
    for row in cur.fetchall():
        if row[index] < 500: 
            need = True

    db.close()
    return render_template('hospitalsearch.html', result=need, blood_type=blood_type, zipcode=zipcode)

@app.route('/noneligible', methods=['GET','POST'])
def noneligible():
    return render_template('noneligible.html')

@app.route('/nearby', methods=['GET','POST'])
def nearby():
    return render_template('nearby.html')


if __name__ == "__main__":
    app.run()