# Importing packages:
import math as m
import pandas as pd



class Wind (object):
    # Create a function that calculates the power of a wind turbine given the following variables:
    # the air density, the blade area, the wind speed and the power coefficient of the turbine.
    def __init__(self, density, blade_length, wind_speed, p_coeff):
        # binding the self class to the input variables:
        self.density = density
        self.blade_length = blade_length
        self.wind_speed = wind_speed
        self.p_coeff = p_coeff
        # Writing the equation the converts the input of blade_length to the total swept area of the turbine:
        swept_area = (m.pi * blade_length**2)
        # The core equation that calculates the power of the wind turbine given the above variables:
        power_eval_w = ((0.5 * self.density) * swept_area * (self.wind_speed**3) * self.p_coeff)
        # power_eval calculates the power output in watts, it must be converted into megawatts:
        power_eval_mw = round(power_eval_w/1000000, 5)
        return







print((Wind(1.23, 52, 12,0.4)))


# Creates a data frame by importing data from an external .csv file:
df = pd.read_csv("Test_Wind_Data.csv")

# NOTE: This data cleaning is unique to this data set and may not be necessary depending on how the .csv that is being
# used in formatted #

# Creating a new data frame that contains only the necessary columns: ["Day"],["Month"],["Year"],["WindSpeed"]
df_clean = df.drop(["Sec", "WindDir_deg", "WindDirSTD_deg", "1-secGust_m/s", "3-secGust_m/s",
                    "AtmPr_mb", "AirTemp_°C", "Humidity_%"], axis=1)
df_clean = df_clean.drop([0], axis=0)

print(df_clean.iloc[0, 5])
print(len(df_clean.index))

