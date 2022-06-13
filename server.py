from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app = Flask(__name__)
app.secret_key = 'kendra counter assignment'

@app.route('/')
def index():
    #session['key_name'] += 1
    #if 'key_name' in session:
    #    print('key exists!')
    #else:
    #    print("key 'key_name' does NOT exist")
    #return render_template('index.html')

    if 'key_name' in session:
        session['key_name'] += 1
    else:
        session['key_name'] = 1

    return render_template('index.html')

@app.route('/counter')
def manipulate_counter(counter):
    session['key_name'] += 1
    return redirect('/')

@app.route('/reset')
def reset_counters():
    session.clear()

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
