from flask import Flask, request
import requests, json, argparse, sys

app = Flask(__name__)

@app.route('/get_ip_owner', methods=['GET'])
def get_owner():

    ip = request.args.get('ip')
    print(ip)

    head = {'Accept': r'application/json'}
    url = f'http://whois.arin.net/rest/ip/{ip}'
    r = requests.get(url, headers=head, verify=False)
    #if r.status_code != 200:
        #raise Exception(f'Error code in response: {r.status_code}')
    #else:
    print(r.status_code)
    return r.json().get("net").get("orgRef").get("@name")

if __name__ == "__main__":
    app.run()