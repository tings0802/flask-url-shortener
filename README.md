# flask-url-shortener

A very simple URL shortener using Python Flask

## Setup

It's recommended to run this app in a virtual environment.

```shell
python -m venv .env
source .env/bin/activate
```

Then install the dependencies with pip.

```shell
pip install Flask
```

Set the environment variable as the following
```
export FLASK_ENV=development
```

## Usage

Run the app with

```shell
flask run
```

Navigate [localhost:5000](http://127.0.0.1:5000) on your web browser. Then you can start to use the URL shortener app.

To stop the app, just hit `Ctrl` + `C`.

Finally, you can leave the virtual environment with the following command.

```shell
deactivate
```
