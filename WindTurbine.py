# Importing packages:
import math as m
import pandas as pd


# Creating a class to store the necessary variables as well as the functions used to calculate wind power and re-write
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

    # Creating the function that extracts the data frame from a .csv and cleans said data frame to include only the
    # the relevant data:
    def clean(self, csv):
        self.csv = csv
        # Creates a data frame by importing data from an external .csv file:
        df = pd.read_csv(csv)
        # Creating a new data frame that contains only the necessary columns: ["Day"],["Month"],["Year"],["WindSpeed"]
        df_clean = df.drop(["Sec", "WindDir_deg", "WindDirSTD_deg", "1-secGust_m/s", "3-secGust_m/s",
                            "AtmPr_mb", "AirTemp_°C", "Humidity_%"], axis=1)
        df_clean = df_clean.drop([0], axis=0)
        # declaring the variable self.df_clean for use in the next function:
        self.df_clean = df_clean
        return df_clean

    # Creating a function that consumes the int num_rows which row in the data frame the function will draw variables
    # from. The function then uses the values in the selected column as input for the self.calc() function to calculate
    # power output of a wind turbine. (It is assumed that the selected column contains wind speed variables:
    def compile(self, num_rows):
        self.num_rows = num_rows
        # declaring a data frame as our previous data frame used in the self.clean() function:
        df = self.df_clean
        # Applies the self.calc() function to the variable pulled from the data frame:
        # the values in the .csv are stored as strings so they need to be converted into a floating point decimal:
        return self.calc(float(df.iloc[0,self.num_rows]))


Frame = Wind(1.23, 52, 0.4)
print(Frame.clean("Test_Wind_Data.csv").head())
print(Frame.compile(5))


