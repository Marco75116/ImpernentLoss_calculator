from math import sqrt

print("Imparnent Loss Calculator")
print("-------------------------")

# symbolA = input("Enter symbol of token A")
# priceA = input("Enter price of token A")

# symbolB = input("Enter symbol of token A")
# priceB = input("Enter price of token A")

symbolA = "USDC"
priceA = 1

symbolB = "MOVR"
priceB = 100

totalValue =10000


def initialAmountToken(priceA, priceB, totalValue):
    amountTokenA = totalValue / (2 * priceA)
    amountTokenB = totalValue / (2 * priceB)
    return (amountTokenA, amountTokenB)


def helpCrypto(endedPriceA, endedPriceB):
    initialsupplyA, initialsupplyB = initialAmountToken(priceA, priceB, totalValue)
    endedTotalValueTokenA = endedPriceA * initialsupplyA
    endedTotalValueTokenB = endedPriceB * initialsupplyB
    endedTotalValue = endedTotalValueTokenA + endedTotalValueTokenB
    return endedTotalValue


def poolFarm(endedPriceA, endedPriceB):
    initialsupplyA, initialsupplyB = initialAmountToken(priceA, priceB, totalValue)
    constantProduct = initialsupplyA * initialsupplyB
    endedAmountTokenA = sqrt(constantProduct * endedPriceB)
    endedAmountTokenB = sqrt(constantProduct / endedPriceB)
    if round(constantProduct, 2) == round(endedAmountTokenB * endedAmountTokenA, 2):
        endedTotalValueTokenA = endedAmountTokenA * endedPriceA
        endedTotalValueTokenB = endedAmountTokenB * endedPriceB
        endedTotalValue = endedTotalValueTokenA + endedTotalValueTokenB
        return endedTotalValue


def impernentLoss():
    ratio = poolFarm(1, 2000) / helpCrypto(1, 2000)
    differenceAbsolu= poolFarm(1, 2000) - helpCrypto(1, 2000)
    print(poolFarm(1, 2000) , helpCrypto(1, 2000))
    print(ratio,differenceAbsolu)


impernentLoss()