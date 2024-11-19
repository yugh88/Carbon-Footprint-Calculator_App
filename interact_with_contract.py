# interact_with_contract.py
from web3 import Web3
from blockchain_config import CONTRACT_ADDRESS, CARBON_FOOTPRINT_ABI, GANACHE_URL

# Connect to Ethereum node (Ganache in this case)
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

# Check if the connection is successful
print(f"Connected to blockchain: {w3.is_connected()}")

# Interact with the contract
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=CARBON_FOOTPRINT_ABI)

# Optionally: Add other contract calls here
# For example, print the contract's address:
print(f"Contract Address: {contract.address}")
