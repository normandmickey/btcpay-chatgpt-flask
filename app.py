from flask import Flask, request, jsonify, render_template
import openai
import os, json
from dotenv import load_dotenv
import btcpay
from flask_csp.csp import csp_header
load_dotenv()

btcpay.api_key = os.environ.get("BTCPAY_API_KEY")
btcpay.host_url = os.environ.get("BTCPAY_HOST_URL")
btcpay.store_id = os.environ.get("BTCPAY_STORE_ID")


# Set up Flask app and OpenAI API key
app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def test_create_invoice():
    test_data = {
        "metadata": {
            "orderId": "03ea7e71-2e3a-4ed6-859f-781241784357"
        },
        "checkout": {
            "speedPolicy": "MediumSpeed",
            "defaultPaymentMethod": "BTC",
            "expirationMinutes": 90,
            "monitoringMinutes": 90,
            "paymentTolerance": 0,
            "redirectAutomatically": True,
            "requiresRefundEmail": False
        },
        "amount": "0.01",
        "currency": "USD"
    }

    r = btcpay.Invoices.create_invoice(**test_data)
    r_json = json.dumps(r)
    r_json = json.loads(r_json)
    invoiceId = r_json["id"]
    return invoiceId


# Define route to render HTML template
@app.route("/")
#@csp_header({'script-src':"'self' 'wasm-unsafe-eval' 'unsafe-inline' https://code.jquery.com https://botomatic.co",'style-src':"'self' 'unsafe-inline'",'frame-src':"'self' https://btcpay.btcpi.com"})
def home():
    return render_template("index.html")

# Define route for API endpoint
@app.route("/api", methods=["POST"])
def api():
    # Get question from form data
    question = request.json["question"]
    
    # Use OpenAI to generate answer
    #response = openai.Completion.create(
    #    engine="text-davinci-003", prompt=f"Q: {question}\nA:", max_tokens=3000, n=1, stop=None, temperature=0.7,
    #)
    #answer = response.choices[0].text.strip()
    
    # Use OpenAI ChatCompletion
    response = openai.ChatCompletion.create(
      model="gpt-4",
      max_tokens=500,
      messages=[
        {"role": "user", "content": question}
      ]
    )
    
    answer = response.choices[0].message.content
    
    # Return answer as JSON
    return jsonify({"answer": answer})

@app.route("/createInvoice", methods=["POST"])
def createInvoice():
    invoiceId = test_create_invoice()
    return jsonify(
        id=invoiceId
    )

# Run app
if __name__ == "__main__":
    app.run()
