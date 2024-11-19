const CarbonFootprintTracker = artifacts.require("CarbonFootprintTracker");

module.exports = function (deployer) {
  deployer.deploy(CarbonFootprintTracker);
};
