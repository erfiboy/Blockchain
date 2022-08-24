pragma solidity ^ 0.5.1;

import "./Auction.sol";


contract CustomAuction is Auction {

    enum Phase { Pending, Commitment, Opening, Finished }
    
    Phase public phase;

    uint startPhaseBlock;
    uint commitment_len;
    uint opening_len;
    // winner address and bid
    address payable lowestBidder;
    uint lowestBid;
    
    uint ReserveFund;


    bool firstOpen = true;

    struct Bid {
        
        bytes32 FileAddress;
        uint value;
        bytes32 hash;
        bytes32 nonce;
    }

    mapping(address => Bid) bids;
    
    // address of accounts admin choose in Opening phase
    mapping(address => bool) chooses;

    
    
    event openingStarted();
        

    constructor(
        

        address payable _admin,
        uint _commitment_len,
        uint _opening_len
        
    ) public payable {

        // Control if inputs are valid or not and then initialize local variables
        require(_commitment_len > 0);
        commitment_len = _commitment_len;
        require(_opening_len > 0);
        opening_len = _opening_len;
        require(_admin != address(0));
        description.admin = _admin;
        phase = Phase.Pending;
        description.deployBlock = block.number; 
        ReserveFund = msg.value;
    }



    /// @dev This modifier allow to invoke the function olny during the Commitment phase.
    modifier duringCommitment {
        require(phase == Phase.Commitment);
        require( block.number <= startPhaseBlock + commitment_len);
        _;
    }

    /// @dev This modifier allow to invoke the function olny during the Opening phase.
    modifier duringOpening {
        require(phase == Phase.Opening);
        require(block.number <= startPhaseBlock + opening_len );
        _;
    }
    
    
    function getReserveFund() public view returns (uint256) {
        return ReserveFund;
    }
    
    function getFile( address add ) public view returns ( bytes32 fileAdd) {
        require(add != address(0));
        return bids[add].FileAddress;
        
    }
    
    /// @notice This function will activate the auction.
    function activateAuction() public onlyAdmin {
        require(phase == Phase.Pending);
        phase = Phase.Commitment;
        startPhaseBlock = block.number;
        description.startBlock = startPhaseBlock;
        emit auctionStarted();

    }

    ///@notice This function allow people to make bid.
    ///@notice Note that a bid will be taken into account if the value sent is >= the minimum deposit.
    ///@dev This function can be invoked only during the commitment phase.
        ///@param _bidHash this is the hash of the tuple <value,nonce>. See `GenerateBid` contract for more info.
    function bid(bytes32 _bidHash, bytes32 _FileAddress) public duringCommitment payable {
        require(_bidHash != 0 && _FileAddress != 0);
        require(bids[msg.sender].hash == 0 && bids[msg.sender].FileAddress == 0);
        bids[msg.sender].hash = _bidHash;
        bids[msg.sender].FileAddress = _FileAddress;
    }

 
    ///@notice This function activate the Opening phase
    function startOpening(address add1, address add2, address add3) public onlyAdmin {
        require(phase == Phase.Commitment);
        require( block.number >= startPhaseBlock + commitment_len);
        phase = Phase.Opening;
        startPhaseBlock = block.number;
        chooses[add1] = true;
        chooses[add2] = true;
        chooses[add3] = true;
        emit openingStarted();
    }

    ///@notice This function allow people to open their bid.
    function open( uint value, bytes32 _nonce) public duringOpening {
        
        // Control the correctness of the bid
        require(chooses[msg.sender]);
        require(bids[msg.sender].value <= ReserveFund);
        require(bids[msg.sender].hash ==  sha256(abi.encodePacked(value, _nonce)));
        // Update the bid status
        bids[msg.sender].value = value;
        bids[msg.sender].nonce = _nonce;
        if (firstOpen)
        {
            lowestBid = bids[msg.sender].value;
            lowestBidder = msg.sender;
        }
        else
        {
            if (bids[msg.sender].value < lowestBid)
            {
                lowestBid = bids[msg.sender].value;
                lowestBidder = msg.sender;             
            }
        }
    }


    ///@notice This function finalize and close the contract.
    function finalize() public onlyAdmin {
        require(phase == Phase.Opening);
        require(block.number >= startPhaseBlock + opening_len);
        if (firstOpen)
        {
            description.admin.transfer(ReserveFund);
            description.winnerAddress = address(0);
            description.winnerBid = 0 ;
            
        }
        else
        {
            lowestBidder.transfer(lowestBid);
            description.admin.transfer(ReserveFund - lowestBid);
            description.winnerAddress = lowestBidder;
            description.winnerBid = lowestBid ;
        }

        emit auctionFinished(lowestBidder , lowestBid);

    }
}
