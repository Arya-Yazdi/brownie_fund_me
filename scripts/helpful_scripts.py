from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    # Get first brownie/ganache-cli generated account address if connected to a local network
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        # Get real account private key stored in .env file
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is: {network.show_active()}")
    print("Deploying Mocks...")
    # If MockV3Aggregator function is not already deployed...
    if len(MockV3Aggregator) <= 0:
        # Deploy our MockV3Aggregator contract.
        # MockV3Aggregator is a contract that stores the code for price feed.
        # This is done because we have to use locally generated price feed as
        # we won't be connected to any networks.
        MockV3Aggregator.deploy(
            DECIMALS,
            STARTING_PRICE,
            {"from": get_account()})
            
        print("Mock is deployed")
