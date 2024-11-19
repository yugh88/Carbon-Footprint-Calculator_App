// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CarbonFootprintTracker {
    struct FootprintRecord {
        uint256 timestamp;
        uint256 carbonFootprint;
        uint256 treeCredits;
        bool isOffset;
    }
    
    mapping(address => FootprintRecord[]) public userFootprints;
    mapping(address => uint256) public totalTreeCredits;
    
    event FootprintRecorded(address indexed user, uint256 carbonFootprint, uint256 treeCredits);
    event CreditsOffset(address indexed user, uint256 treeCredits);
    
function recordFootprint(uint256 _carbonFootprint, uint256 _treeCredits) public {
    require(_carbonFootprint > 0, "Carbon footprint must be positive");
    require(_treeCredits >= 0, "Tree credits cannot be negative");

    FootprintRecord memory newRecord = FootprintRecord({
        timestamp: block.timestamp,
        carbonFootprint: _carbonFootprint,
        treeCredits: _treeCredits,
        isOffset: false
    });

    userFootprints[msg.sender].push(newRecord);
    totalTreeCredits[msg.sender] += _treeCredits;

    emit FootprintRecorded(msg.sender, _carbonFootprint, _treeCredits);
}

    
    function offsetCredits(uint256 _amount) public {
        require(totalTreeCredits[msg.sender] >= _amount, "Insufficient credits");
        totalTreeCredits[msg.sender] -= _amount;
        
        // Mark the oldest non-offset records as offset
        uint256 remainingAmount = _amount;
        for (uint256 i = 0; i < userFootprints[msg.sender].length && remainingAmount > 0; i++) {
            if (!userFootprints[msg.sender][i].isOffset) {
                userFootprints[msg.sender][i].isOffset = true;
                remainingAmount--;
            }
        }
        
        emit CreditsOffset(msg.sender, _amount);
    }
    
    function getUserFootprints(address _user) public view returns (FootprintRecord[] memory) {
        return userFootprints[_user];
    }
    
    function getUserTreeCredits(address _user) public view returns (uint256) {
        return totalTreeCredits[_user];
    }
}