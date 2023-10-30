from flask import Flask, render_template
from pydebugtoolkit.forms import ProcessForm
from pydebugtoolkit import ProcessMonitor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ProcessForm()
    if form.validate_on_submit():
        process_name = form.process_name.data
        process_monitor = ProcessMonitor(process_name)
        process_monitor.start_monitoring()
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
