# Import
import random

# Variables
weight = random.randint(1,20)
flat_charge_ground_shipping = 20

# Ground Shipping
if weight > 10:
  cost = 4.75 * weight + flat_charge_ground_shipping
elif weight > 6:
  cost = 4 * weight + flat_charge_ground_shipping
elif weight > 2:
  cost = 3 * weight + flat_charge_ground_shipping
else:
  cost = 1.5 * weight + flat_charge_ground_shipping

# Ground Shipping Premium 
ground_shipping_premium_cost = 125.00

# Drone Shipping
if weight > 10:
  drone_cost = 14.25 * weight
elif weight > 6:
  drone_cost = 12 * weight
elif weight > 2:
  drone_cost = 9 * weight
else:
  drone_cost = 4.5 * weight

# Final part
print("The weight of the package is: " + str(weight))
print("The cost of the Ground Shipping option is: " + str(cost) + "$")
print("The cost of the Ground Shipping Premium option is: " + str(ground_shipping_premium_cost) + "$")
print("The cost of the Drone Shipping option is: " + str(drone_cost) + "$")

# Whitespace
print("")
print("")

# The cheapest
all_ = [[cost, "Ground Shipping"], [ground_shipping_premium_cost, "Ground Shipping Premium"], [drone_cost, "Drone Shipping"]]
sorted_all = sorted(all_)
print("The cheapest way is " + sorted_all[0][1] + " and it costs: " + str(sorted_all[0][0]) + "$")
