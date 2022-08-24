pragma solidity ^0.5.1;

import "./SafeMath.sol";
import "./AddressUtils.sol";


contract ERC721Receiver {
    
  bytes4 constant ERC721_RECEIVED = 0xf0b9e5ba;

  function onERC721Received(address _from, uint256 _tokenId, bytes memory _data) public returns(bytes4);
}


contract ERC721Interface {

    event Transfer(address indexed _from, address indexed _to, uint256 _tokenId);
    event Approval(address indexed _owner, address indexed _approved, uint256 _tokenId);
    event ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved);

    function balanceOf(address _owner) public view returns (uint256);
    function ownerOf(uint256 _tokenId) public view returns (address);
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes memory data) public;
    function safeTransferFrom(address _from, address _to, uint256 _tokenId) public;
    function transferFrom(address _from, address _to, uint256 _tokenId) public;
    function approve(address _approved, uint256 _tokenId) public;
    function setApprovalForAll(address _operator, bool _approved) public;
    function getApproved(uint256 _tokenId) public view returns (address);
    function isApprovedForAll(address _owner, address _operator) public view returns (bool);
}

contract ERC721 is ERC721Interface {
    
    using SafeMath for uint256;
    using AddressUtils for address;

    bytes4 constant ERC721_RECEIVED = 0xf0b9e5ba;

    mapping(uint256 => address) internal tokenOwner;
    mapping (address => uint256) internal ownedTokensCount;
    mapping (uint256 => address) internal tokenApprovals;


    // address "A" allows address "B" to operate all A's assets
    mapping (address => mapping (address => bool)) internal operatorApprovals;


    modifier canTransfer(uint256 _tokenId) {
            require(isApprovedOrOwner(msg.sender , _tokenId));
            _;
    }


    function balanceOf(address _owner) public view returns (uint256) {
        require(_owner != address(0));
        return ownedTokensCount[_owner];
    }

    function ownerOf(uint256 _tokenId) public view returns (address) {
        address owner = tokenOwner[_tokenId];
        require (owner != address(0));
        return owner;
        
    }

    function isApprovedOrOwner(address _spender, uint256 _tokenId) internal view returns (bool) {
        address owner = tokenOwner[_tokenId];
        bool result = ( owner == _spender || getApproved(_tokenId)==_spender || isApprovedForAll(owner,_spender));
        return result;
    }
    
    
    function transferFrom(address _from, address _to, uint256 _tokenId) public canTransfer(_tokenId) {
        require(isApprovedOrOwner(msg.sender , _tokenId));
        clearApproval(_from , _tokenId);
        removeTokenFrom(_from , _tokenId);
        addTokenTo(_to , _tokenId);
    }
    
    
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes memory data) public {
        // if target address is a contract, make sure it supports ERC721 interface
        if(! AddressUtils.isContract(_to)){
            transferFrom( _from, _to , _tokenId);
        }
        else{
            bytes4 result = onERC721Received ( _from , _tokenId , data);
            require( result == ERC721_RECEIVED );
            transferFrom(_from , _to ,_tokenId);    
        }
        
        
    }

    function safeTransferFrom(address _from, address _to, uint256 _tokenId) public {
            safeTransferFrom(_from , _to , _tokenId , "");
    }

    function clearApproval(address _owner, uint256 _tokenId) internal {
        require(ownerOf(_tokenId) == _owner);
        tokenApprovals[_tokenId] == address(0);
    }

    function removeTokenFrom(address _from, uint256 _tokenId) internal {
        require (ownerOf(_tokenId) == _from);
        ownedTokensCount[_from] = SafeMath.sub(ownedTokensCount[_from],1);
        tokenOwner[_tokenId] = address(0);
    }

    function addTokenTo(address _to, uint256 _tokenId) internal {
        require(ownerOf(_tokenId) == address(0));
        tokenOwner[_tokenId] = _to;
        ownedTokensCount[_to] = SafeMath.add(ownedTokensCount[_to] , 1);
        
    }

    function isApprovedForAll(address _owner, address _operator) public view returns (bool) {
        return operatorApprovals[_owner][_operator];
    }

    function getApproved(uint256 _tokenId) public view returns (address) {
        return tokenApprovals[_tokenId];
    }
    
    function approve(address _approved, uint256 _tokenId) public {
        address owner = ownerOf(_tokenId);
        require(_approved != owner && ( msg.sender == owner || isApprovedForAll(owner,msg.sender)));
        tokenApprovals[_tokenId] = _approved;
        emit Approval( owner , _approved  , _tokenId);
    }

        function setApprovalForAll(address _operator, bool _approved) public {
        require( _operator != msg.sender);
        operatorApprovals [msg.sender][_operator] = _approved;
        emit ApprovalForAll(msg.sender , _operator , _approved);
        
    }

    
    function onERC721Received(address, uint256,  bytes memory) public returns (bytes4) {
        return ERC721_RECEIVED;
    }
}

