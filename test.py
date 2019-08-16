#ddPrivateKey(!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PythonMiddleware.graphene import Graphene
from PythonMiddleware.instance import set_shared_graphene_instance
from PythonMiddleware.storage import configStorage as config
from pprint import pprint

#nodeAddress = "ws://47.93.62.96:8049"
#gph = Graphene(node=nodeAddress, blocking=True)
#set_shared_graphene_instance(gph)

#if gph.wallet.created() is False:                                                                                                                                                                      
#   gph.newWallet("123456")
#print(gph.wallet.unlock("123456"))

#ret = gph.start()
#print(ret)

local_nodeAddress = "ws://127.0.0.1:8049"
local_gph = Graphene(node=local_nodeAddress, blocking=True)
set_shared_graphene_instance(local_gph)

if local_gph.wallet.created() is False: 
   local_gph.newWallet("123456")
   print("create new wallet")
print(local_gph.wallet.unlock("123456")) 

#config["default_prefix"] = local_gph.rpc.chain_params["prefix"] 
#privateKey="5HqVs2QEk7Ndt6vmGZES26ecEZpcFmc9NQVzHL9T8M5muhJjjNa"
#local_gph.wallet.addPrivateKey(privateKey) 
#config["default_account"] = "nicotest"

#pprint(local_gph.create_account(account_name="test12", password="123456", proxy_account="nicotest"))

print(local_gph.wallet.getAccounts())
print("\n\n")
pprint(local_gph.create_account(account_name="test12", password="123456", proxy_account="init0"))


data = """
        function hello()
            chainhelper:log('hello world')
        end"""
print(local_gph.create_contract("contract.hello",data,con_authority="COCOS7Pf4ashtamfp9APegvsTY1quatrULosVpEeGEcKWr7fng1ERgk", account="test2"));
