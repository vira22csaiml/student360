import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import request_zoho

# Set up logging
logging.basicConfig(level=logging.INFO)

# creating a Flask app 
app = Flask(__name__) 
CORS(app)

@app.route('/api/student_360', methods=['GET', 'POST'])
def input_form():
    if request.method == 'GET':
        data = "APP Works"
        logging.info("GET request received for /api/student_360")
        return jsonify({'data': data})
    
    elif request.method == 'POST':
        logging.info("POST request handled for /api/student_360")
        return jsonify({'message': 'Handled POST request'}), 200

#Go to This Link and Click Accept to Activate
#It uses the Access Token
#https://accounts.zoho.in/oauth/v2/auth?response_type=code&client_id=1000.H8U3OC2MZZNWYBTVI37HKTVHZQL2BH&scope=Desk.tickets.ALL&redirect_uri=http://127.0.0.1:5000/zoho/oauth/&state=randomstring123

@app.route('/zoho/oauth/')
def zoho_oauth_callback():
    logging.info("Received request for ZOHO OAuth callback")
    # ZOHO Data
    access_code = request.args.get('code')
    logging.info(f"Access code received: {access_code}")

    # Store or use the grant token here
    access_token = request_zoho.get_access_token(access_code)
    logging.info(f"Access token obtained: {access_token}")

    ticket_data = request_zoho.get_ticket_data(access_token)

    # Print out as CSV
    df = pd.DataFrame(ticket_data['data'])
    logging.info(f"Ticket Data:\n{df.head()}")
    df.to_csv('ticket_data_zoho.csv', index=False)

    return "Authorization successful! You can close this window."

if __name__ == '__main__': 
    logging.info("Starting Flask app")
    app.run(debug=True)