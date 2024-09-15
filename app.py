from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/api/commits', methods=['GET'])
def get_commits():
    commit_data = pd.read_csv('commits.csv')
    commit_data_json = commit_data.to_dict(orient='records')
    return jsonify(commit_data_json), 200

if __name__ == '__main__':
    app.run(debug=True)
