from eth_account import Account
from brownie import FundMe
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    # Get an account
    account = get_account()

    # Get deployed contract
    fund_me = deploy_fund_me()

    # Get minimum amount required to fund FundMe contract
    entrance_fee = fund_me.getEntranceFee()

    # Fund contract with minimum value
    transaction = fund_me.fund({"from": account, "value": entrance_fee})

    # Wait one block
    transaction.wait(1)

    # Check if our funding was recorded correctly in addressToAmountFunded mapping
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    # Withdraw all fund from Fund Me contract
    transaction2 = fund_me.withdraw({"from": account})

    # Wait one block
    transaction2.wait(1)

    # Check if all funds have been successfully
    assert fund_me.addressToAmountFunded(account.address) == 0


def main():
    pass
