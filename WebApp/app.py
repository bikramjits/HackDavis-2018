from flask import render_template
from flask import Flask
from models import *
app = Flask(__name__)
@app.route('/')
def index():
  # school_count = School.select().count()
  # schools = School.select().order_by(School.school_name.asc())
  return render_template('index.html')
@app.route('/schools/clemente')
def school():
    return render_template('school.html')
if __name__ == '__main__':
    app.run(debug=True)
