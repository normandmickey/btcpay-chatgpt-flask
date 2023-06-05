# btcpay-chatgpt-flask
This project is a demonstration of how to add a Bitcoin Lightning Paywall for the OPENAI ChatGPT API using BTCPayServer and Flask.  


## Getting Started

### Dependencies

* OPENAI API Key
* BTCPayServer Instance
* Ubuntu VPS or RaspberryPi (for development server).
* Python 3.10+

### Installing

```
git clone https://github.com/normandmickey/btcpay-chatgpt-flask.git
cd btcpay-chatgpt-flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Update the following variables in your .env file
```
cp env_example .env 
nano .env
```

* OPENAI_API_KEY="Your OpenAI API Key"
* BTCPAY_API_KEY = "Your BTCPayServer API Key"
* BTCPAY_HOST_URL = "Your BTCPayServer Host URL"
* BTCPAY_STORE_ID = "Your BTCPayServer Store ID"

> To generate an API key, you need to log in to your BTCPay instance, click "Account" in the lower left corner, click 
> "Manage Account", click the "API Keys" tab, and then generate your key.


Update the btcpay.js file under static/js
```
cp static/js/btcpay.js.example static/js/btcpay.js 
nano static/js/btcpay.js
```
Find the line "var origin = 'YourBTCPayServerURL';" and replace YourBTCPayServerURL with your own.  Include https:// and port if necessary. 

```
flask run
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
