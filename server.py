from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)

@app.route("/")
def home_page():
   return render_template("index.html")

@app.route("/<string:page_name>")
def about_page(page_name):
   return render_template(page_name)


def write_to_file(data):
   with open('database.txt', mode='a') as database:
      email = data["email"]
      subject = data["subject"]
      message = data["message"]
      file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
   with open('database.csv',newline='', mode='a') as databasedf:
      email = data["email"]
      subject = data["subject"]
      message = data["message"]
      csv_writer = csv.writer(databasedf, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   if request.method == "POST":
      data = request.form.to_dict()
      write_to_csv(data)
      return redirect("thankyou.html")
   else:
      return "Somethong went wrong. Try again..."


