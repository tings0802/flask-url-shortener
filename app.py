import json, random, string

from flask import Flask, render_template, request, redirect


class JsonDatabase(object):
    def __init__(self, filename) -> None:
        self.filename = filename
        with open(filename, 'r') as file:
            self.data = json.loads(file.read())
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        db.data[key] = value
        with open(self.filename, 'w') as file:
            file.write(json.dumps(self.data, indent=4))

    def get_key(self, target):
        for key, value in self.data.items():
            if value == target:
                return key
        
        key = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
        while key in self.data:
            key += random.choice(string.ascii_lowercase)
        
        self[key] = target
        return key


db = JsonDatabase('data.json')
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    url = ''
    if request.method == 'POST' and request.form['url']:
        origin = request.form['url']
        key = db.get_key(origin)
        url = f'{request.host_url}{key}'
    return render_template('index.html', url=url)


@app.route('/<key>', methods=['GET'])
def redirect_url(key):
    return redirect(db.data[key])


if __name__ == '__main__':
    app.run()
