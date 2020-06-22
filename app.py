from flask import Flask, render_template, url_for, flash, redirect


app = Flask(__name__)




all_reminders = [
    {
        'author': 'kasem',
        'title': 'remind 1',
        'content': 'this is the first remind'
               
    },
    {
        'author': 'kasem boutou',
        'title': 'remind 2',
        'content': 'this is the second remind'
               
    }
]

    

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/reminders")
def reminders():
    return render_template('reminders.html', reminders=all_reminders)




if __name__ == '__main__':
    app.run(debug=True)