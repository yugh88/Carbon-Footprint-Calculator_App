CONTRACT_ADDRESS = "0x32F6b9Be09d07E79C133b89D6B79441eb4B7F42D"  # Deployed contract address
GANACHE_URL = "http://127.0.0.1:7545"  # URL for local Ganache instance

# ABI generated after compiling the contract
CARBON_FOOTPRINT_ABI = [
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "user",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "carbonFootprint",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "treeCredits",
          "type": "uint256"
        }
      ],
      "name": "FootprintRecorded",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "user",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "treeCredits",
          "type": "uint256"
        }
      ],
      "name": "CreditsOffset",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_amount",
          "type": "uint256"
        }
      ],
      "name": "offsetCredits",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "_carbonFootprint",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_treeCredits",
          "type": "uint256"
        }
      ],
      "name": "recordFootprint",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_user",
          "type": "address"
        }
      ],
      "name": "getUserFootprints",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "timestamp",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "carbonFootprint",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "treeCredits",
              "type": "uint256"
            },
            {
              "internalType": "bool",
              "name": "isOffset",
              "type": "bool"
            }
          ],
          "internalType": "struct CarbonFootprintTracker.FootprintRecord[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_user",
          "type": "address"
        }
      ],
      "name": "getUserTreeCredits",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
]
