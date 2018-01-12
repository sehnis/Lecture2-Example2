from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Here's the main page. <a href='http://localhost:5000/seeform'>Click here to see the form</a>."

lastpost = ''
lastget = ''

@app.route('/seeform',methods=["GET","POST"])
def see_form():
    if request.method == "POST":
        global lastpost
        lastpost = request.form['phrase']
        # OR: request.form.get('phrase', '')
    if request.method == "GET":
        global lastget
        lastget = request.args.get('phrase','')
    
    formone = """<br><form action="/seeform" method='POST'> Enter a phrase to use the POST Method: <br>
<input type="text" name="phrase">&nbsp;Last POST request: <a style="color:green;">{}</a><br>
<input type="submit" value="Submit"><br><br></form>""".format(lastpost)
    formtwo = """<form action="/seeform" method='GET'> Enter a phrase to use the GET Method: <br>
<input type="text" name="phrase">&nbsp;Last GET request: <a style="color:green;">{}</a><br>
<input type="submit" value="Submit"><br><br></form>""".format(lastget)
    formstring = formone + formtwo
    return formstring





if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
