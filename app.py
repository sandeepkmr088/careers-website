from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': ' Bengaluru, India',
    'salary': 'Rs. 10,00000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': ' Pune, India',
    'salary': 'Rs. 13,00000'
  },
  {
    'id': 3,
    'title': 'Data Administrator',
    'location': ' Bengaluru, India',
    'salary': 'Rs. 12,00000'
  },
  {
    'id': 4,
    'title': 'Project Engineer',
    'location': ' Delhi, India',
    'salary': 'Rs. 14,00000'
  },
  {
    'id': 5,
    'title': 'Project Engineer',
    'location': ' Kolkata, India',
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
