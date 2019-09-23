#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PythonMiddleware.graphene import Graphene
from PythonMiddleware.instance import set_shared_graphene_instance
from pprint import pprint
from PythonMiddleware.account import Account
from PythonMiddleware.storage import configStorage as config

nodeAddress = "ws://127.0.0.1:8049" 
gph = Graphene(node=nodeAddress, blocking=True) 
set_shared_graphene_instance(gph) 

#account info for test
defaultAccount="nicotest"
privateKey="5KgiWEMJPYbLpMhX6jvS9yBehhr4mWZhxX7hfxZQEo3rs8iakUQ"
pub="COCOS5X4bfMnAmeWhLoiHKUNrRu7D3LTXKBZQkZvWGj9YCTDBAYaSXU"

#创建钱包
if gph.wallet.created() is False: 
    gph.newWallet("123456")

#钱包解锁
if gph.wallet.locked() is True:
    gph.wallet.unlock("123456")

#add key
if gph.wallet.getAccountFromPublicKey(pub) is None:
    gph.wallet.addPrivateKey(privateKey) #账号私钥导入钱包
pprint(gph.wallet.getPrivateKeyForPublicKey(pub))

#config
config["default_prefix"] = gph.rpc.chain_params["prefix"] # 向钱包数据库中添加默认信息
config["default_account"] = defaultAccount # 向钱包数据库中添加默认信息

#account test
#pprint(gph.wallet.removeAccount(None))
pprint(gph.wallet.getAccounts())

# transfer
#print("-------- transfer ------------")
#pprint(gph.transfer("test1", 100, "COCOS", defaultAccount))

print("-------- create asset ----------")
options = {
    "max_supply":"2100000000000000",
    "market_fee_percent":0,
    "max_market_fee":0,
    "issuer_permissions":79,
    "flags":0,
    "core_exchange_rate":{
        "base":{
            "amount":100000000,
            "asset_id":"1.3.1"
        },
        "quote":{
            "amount":100000,
            "asset_id":"1.3.0"
        }
    },
    "description":'{"main":"YUAN 2100","short_name":"","market":""}',
    "extensions":[]
}
#base: amount asset
#quote: _amount _asset
#pprint(gph.asset_create(symbol="YUAN", precision=5, amount=1000, asset="1.3.1", _amount=1, _asset="1.3.0", common_options=options, bitasset_opts=None, account=defaultAccount))

print("-------- update asset ----------")
new_options = {
    "max_supply":"2100000000000000",
    "market_fee_percent":0,
    "max_market_fee":0,
    "issuer_permissions":79,
    "flags":0,
    "core_exchange_rate":{
        "base":{
            "amount":1000,
            "asset_id":"1.3.1"
        },
        "quote":{
            "amount":1,
            "asset_id":"1.3.0"
        }
    },
    "description":'{"main":"YUAN 2100","short_name":"YUAN","market":"test net"}',
    "extensions":[]
}
#
pprint(gph.asset_update(asset="YUAN", new_options=new_options, issuer=defaultAccount, account=defaultAccount))


'''
1. create ERC20 token

unlocked >>> get_object 1.3.5
get_object 1.3.5
[{
    "id": "1.3.5",
    "symbol": "YUAN",
    "precision": 5,
    "issuer": "1.2.15",
    "options": {
      "max_supply": "2100000000000000",
      "market_fee_percent": 0,
      "max_market_fee": 0,
      "issuer_permissions": 79,
      "flags": 0,
      "core_exchange_rate": {
        "base": {
          "amount": 100000000,
          "asset_id": "1.3.5"
        },
        "quote": {
          "amount": 100000,
          "asset_id": "1.3.0"
        }
      },
      "description": "{\"main\":\"YUAN 2100\",\"short_name\":\"\",\"market\":\"\"}",
      "extensions": []
    },
    "dynamic_asset_data_id": "2.3.5"
  }
]
unlocked >>> 

2. asset update


'''


