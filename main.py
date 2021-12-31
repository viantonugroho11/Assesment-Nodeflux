# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
# from flask import request
from flask import jsonify
from controller.alldataController import alldata

app = Flask(__name__)


@app.route('/', methods=['GET'])
def getall():
    return alldata()
    # return alldata()

    # return apinotif(uuid)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
