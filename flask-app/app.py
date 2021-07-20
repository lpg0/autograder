import sys
from subprocess import Popen, PIPE, STDOUT
import json
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
app = Flask(__name__)

@app.route('/submission', methods = ['POST', 'GET'])
def submission(result=None):
    ans = None
    if request.method == 'POST':
        n1 = request.form['n1']
        n2 = request.form['n2']
        #ans = None
        #try: 
        #ans = subprocess.check_call(["python", "subtract.py", n1, n2])
        p = Popen(['python', 'subtract.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        ans = p.communicate(input=(n1+"\n"+n2).encode())[0]
        ans = ans.split()[4].decode()
        #except subprocess.CalledProcessError as e:
        #    ans = e.output  
    return render_template('submission_page.html', result=ans)

if __name__ == '__main__':
    app.run(debug = True,host="0.0.0.0")

