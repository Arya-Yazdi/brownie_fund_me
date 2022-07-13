from sre_constants import IN
from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    # Get account
    account = get_account()

    # Get active network (network which contract is being deployed on)
    active_network = network.show_active()

    # If not on a development network
    if active_network not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # Get address of eth / usd price feed from .yaml file.
        price_feed_address = config["networks"][active_network]["eth_usd_price_feed"]
    else:
        # Deploy mock contracts
        deploy_mocks()
        # Get address of eth / usd price feed from most recently deployed mock_aggregator contarct
        price_feed_address = MockV3Aggregator[-1].address

    # Pass priceFeed address to FundMe.sol constructor function and
    # deploy contract from account and publish source code
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        # .get() allows you to get the value if you have added the key in the .yaml file
        # ^ this is used as a way to prevent bugs
        publish_source=config["networks"][active_network].get("verify")
    )

    print(f"Contract deployed to this address: {fund_me.address}")

    # This return allows you to call this function to deploy the Fund Me contract and
    # get the deployed address returned
    return fund_me


def main():
    deploy_fund_me()
