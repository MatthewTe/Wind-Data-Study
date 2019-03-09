# Importing packages:
import math as m
import pandas as pd


# Creating a class to store the necessary variables as well as the functions used to calculate wind power and wre-write
# the .csv file.
class Wind (object):
    # Create a function that stores the following variables: the air density, the blade area, the wind speed
    # and the power coefficient of the turbine.
    def __init__(self, density, blade_length, p_coeff):
        # binding the self class to the input variables:
        self.density = density
        self.blade_length = blade_length
        self.p_coeff = p_coeff

    # Creating a function to calculate the power generated from the input wind speed:
    def calc(self, wind_spd):
        self.wind_spd = wind_spd
        # Writing the equation the converts the input of blade_length to the total swept area of the turbine:
        swept_area = (m.pi * self.blade_length ** 2)
        # The core equation that calculates the power of the wind turbine given the above variables in watts:
        power_eval_w = ((0.5 * self.density) * swept_area * (self.wind_spd ** 3) * self.p_coeff)
        # power_eval calculates the power output in watts, it must be converted into megawatts and rounding to four
        # decimal places:
        power_eval_mw = round(power_eval_w / 1000000, 4)
        return power_eval_mw


Frame = Wind(1.23, 52, 0.4)
print(Frame.calc(12))





