pragma solidity ^0.4.18;

contract EscrowLedger {
    //https://coursetro.com/posts/code/102/Solidity-Mappings-&-Structs-Tutorial
    struct LedgerEntry {
        uint money;
        string ledgerUser;
        string escrowName;
    }
   constructor() public {
       setLedgerEntry(this,12400,"LENDER","USD");
       setLedgerEntry(this,0,"BUYER","DEED");
       setLedgerEntry(this,0,"SELLER","DEED");
       setLedgerEntry(this,0,"LEIN-BANK","RELEASE");
       setLedgerEntry(this,0,"CHICAGO","TAXBILL");
       setLedgerEntry(this,0,"BUYER_REALITOR","COMMISSION");
       setLedgerEntry(this,0,"SELLER_REAILTOR","COMMISION_INVOICE");
       setLedgerEntry(this,0,"BUYER","SELLER_FEES_AND_TAXES");
       
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
