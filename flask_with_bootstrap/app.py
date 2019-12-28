from flask import Flask, render_template
app=Flask(__name__)

posts = [
    {
        'author':   'Krystian Osiekowicz',
        'title':    'First BLog Post',
        'date':     '28-12-2019'
    },
    {
        'author':   'Krystian Osiekowicz',
        'title':    'Second BLog Post',
        'date':     '28-12-2019'        
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def abount():
    return render_template('about.html')

if __name__=='__main__':
    app.run(debug=True)