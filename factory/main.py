#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import json
import sys

symbol = "COCOS"
chainID = "725fdc4a727a6aa84aea37376bb51e419febbf0f59830c05f3e82f607631e5fc"
endpoint = "127.0.0.1:8049"  #endpoint 

middleware_path="Python-Middleware"
#chains.py data
default_chains_data = """
default_prefix = "symbol"
known_chains = { 
    "symbol": {
        "chain_id": "chainID",
        "core_symbol": "symbol",
        "prefix": "symbol"
        },
    } 
"""


def clean():
    os.system("pkill witness_node; sleep 2")
    os.system("rm -rf witness_node_data_dir *.log witness_node cli_wallet wallet")

def node_init():
    clean()
    os.system("tar -zxf node_bin.tar.gz")
    os.system("nohup ./witness_node --genesis-json genesis.json >> witness_node.log 2>&1 &")
    os.system("sleep 5")
    os.system("pkill witness_node; cp config.ini ./witness_node_data_dir/config.ini")
    os.system("nohup ./witness_node --genesis-json genesis.json >> witness_node.log 2>&1 &")
    os.system("sleep 3")
    os.system("grep -n 'Chain ID is' witness_node.log >> chainID.log")

def node_run():
    os.system("pkill witness_node; sleep 2")
    os.system("nohup ./witness_node --genesis-json genesis.json >> witness_node.log 2>&1 &")

def chainID_init():
    global chainID
    with open("chainID.log", "r") as f:
        for line in f:
            tokens = line.split("is")
            chainID = tokens[1].strip()
            print("[chainID_init] chain id: " + chainID)
            break

def chains_py_init():
    chainID_init()
    chains_data = default_chains_data.replace("symbol", symbol)
    chains_data = chains_data.replace("chainID", chainID)
    chains_file = "../" + middleware_path + "/PythonMiddlewarebase/chains.py"
    print("open file: " + chains_file + ", write data: " + chains_data)
    with open(chains_file, "w") as file:
        file.write(chains_data)

def cli_wallet_start():
    chainID_init()
    cmd = "cd wallet; ./cli_wallet --chain-id " + chainID + " -s ws://" + endpoint
    print(">>> " + cmd)
    os.system(cmd)

def cli_wallet_init():
    os.system("rm -rf wallet; mkdir wallet; cp cli_wallet wallet/")
    cli_wallet_start()

def middleware_install():
    chains_py_init()
    cmd = "cd ../" + middleware_path + "; python3 setup.py install --user"
    print(">>> " + cmd)
    os.system(cmd)

def import_balance():
    text = """
    *******************************************************************************************
    * import balance cli_wallet steps:
    *  1. set_password 123456
    *  2. unlock 123456
    *  3. import_key  nicotest  5KgiWEMJPYbLpMhX6jvS9yBehhr4mWZhxX7hfxZQEo3rs8iakUQ
    *  4. import_balance  nicotest  ["5KAUeN3Yv51FzpLGGf4S1ByKpMqVFNzXTJK7euqc3NnaaLz1GJm"] true
    *  5. list_account_balances nicotest
    *  6. upgrade_account nicotest true
    *  7. exit cli_wallet: ctrl+c 
    *******************************************************************************************
    """
    print(text)
    cli_wallet_init()

# run once
# create new chain, import balance, install python-middleware
def init():
    node_init()
    import_balance()
    middleware_install()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == "init":
            init()
            node_run()
        elif sys.argv[1] == "cli":
            cli_wallet_start()
        elif sys.argv[1] == "clean":
            clean()
        else:
            node_run()
    else:
        node_run()
