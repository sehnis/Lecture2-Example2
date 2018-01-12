from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main_page():
    return "Here's the main page. <a href='http://localhost:5000/seeform'>Click here to see the form</a>."

@app.route('/seeform',methods=["GET","POST"])
def see_form():
    formstring = """<br><form action="/seeform" method='POST'> Enter a phrase to use the POST Method: <br>
<input type="text" name="phrase"><br>
<input type="submit" value="Submit"><br><br></form>

<form action="/seeform" method='GET'> Enter a phrase to use the GET Method: <br>
<input type="text" name="phrase"><br>
<input type="submit" value="Submit"><br><br></form>
""" ## HINT: In there ^ is where you need to add a little bit to the code...
    if request.method == "POST":
        formstring += ("<br>POST USED<br>You entered: " + request.form['phrase'])
        # Add more code here so that when someone enters a phrase, you see their data (somehow) AND the form!
    if request.method == "GET":
        	formstring += ("<br>GET USED<br>The data from the url is: " + request.args.get('phrase',''))
    return formstring





if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
