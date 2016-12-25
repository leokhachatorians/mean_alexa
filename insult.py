import logging
import random
from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, "/")

@ask.launch
def launch():
    return statement("I really don't like you")

@ask.intent("InsultIntent",
        mapping={'name': 'Name'})
def insult(name):
    num_insults = 6
    insult_index = random.randint(0,num_insults - 1)
    insult_text = render_template('insult_{}'.format(insult_index), Name=name)
    return statement(insult_text)



if __name__ == '__main__':
    app.run(debug=True)
