from flask import Flask , render_template , request,redirect ,url_for , flash

# THIS IS CLASS NAME WHICH WE MADE IN FORMS.PY WE HAVE IMPORTED IT INTO ANOTHER PY FILE
from forms import RegistrationForm


app = Flask(__name__)
app.secret_key = "abdullah"


@app.route("/" , methods = ["GET" , "POST"] )

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"WELCOME {name}! YOU REGISTERED SUCCESFULLY")
        return redirect(url_for("success"))
    return render_template("register.html" , form = form)

@app.route("/success")
def success():
    return render_template("success.html")

app.run(debug=True)