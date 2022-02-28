from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

#Work Experience
@app.route('/Humana')
def humana():
    return render_template('Humana.html')

@app.route('/Untitled')
def untitled():
    return render_template('Untitled.html')

#Tech Writing 
@app.route('/System_Analysis_Design')
def sys_analysis_des():
    return render_template('sys_analysis_des.html')

@app.route('/Visio_Database_Design')
def visio_databaseD():
    return render_template('visio_databaseD.html')

@app.route('/Case_WriteUps')
def case_writeups():
    return render_template('case_writeups.html')

#Languages / Software
@app.route('/Front_end_languages')
def front_end():
    return render_template('front_end.html')

@app.route('/Back_end_languages')
def back_end():
    return render_template('back_end.html')

@app.route('/PowerBI')
def powerBI():
    return render_template('powerBI.html')

#Personal Projects
@app.route('/Old_Bridge')
def old_bridge():
    return render_template('oldbridge.html')

@app.route('/Smart_Mirror')
def smart_mirror():
    return render_template('smart_mirror.html')

@app.route('/Eatz')
def eatz():
    return render_template('eatz.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

#Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(debug=True)