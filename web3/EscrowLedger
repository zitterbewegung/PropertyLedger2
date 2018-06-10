pragma solidity ^0.4.18;

contract EscrowLedger {
    
    struct LedgerEntry {
        uint money;
        string ledgerUser;
        string escrowName;
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
