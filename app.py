from flask import Flask, render_template,url_for,request,redirect

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('main.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = ['saimugil','shravan']
        if username not in users:
           
            return redirect(url_for('home'))

        
        return 'Signup successful! Please log in.'
    
   

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8000)
