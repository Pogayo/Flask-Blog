from flask import Flask, render_template,url_for

app = Flask(__name__)

posts=[
    {
        "Author": "Perez Ogayo",
        "Title": "First Post",
        "Content": "Post 1 content lorem",
        "Date_Posted":"20-12-2018"

    },
{
        "Author": "Faith Ogayo",
        "Title": 'Second Post',
        "Content": "Post 2 content lorem",
        "Date_Posted":"20-12-2018"

    },
{
        "Author": " Atieno Ogayo",
        "Title": 'Third Post',
        "Content": "Post 3 content lorem",
        "Date_Posted":"20-12-2018"

    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)
@app.route('/About')
def about():
    return render_template('about.html',title='About')


@app.route('/Contact us')
def contact_me():
    return 'Contact me here'
if __name__ == '__main__':
    app.run(debug=True)
