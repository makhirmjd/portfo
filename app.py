from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<page_name>')
def page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'


if __name__ == '__main__':
    app.run()


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        sep = ','
        text = sep.join(data.values())
        file = database.write(f'\n{text}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='\r\n') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data.values())
