from web3 import Web3
from solcx import compile_standard, install_solc

install_solc("0.8.0")
import json

# Connect to Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Account information
account_1 = "0x815155C8ada5fbFaEF51fB900cA4932B2EC37558"
private_key = "0xcb020f2b814a13a2637e6ff501165f5183054498b25809c6cfa6e74dfc694144"


contract_address = None  # Store contract address after deployment

# Compile Solidity contract
def compile_contract():
    with open("./contracts/DataStorage.sol", "r") as file:
        data_storage_file = file.read()

    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"DataStorage.sol": {"content": data_storage_file}},
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version="0.8.0",
    )
    return compiled_sol

# Deploy the contract (once) and store the address
def deploy_contract(compiled_sol):
    global contract_address
    bytecode = compiled_sol["contracts"]["DataStorage.sol"]["DataStorage"]["evm"]["bytecode"]["object"]
    abi = compiled_sol["contracts"]["DataStorage.sol"]["DataStorage"]["abi"]

    # Get nonce
    nonce = web3.eth.getTransactionCount(account_1)

    # Build transaction
    transaction = {
        "from": account_1,
        "gas": 2000000,
        "gasPrice": web3.toWei("50", "gwei"),
        "nonce": nonce,
        "data": bytecode,
    }

    # Sign transaction
    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key)

    # Send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

    # Get transaction receipt
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    contract_address = tx_receipt.contractAddress  # Store deployed contract address

    return web3.eth.contract(address=contract_address, abi=abi)

# Load the contract at the existing address
def load_contract(compiled_sol):
    abi = compiled_sol["contracts"]["DataStorage.sol"]["DataStorage"]["abi"]
    return web3.eth.contract(address=contract_address, abi=abi)

# Function to add data to the contract
def add_data(identifier, data_list):
    compiled_sol = compile_contract()
    contract = load_contract(compiled_sol)

    # Get nonce
    nonce = web3.eth.getTransactionCount(account_1)

    # Build transaction to add data
    transaction = contract.functions.addData(identifier, data_list).buildTransaction({
        'from': account_1,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    })

    # Sign transaction
    signed_transaction = web3.eth.account.sign_transaction(transaction, private_key)

    # Send transaction
    tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

    # Wait for transaction receipt
    web3.eth.wait_for_transaction_receipt(tx_hash)

    print(f"Data added for {identifier}: {data_list}")

# Function to add more data after deployment
def add_more_data():
    compiled_sol = compile_contract()
    contract = load_contract(compiled_sol)
    add_data("ali@gmail.com", ["item1", "item2", "item3"])
    add_data("swamy@gmail.com", ["data1", "data2", "data3"])

# Function to retrieve all stored data
def dataget():
    compiled_sol = compile_contract()
    contract = load_contract(compiled_sol)

    # Fetch all data entries from the contract
    data_entries = contract.functions.getAllData().call()

    res=[]

    # Display the data
    for entry in data_entries:
        identifier = entry[0]
        data_list = entry[1]
        print(f"Identifier: {identifier}, Data List: {data_list}")
        res.append(data_list)

    return res


# Store contract address after first deployment
def store_contract_address(address):
    with open('contract_address.txt', 'w') as f:
        f.write(address)

# Load contract address for future interaction
def load_contract_address():
    global contract_address
    try:
        with open('contract_address.txt', 'r') as f:
            contract_address = f.read().strip()
            print(contract_address, 'contract_address')
    except FileNotFoundError:
        print("Contract address file not found. Deploying a new contract.")
        compiled_sol = compile_contract()
        contract = deploy_contract(compiled_sol)
        store_contract_address(contract_address)

if __name__ == "__main__":
    # Load or deploy the contract
    load_contract_address()

    # Add some data entries
    add_data("sajid24x7@gmail.com", ["item1", "item2", "item3"])
    add_data("example@gmail.com", ["data1", "data2", "data3"])

    # Retrieve all data
    res=dataget()
    print(res)
