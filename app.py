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

@app.route('/System_Analysis_Design')
def sys_analysis_des():
    return render_template('sys_analysis_des.html')

if __name__ == '__main__':
    app.run(debug=True)