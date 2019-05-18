from flask import Flask, render_template, request
from main import mappy1, mappy2
from main import is_valid

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('site.html')


@app.route('/hotels', methods=['POST'])
def hotels():
    return render_template('besthotels.html')


@app.route('/restaurants', methods=['POST'])
def restaurants():
    return render_template('bestrestaurants.html')

@app.route('/specialhot', methods=['POST'])
def specialhot():
    city = request.form['city']
    if is_valid(city) == True:
        res = mappy1(city,20190708,20190709)
        if res != None:
            return res
        else:
            return render_template("besthotels.html")
    else:
        return render_template('besthotels.html')
    

@app.route('/specialres', methods=['POST'])
def specialres():
    city = request.form['city']
    if is_valid(city) == True:    
        res = mappy2(city)
        if res != None:
            return res
        else:
            return render_template("bestrestaurants.html")
    else:
        return render_template("bestrestaurants.html")
        
if __name__ =="__main__":
    app.run()

