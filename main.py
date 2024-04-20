from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

@app.route('/', methods=['GET', 'POST'])
def index():
    choices = ['rock', 'paper', 'scissors', 'fire', 'water']
    outcomes = {
    'rock': {'rock': 'Tie', 'paper': 'You lose', 'scissors': 'You win', 'fire': 'You win', 'water': 'You win'},
    'paper': {'rock': 'You win', 'paper': 'Tie', 'scissors': 'You lose', 'fire': 'You lose', 'water': 'You lose'},
    'scissors': {'rock': 'You lose', 'paper': 'You win', 'scissors': 'Tie', 'fire': 'You lose', 'water': 'You win'},
    'fire': {'rock': 'You lose', 'paper': 'You win', 'scissors': 'You win', 'fire': 'Tie', 'water': 'You lose'},
    'water': {'rock': 'You lose', 'paper': 'You win', 'scissors': 'You lose', 'fire': 'You win', 'water': 'Tie'}
}


    
    if 'user_choice' not in session or 'computer_choice' not in session or 'result' not in session:
        session['user_choice'] = None
        session['computer_choice'] = None
        session['result'] = None

    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(choices)
        result = outcomes[user_choice][computer_choice]

        session['user_choice'] = user_choice
        session['computer_choice'] = computer_choice
        session['result'] = result

        return redirect(url_for('index'))

    return render_template('index.html', user_choice=session.get('user_choice'), 
                           computer_choice=session.get('computer_choice'), 
                           result=session.get('result'), choices=choices)

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    session.pop('user_choice', None)
    session.pop('computer_choice', None)
    session.pop('result', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
