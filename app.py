'''
    Web sederhana pemetaan kecelakaan aja
    mirip first news app
'''
# app.py >> konfigurasi untuk server & route ada di sini

import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path = './static/data-bencana-kecelakaan-transportasi-2011-2014.csv'
    csv_file = open(csv_path, 'r')
    csv_obj  = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list = object_list)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
