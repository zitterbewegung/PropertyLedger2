import json
import web3

from web3 import Web3
from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code

contract_source_code = '''
<<<<<<< HEAD

pragma solidity ^0.4.21;

contract Greeter {
    string public greeting;

    function Greeter() public {
        greeting = 'Hello';
=======
pragma solidity ^0.4.18;

contract EscrowLedger {
    
    struct LedgerEntry {
        uint money;
        string ledgerUser;
        string escrowName;
>>>>>>> 2bf226da0e2eed244cbc1d4e4ffb7916b7a4b721
    }
    
    mapping (address => LedgerEntry) LedgerEntrys;
    address[] public LedgerEntryAccts;
    
    function setLedgerEntry(address _address, uint _money, string _ledgerUser, string _escrowName) public {
        var LedgerEntry = LedgerEntrys[_address];
        
        LedgerEntry.money = _money;
        LedgerEntry.ledgerUser = _ledgerUser;
        LedgerEntry.escrowName = _escrowName;
        
        LedgerEntryAccts.push(_address) -1;
    }
    
    function getLedgerEntrys() view public returns(address[]) {
        return LedgerEntryAccts;
    }
    
    function getLedgerEntry(address _address) view public returns (uint, string, string) {
        return (LedgerEntrys[_address].money, LedgerEntrys[_address].ledgerUser, LedgerEntrys[_address].escrowName);
    }
    
    function countLedgerEntrys() view public returns (uint) {
        return LedgerEntryAccts.length;
    }
    
}
'''

compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Greeter']

# web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# Instantiate and deploy contract
Greeter = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
pragma
# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Create the contract instance with the newly-deployed address
greeter = w3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=contract_interface['abi'],
)

# Display the default greeting from the contract
print('Default contract greeting: {}'.format(
    greeter.functions.greet().call()
))

print('Setting the greeting to Nihao...')
tx_hash = greeter.functions.setGreeting('Nihao').transact()

# Wait for transaction to be mined...
w3.eth.waitForTransactionReceipt(tx_hash)

# Display the new greeting value
print('Updated contract greeting: {}'.format(
    greeter.functions.greet().call()
))

# When issuing a lot of reads, try this more concise reader:
reader = ConciseContract(greeter)
assert reader.greet() == "Nihao"
