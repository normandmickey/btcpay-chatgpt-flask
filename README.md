# btcpay-chatgpt-flask
This project is a demonstration of how to add a Bitcoin Lighting Paywall for the OPENAI ChatGPT API using BTCPayServer and Flask.  


## Getting Started

### Dependencies

* OPENAI API Key
* BTCPayServer Instance
* Ubuntu VPS 

### Installing

* How to run the program
* Step-by-step bullets
```
git clone https://github.com/normandmickey/btcpay-chatgpt-flask.git
cd btcpay-chatgpt-flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp env.example .env
```

Update the following variables in your .env file
OPENAI_API_KEY="Your OpenAI API Key"
BTCPAY_API_KEY = "Your BTCPayServer API Key"
BTCPAY_HOST_URL = "Your BTCPayServer Host URL"
BTCPAY_STORE_ID = "Your BTCPayServer Store ID"

Update the btcpay.js file under static/js
Replace 

```
flask run
```

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details