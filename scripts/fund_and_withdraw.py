from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    # Get latest deployed FundMe.sol contract
    fund_me = FundMe[-1]

    # Get account
    account = get_account()

    # Get entrance fee from FundMe.sol smart contract
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)

    # Send/fund minimum amount required to smart contract
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    # Get latest deployed FundMe.sol contract
    fund_me = FundMe[-1]

    # Get account
    account = get_account()

    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
