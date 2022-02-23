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



if __name__ == '__main__':
    app.run(debug=True)