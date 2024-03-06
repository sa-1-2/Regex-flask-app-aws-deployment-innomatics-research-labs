from flask import Flask, render_template, request

import re

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def homepage():
    ls_matched = []
    test_string = request.form.get('input_string')
    regex_val = request.form.get('regex')
    if test_string and regex_val:
        ls_matched.extend(re.findall(pattern=regex_val, string = test_string))
    return render_template('index.html', list_match = ls_matched, test_string=test_string)

    
@app.route('/email', methods=['GET', 'POST'])
def email_validate():
    if request.method == 'GET':
        return render_template('emails.html')
    
    elif request.method == 'POST':
        email_id = request.form.get('email_ids')
        email_id_regex = re.match(pattern=r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", string=email_id)
        if email_id_regex:
            if email_id_regex.group()==email_id:
                return render_template('emails.html', email=email_id)
        else:
            return "Invalid email address"
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)