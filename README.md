# Fruit Garden
Webapplication with Django backend and VueJs frontend.

## Description

We have a fruit garden with apple, pear and peach trees.
We can take orders to assemble fruit baskets. (1 order is 1 fruit basket) In an order it's not necessary to request all type of fruits, and the maximum number per fruit is 100.

> order 1: 50 apple, 90 pear
order 2: 25 apple, 25 pear, 25 peac

We have to go out to the garden to collect the fruits, but unfortunately 
we can only collect maximum 50 piece of fruit in one round.

>  round 1: 10 apple, 20 pear, 20 peach
 round 2: 50 apple

The baskets needs to be filled in the order of the basket's request date, and
we would like to track from which collection round we got the fruits.

## Installation

Install the dependencies and devDependencies and start the server.

#### Backend
in the `backend` directory, and after activating the venv run:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata Fruit
python manage.py runserver
```
#### Frontend
It requires [Node.js](https://nodejs.org/).

move to `frontend` directory, then run:
```sh
npm install
npm run dev
```
