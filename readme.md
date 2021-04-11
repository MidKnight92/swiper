# Swiper

## Setup
The first thing to do is to clone this repository:

```sh
$ git clone https://github.com/MidKnight92/swiper.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv -p python3 env
$ source env/bin/activate
```
Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by `virtualenv`

Deactivate and reactivate a virtual environment:
```sh
// Deactivate
(env)$ deactivate 

// Reactivate
$ source env/bin/activate
```

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```