from flask import Flask, render_template
import time

app = Flask(__name__)

# DDoS prevention system check
def ddos_prevention_check(requests_per_second):
    if requests_per_second > 1000:
        return True
    return False

# Simulate request processing
def process_request():
    # Simulate processing time
    time.sleep(0.01)
    return "Request processed successfully"

@app.route('/')
def index():
    # Simulate request processing
    response = process_request()

    # Check for DDoS attack
    if ddos_prevention_check(1000):  # Replace with actual request count
        return render_template('ddos_warning.html')

    return response

@app.route('/ddos_warning')
def ddos_warning():
    return render_template('ddos_warning.html')

if __name__ == '__main__':
    app.run()
