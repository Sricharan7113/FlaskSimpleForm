from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
@app.route('/index')


def home():
    #return "<h1>Helo World </h1>"
    return render_template("index.html")

@app.route("/Confirmation",methods=['POST','GET'])

def register():
    if request.method =='POST':
        Name = request.form.get('Name')
        Mail = request.form.get('Mailid')
        return render_template('Confirmation.html' , Name=Name , Mail=Mail)

if(__name__=="__main__"):
    app.run(debug=True)
