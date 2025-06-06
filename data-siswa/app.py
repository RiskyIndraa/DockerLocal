from flask import Flask, render_template

app = Flask(__name__)

data_siswa = [
    {"nama": "Andi", "kelas": "10A"},
    {"nama": "Budi", "kelas": "10B"},
    {"nama": "Cici", "kelas": "10A"},
]

@app.route('/')
def index():
    return render_template('index.html', siswa=data_siswa)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
