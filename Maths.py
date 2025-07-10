#Maths



def PhysicalPriceCalc(matCost, time, yearsXP, galleryCut, creditFee, artShowCost, packingCost, tax, studiotime ):
    timePrice = time * 15
    # yearsMult = yearsXP / 15 + 1
    galleryCutMult = galleryCut / 100 + 1
    creditFeeMult = creditFee / 100 + 1
    artShowCostMult = artShowCost / 15
    taxMod = tax / 100 + 1

    studioMod = yearsXP / studiotime * time
    totalPrice = (timePrice + matCost + artShowCostMult + packingCost + studioMod) * galleryCutMult * creditFeeMult * taxMod
    ProfitPrice = totalPrice * 1.5
    roundedPrice = round(totalPrice, 2)
    ProfitRounded = round(ProfitPrice, 2)
    return roundedPrice, ProfitRounded

def DigitalPriceCalc(matCost, time, StudioCost, galleryCut, creditFee, artShowCost, packingCost, tax, totalPrice, studiotime ):
    
    # yearsMult = yearsXP / 15 + 1
    galleryCutMult = galleryCut / 200 + 1
    creditFeeMult = creditFee / 100 + 1
    artShowCostMult = artShowCost / 15
    taxMod = tax / 100 + 1
    studioMod = StudioCost / studiotime * time
    hourlyPay = totalPrice / galleryCutMult / creditFeeMult / taxMod - (matCost + artShowCostMult + packingCost + studioMod)
    roundedPrice = round(hourlyPay, 2)
    return roundedPrice


def errorCheck(matCost, time, yearsXP, galleryCut, creditFee, artShowCost):
    if matCost == int or matCost == float:
        return True
    elif time == int or time == float:
        return True
    elif yearsXP == int or yearsXP == float:
        return True
    elif galleryCut == int or galleryCut == float:
        return True
    elif creditFee == int or creditFee == float:
        return True
    elif artShowCost == int or artShowCost == float:
        return True
    else:
        return False


# matCost = (input("material cost: "))
# time = (input("time spent making piece: "))
# yearsXP = (input("Years of expertice: "))
# galleryCut = (input("Gallery Cut %: "))
# creditFee = (input("Credit card fees %: "))
# artShowCost = (input("Art show cost: "))

# priceCalc()
# test = "test price"
#