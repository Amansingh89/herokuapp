from flask import Flask, render_template

app = Flask(__name__)

vehicles = [{
    'company': 'Honda',
    'model': 'civic',
    'year': '2015'
},
    {
        'company': 'Ford',
        'model': 'Mondeo',
        'year': '2016'
    },
    {
        'company': 'Cooper',
        'model': 'Mini',
        'year': '2014'
    },
]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/cars')
def list_company():
    return render_template('index.html', vehicles=vehicles)


if __name__ == '__main__':
    app.run()