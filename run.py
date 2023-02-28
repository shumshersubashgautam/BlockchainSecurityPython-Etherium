#python = 3.6.8
#web3:3.2.0
#pip:21.3.1
from web3 import Web3

INFURA = 'https://mainnet.infura.io/v3/111df5433d554dfa90d9895980d81f22'

web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected:{web3.isConnected()}')
