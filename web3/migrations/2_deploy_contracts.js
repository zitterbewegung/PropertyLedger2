var EscrowLedger = artifacts.require("EscrowLedger");

module.exports = function(deployer){

    deployer.deploy(EscrowLedger);
    
};
