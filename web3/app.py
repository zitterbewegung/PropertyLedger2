from flask import Flask,request
# solc is needed to compile our Solidity code
from solc import compile_source

# web3 is needed to interact with eth contracts
from web3 import Web3, HTTPProvider

# we'll use ConciseContract to interact with our specific instance of the contract
from web3.contract import ConciseContract

app = Flask(__name__)

@app.route('/')
def make_contract():
    
    # open a connection to the local ethereum node
    #http_provider = HTTPProvider('http://localhost:8545')
    #eth_provider = Web3(http_provider).eth
    #https://ethereum.stackexchange.com/questions/44614/how-to-connect-to-infura-and-deploy-contract-use-web3-py
    # we'll use one of our default accounts to deploy from. every write to the chain requires a
    # payment of ethereum called "gas". if we were running an actual test ethereum node locally,
    # then we'd have to go on the test net and get some free ethereum to play with. that is beyond
    # the scope of this tutorial so we're using a mini local node that has unlimited ethereum and
    # the only chain we're using is our own local one
    #default_account = eth_provider.accounts[0]
    # every time we write to the chain it's considered a "transaction". every time a transaction
    # is made we need to send with it at a minimum the info of the account that is paying for the gas
    #transaction_details = {
    #    'from': default_account,
    #}

    # load our Solidity code into an object
    #with open('/home/r2q2/Desktop/coinsulting/PropertyLedger2/sawtooth-tuna/web3_server/EscrowLedger.sol') as file:
    #    source_code = file.readlines()

    # compile the contract
    #compiled_code = compile_source(''.join(source_code))

    # store contract_name so we keep our code DRY
    contract_name = 'EscrowLedger'

    # lets make the code a bit more readable by storing these values in variables
    contract_bytecode = '0x60806040526102e0604051908101604052806102a781526020016101316102a7913960009080519060200190610036929190610049565b5034801561004357600080fd5b506100ee565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061008a57805160ff19168380011785556100b8565b828001600101855582156100b8579182015b828111156100b757825182559160200191906001019061009c565b5b5090506100c591906100c9565b5090565b6100eb91905b808211156100e75760008160009055506001016100cf565b5090565b90565b6035806100fc6000396000f3006080604052600080fd00a165627a7a723058205ad811dcf83221f2b7f8bba4c62cae59296fd18062f0bfbcdb4635bc99998ffe0029434f4f4b20434f554e545920494c4c494e4f4953205553412030322d31312d32303138203a3a2031343a32323a3038205458204e554d4245523a203230313830303030303030303120494e535452554d454e5420545950453a2057617272616e74792044656564204255594552204e414d453a204a6f7368756120582e204a6f686e736f6e2053454c4c4552204e414d453a204d697269616d20542e20616e64204d69636861656c20522e20536d69746820434f4d4d4f4e20414444524553533a203135353039204c4520434c414952452041564520416d6573205374726565742c204368696361676f20496c6c696e6f69732050494e206f662050524f50455254593a2032382d31362d363430312d34362d30303030302048415348204f46204c4547414c204445534352495054494f4e3a2031643334356a6c6536736572613435336c6b6a337878657334363433326420317374205052494f5220444f43554d454e54204e554d4245523a20323031333335353534303332205349474e45442042592042555945523a20596573205349474e45442042592053454c4c45523a20596573204e4f54415259205349474e41545552453a20313334336b7364383864733037303938307365383736733939204d554e49434950414c2054415820504149443a203130302e303020434f554e54592054415820504149443a203530302e30302053544154452054415820504149443a20313030302e30302048415348204f462053414c455320434f4e54524143543a2031646669333435336c38393873396467667373733938392048415348204f46204d4f525447414745202d204c49454e3a20316664663864356464646768686838726768383864362048415348204f46205448495320545820444154413a2031646b333334356b6a6c69333435336964663064'
    contract_abi = [{"constant":True,"inputs":[],"name":"countLedgerEntrys","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint256"}],"name":"LedgerEntryAccts","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_address","type":"address"}],"name":"getLedgerEntry","outputs":[{"name":"","type":"uint256"},{"name":"","type":"string"},{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_address","type":"address"},{"name":"_money","type":"uint256"},{"name":"_ledgerUser","type":"string"},{"name":"_escrowName","type":"string"}],"name":"setLedgerEntry","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"getLedgerEntrys","outputs":[{"name":"","type":"address[]"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"}]
    # the contract abi is important. it's a json representation of our smart contract. this
    # allows other APIs like JavaScript to understand how to interact with our contract without
    # reverse engineering our compiled code

    
    w3 = Web3(HTTPProvider("https://rinkeby.infura.io/AJzACQv9DEFVUKsFYFV2"))

    contract_ = w3.eth.contract(
        abi=contract_abi,
        bytecode=contract_bytecode)

    #acct = w3.eth.account.privateKeyToAccount(privateKey)
    acct = w3.eth.account.privateKeyToAccount("22d07f87694cb5b40641cd2257040ce4e11e278ad92cdb98d0d0a07fdf9feae9")
    
    construct_txn = contract_.constructor().buildTransaction({
    'from': acct.address,
    'nonce': w3.eth.getTransactionCount(acct.address),
    'gas': 1728712,
    'gasPrice': w3.toWei('21', 'gwei')})

    signed = acct.signTransaction(construct_txn)
    try:
        result = w3.eth.sendRawTransaction(signed.rawTransaction)
    except:
        return "Please wait for the previous transaction to finish"
    result = w3.eth.sendRawTransaction(signed.rawTransaction)
    
    #tx_receipt = w3.eth.getTransactionReceipt(result)
    # # contract that we probably will not change later in the deployment script.
    # contract_factory = eth_provider.contract(
    #     abi=contract_abi,
    #     bytecode=contract_bytecode,
    # )

    #  # here we deploy the smart contract
    # # two things are passed into the deploy function:
    # #   1. info about how we want to deploy to the chain
    # #   2. the arguments to pass the smart contract constructor
    # # the deploy() function returns a transaction hash. this is like the id of the
    # # transaction that initially put the contract on the chain
    # transaction_hash = contract_factory.deploy(
    #     # the bare minimum info we give about the deployment is which ethereum account
    #     # is paying the gas to put the contract on the chain
    #     transaction=transaction_details,
    #     # here was pass in a list of smart contract constructor arguments
    #     # our contract constructor takes only one argument, a list of candidate names
    #     args=[],
    # )

    # # if we want our frontend to use our deployed contract as it's backend, the frontend
    # # needs to know the address where the contract is located. we use the id of the transaction
    # # to get the full transaction details, then we get the contract address from there
    # transaction_receipt = eth_provider.getTransactionReceipt(transaction_hash)
    # contract_address = transaction_receipt['contractAddress']

    # contract_instance = eth_provider.contract(
    #     abi=contract_abi,
    #     address=contract_address,
    #     # when a contract instance is converted to python, way call the native solidity
    #     # functions like: contract_instance.call().someFunctionHere()
    #     # the .call() notation becomes repetitive so we can pass in ConciseContract as our
    #     # parent class, allowing us to make calls like: contract_instance.someFunctionHere()
    #     ContractFactoryClass=ConciseContract,
    # )
    # #pi_in_decimal = contract_instance.percent(22,7,10)
    return "Contract deployed at address " + result.hex()
if __name__ == '__main__':
    # set debug=True for easy development and experimentation
    # set use_reloader=False. when this is set to True it initializes the flask app twice. usually
    # this isn't a problem, but since we deploy our contract during initialization it ends up getting
    # deployed twice. when use_reloader is set to False it deploys only once but reloading is disabled
    app.run(debug=True, host='0.0.0.0', port=4444, use_reloader=False)
