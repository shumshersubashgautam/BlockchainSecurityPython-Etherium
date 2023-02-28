from web3 import Web3

INFURA = 'https://mainnet.infura.io/v3/111df5433d554dfa90d9895980d81f22'

#Connect to Blockchain

web3 = Web3(Web3.HTTPProvider(INFURA))
print(f'Connected:{web3.isConnected()}')

target_address = web3.toChecksumAddress("0x514910771AF9Ca656af840dff83E8264EcF986CA")
print(web3.fromWei(web3.eth.getBalance(target_address),'ether'))
print(web3.eth.get_code(target_address))