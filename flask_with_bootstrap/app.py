from flask import Flask, render_template
app=Flask(__name__)

posts = [
    {
        'author':   'Krystian Osiekowicz',
        'title':    'First Blog Post',
        'date':     '28-12-2019',
        'contents': 'This is my first blog entry'
    },
    {
        'author':   'Krystian Osiekowicz',
        'title':    'Second Blog Post',
        'date':     '28-12-2019',
        'contents': 'This is my second blog entry'        
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def abount():
    return render_template('about.html', title='About')

if __name__=='__main__':
    app.run(debug=True)