from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Define API route to return the data
@app.route('/api/commits', methods=['GET'])
def get_commits():
    
    # Read the CSV file into a DataFrame
    commit_data = pd.read_csv('commits.csv')
    
    # Convert DataFrame to JSON format
    commit_data_json = commit_data.to_dict(orient='records')
    
    # Return JSON response with status code 200
    return jsonify(commit_data_json), 200

if __name__ == '__main__':
    app.run(debug=True)
