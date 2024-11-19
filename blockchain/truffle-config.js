module.exports = {
  networks: {
    // Development network configuration
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*",
      gas: 10000000, // Increase gas limit
    },
    
    // Uncomment and configure additional networks as needed
    // advanced: {
    //   port: 8777,
    //   network_id: 1342,
    //   gas: 8500000,
    //   gasPrice: 20000000000,
    //   from: "<address>",
    //   websocket: true,
    // },
    // goerli: {
    //   provider: () => new HDWalletProvider(MNEMONIC, `https://goerli.infura.io/v3/${PROJECT_ID}`),
    //   network_id: 5, 
    //   confirmations: 2,
    //   timeoutBlocks: 200,
    //   skipDryRun: true
    // }
  },

  // Mocha testing framework configuration
  mocha: {
    // timeout: 100000
  },

  // Solidity compiler configuration
  compilers: {
    solc: {
      version: "0.8.0", // Use Solidity version 0.8.21
      // Uncomment for optimization or specific EVM version
      // optimizer: {
      //   enabled: true,
      //   runs: 200
      // },
      // evmVersion: "byzantium"
    },
  },

  // Truffle DB settings (disabled by default)
  db: {
    enabled: false,
  },
};


