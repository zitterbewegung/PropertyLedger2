// Copyright 2017 https://tokenmarket.net - MIT licensed
//
// Run with Node 7.x as:
//
// node --harmony-async-await  deploy.js
//

let fs = require("fs");
let Web3 = require('web3'); // https://www.npmjs.com/package/web3

// Create a web3 connection to a running geth node over JSON-RPC running at
// http://localhost:8545
// For geth VPS server + SSH tunneling see
// https://gist.github.com/miohtama/ce612b35415e74268ff243af645048f4
const HDWalletProvider = require('truffle-hdwallet-provider');

const walletMnemonic = 'sausage food butter ask staff such primary plate light quick drill proof'; // Your mnemonic
const walletAPIUrl = 'rD8Lg0NVjOOkYDcvVi0r'; // Your Infura URL

const provider = new HDWalletProvider(
    walletMnemonic,
    walletAPIUrl
);

const web3 = new Web3(provider);



//let web3 = new Web3(new Web3.providers.HttpProvider("http://168.62.166.36:8545"));

//web3.setProvider(new web3.providers.HttpProvider('http://localhost:8545'));



//console.log("Deploying the contract");
//let contract = SampleContract.new({from: web3.eth.coinbase, gas: 1000000, data: code});

// Transaction has entered to geth memory pool
//console.log("Your contract is being deployed in transaction at http://testnet.etherscan.io/tx/" + contract.transactionHash);

// http://stackoverflow.com/questions/951021/what-is-the-javascript-version-of-sleep

// We need to wait until any miner has included the transaction
// in a block to get the address of the contract
async function waitBlock() {
  while (true) {
    let receipt = web3.eth.getTransactionReceipt(contract.transactionHash);
    if (receipt && receipt.contractAddress) {
      console.log("Your contract has been deployed at http://testnet.etherscan.io/address/" + receipt.contractAddress);
      console.log("Note that it might take 30 - 90 sceonds for the block to propagate befor it's visible in etherscan.io");
      break;
    }
    console.log("Waiting a mined block to include your contract... currently in block " + web3.eth.blockNumber);
    await sleep(4000);
  }
}
	     

	     var filter = web3.eth.filter('latest');
	     filter.watch(function(error, result) {
		 var block = Web3.eth.getBlock(result, true);
		 console.log('block #' + block.number);
		 console.dir(block.transactions);
	     });


//waitBlock();
//Load HTTP module
const http = require("http");
const hostname = 'propdemo.eastus.cloudapp.azure.com';
const port = 3001;

//Create HTTP server and listen on port 3000 for requests
const server = http.createServer((req, res) => {

  //Set the response HTTP header with HTTP status and Content type
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
      	     //var web3 = new Web3(new Web3.providers.HttpProvider("http://127.0.0.1:8545"));
	     var escrowledgerContract = web3.eth.contract([{"constant":true,"inputs":[],"name":"countLedgerEntrys","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"LedgerEntryAccts","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_address","type":"address"}],"name":"getLedgerEntry","outputs":[{"name":"","type":"uint256"},{"name":"","type":"string"},{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_address","type":"address"},{"name":"_money","type":"uint256"},{"name":"_ledgerUser","type":"string"},{"name":"_escrowName","type":"string"}],"name":"setLedgerEntry","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getLedgerEntrys","outputs":[{"name":"","type":"address[]"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]);
console.log("Here")
var escrowledger = escrowledgerContract.new(
		 {
		     from: web3.eth.accounts[0],
		     data: '0x60806040526102e0604051908101604052806102a781526020016101316102a7913960009080519060200190610036929190610049565b5034801561004357600080fd5b506100ee565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061008a57805160ff19168380011785556100b8565b828001600101855582156100b8579182015b828111156100b757825182559160200191906001019061009c565b5b5090506100c591906100c9565b5090565b6100eb91905b808211156100e75760008160009055506001016100cf565b5090565b90565b6035806100fc6000396000f3006080604052600080fd00a165627a7a723058205ad811dcf83221f2b7f8bba4c62cae59296fd18062f0bfbcdb4635bc99998ffe0029434f4f4b20434f554e545920494c4c494e4f4953205553412030322d31312d32303138203a3a2031343a32323a3038205458204e554d4245523a203230313830303030303030303120494e535452554d454e5420545950453a2057617272616e74792044656564204255594552204e414d453a204a6f7368756120582e204a6f686e736f6e2053454c4c4552204e414d453a204d697269616d20542e20616e64204d69636861656c20522e20536d69746820434f4d4d4f4e20414444524553533a203135353039204c4520434c414952452041564520416d6573205374726565742c204368696361676f20496c6c696e6f69732050494e206f662050524f50455254593a2032382d31362d363430312d34362d30303030302048415348204f46204c4547414c204445534352495054494f4e3a2031643334356a6c6536736572613435336c6b6a337878657334363433326420317374205052494f5220444f43554d454e54204e554d4245523a20323031333335353534303332205349474e45442042592042555945523a20596573205349474e45442042592053454c4c45523a20596573204e4f54415259205349474e41545552453a20313334336b7364383864733037303938307365383736733939204d554e49434950414c2054415820504149443a203130302e303020434f554e54592054415820504149443a203530302e30302053544154452054415820504149443a20313030302e30302048415348204f462053414c455320434f4e54524143543a2031646669333435336c38393873396467667373733938392048415348204f46204d4f525447414745202d204c49454e3a20316664663864356464646768686838726768383864362048415348204f46205448495320545820444154413a2031646b333334356b6a6c69333435336964663064',
		     gas: '4700000'
		 }, function (e, contract){
		     console.log(e, contract);
		     if (typeof contract.address !== 'undefined') {
			 var result = "Successfully deployed contract to Ethereum! address: <BR> " + contract.address + ' transactionHash: <BR>' + contract.transactionHash;
			 //bootbox.alert(result);
			 res.end(result);

			 console.log('Contract mined! address: ' + contract.address + ' transactionHash: ' + contract.transactionHash);
		 	
		     }
		 })
  
});

//listen for request on port 3000, and as a callback function have the port listened on logged
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
