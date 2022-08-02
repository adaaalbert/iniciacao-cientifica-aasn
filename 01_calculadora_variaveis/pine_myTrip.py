# Calculates time, liters of gas used and cost of gas for a trip.

distance = 450                      # kilometer
mileage = 15                        # km/liter
speed = 80                          # km/h - average spped
pricePerLiter = 5.80                # R$ - price of gas

trip_time = distance/speed          # hours
total_gas = distance/mileage        # liters
cost = total_gas*pricePerLiter      # R$
