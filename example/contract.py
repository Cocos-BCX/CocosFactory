#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PythonMiddleware.graphene import Graphene
from PythonMiddleware.instance import set_shared_graphene_instance
from pprint import pprint
from PythonMiddleware.account import Account

nodeAddress = "ws://127.0.0.1:8049" 
gph = Graphene(node=nodeAddress, blocking=True) 
set_shared_graphene_instance(gph) 

#创建钱包
#可以通过gph.wallet 直接使用钱包instance，操作钱包的接口。
if gph.wallet.created() is False: 
    gph.newWallet("123456")

#钱包解锁
if gph.wallet.locked() is True:
    gph.wallet.unlock("123456")

#init0 ["COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT", "5JHdMwsWkEXsMozFrQAQKnKwo44CaV77H45S9PsH7QVbFQngJfw"]
pub="COCOS5vzuh6YRRmCjUMeeHLsjnVCdJwqm9WZoUBDDNVp7HTwFM1ZYQT"
pprint(gph.wallet.getPrivateKeyForPublicKey(pub))

#pprint(gph.wallet.removeAccount(None))
pprint(gph.wallet.getAccounts())

#合约创建
contract_name = "contract.debug.hello"
data = "function hello() \
    chainhelper:log('Hello World!') \
    chainhelper:log(date('%Y-%m-%dT%H:%M:%S', chainhelper:time())) \
end "
#pprint(gph.create_contract(contract_name, data=data, con_authority=pub, account="init0"))

#合约调用: contract.debug.hello
value_list=[]
#pprint(gph.call_contract_function(contract_name, "hello", value_list=value_list, account="test14"))


