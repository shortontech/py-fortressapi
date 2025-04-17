from enum import Enum

class PaymentType(Enum):
    INTERNAL:str = "internal"
    CARD_DEPOSIT = "cardDeposit"
    CARD_WITHDRAW = "cardWithdrawal"
    ACH_DEPOSIT = "achDeposit"
    ACH_WITHDRAW = "achWithdrawal"
    WIRE_DEPOSIT = "wireDeposit"
    WIRE_WITHDRAWAL = "wireWithdrawal"
    BUY_CRYPTO = "buyCrypto"
    SELL_CRYPTO = "sellCrypto"
    DEPOSIT_CRYPTO = "depositCrypto"
    WITHDRAWAL_CRYPTO = "withdrawalCrypto"
   INTERNAL_CRYPTO = "internalCrypto"