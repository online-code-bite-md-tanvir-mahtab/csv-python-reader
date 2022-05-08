# import imp
from tkinter.messagebox import YES
import pandas as pd
from flask import Flask, render_template



app = Flask(__name__)

@app.route('/data/<int:user_input>', methods=['GET','POST'])
def home(user_input):
    # going to read the csv file

    csv_path = 'demoreader/Order by file number - result_file_number.csv'

    data = pd.read_csv(csv_path)

    if user_input in data['File number']:
        return f"Rank : {data['Rank'][user_input-1]}"
    else:
        return f"Nothing found"

# print(data.indexof(241))


if __name__ == '__main__':
    app.run(debug=True)
