from flask import Flask, request, jsonify
import os
import logging

app = Flask(__name__)

# Security Issue: Hardcoded secret key
app.secret_key = 'mysecretkey'  # This should be an environment variable

# Duplication Issue: Similar functions for different endpoints
def get_user_data(user_id):
    # Simulating a database call
    return {"user_id": user_id, "name": "User " + str(user_id)}

def get_admin_data(admin_id):
    # Simulating a database call
    return {"admin_id": admin_id, "name": "Admin" + str(admin_id)}

@app.route('/user/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    # Reliability Issue: No error handling for invalid user_id
    user_data = get_user_data(user_id)
    return jsonify(user_data)

@app.route('/admin/<int:admin_id>', methods=['GET'])
def admin_profile(admin_id):
    # Reliability Issue: No error handling for invalid admin_id
    admin_data = get_admin_data(admin_id)
    return jsonify(admin_data)

@app.route('/login', methods=['POST'])
def login():
    # Security Issue: No input validation
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':  # Hardcoded credentials
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/data', methods=['GET'])
def get_data():
    # Maintainability Issue: Complex logic in a single function
    data = []
    for i in range(10):
        data.append({"id": i, "value": "Value" + str(i)})
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

print("OK Sonar test")