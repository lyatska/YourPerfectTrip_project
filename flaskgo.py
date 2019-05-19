from flask import Flask, render_template, request
from main import mappy1, mappy2
from main import is_valid

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    """
    Returns the initial site page.
    """
    return render_template('site.html')


@app.route('/hotels', methods=['POST'])
def hotels():
    """
    Returns the hotel search page.
    """
    return render_template('besthotels.html')


@app.route('/restaurants', methods=['POST'])
def restaurants():
    """
    Returns the restaurants search page.
    """
    return render_template('bestrestaurants.html')

@app.route('/specialhot', methods=['POST'])
def specialhot():
    """
    Returns the map page with the best proposition of hotel.
    """
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
    """
    Returns the map page with the best pproposition of restaurants.
    """
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

