from flask import Flask, request, redirect, render_template
import random 
import string
from model import(
    init_db, 
    insert_url, 
    delete_url, 
    get_all_urls, 
    get_url, 
    increment_visit_count
    )

app = Flask(__name__)

init_db()

def generate_short_code(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))



@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        insert_url(original_url, short_code)
        return redirect("/")
    all_urls = get_all_urls()
    return render_template('index.html', all_urls=all_urls)

    return 'Hello to Python learners!'

@app.route("/about") #is the route is through /about 
def about():
    return 'Hello to Python learners on the about page!'

@app.route("/<short_code>")
def redirect_path(short_code):
    url_data = get_url(short_code)

    if not url_data:
        return render_template("404.html"), 404

    increment_visit_count(short_code)
    return redirect(url_data[0])


@app.route("/delete/<short_code>", methods=['POST']) 
def delete_this_url(short_code):
    delete_url(short_code)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)