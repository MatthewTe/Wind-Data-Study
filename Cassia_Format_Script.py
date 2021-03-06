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
        # Formatting the data frame into a .datetime component:
        df_clean = df_clean.rename(columns={"Min": "Minute"})
        df_clean["datetime"] = pd.to_datetime(df_clean[['Day', "Month", "Year", "Hour", "Minute"]])
        # searching the data frame for all values that contain the error values of "#NUM!" and removing them:
        df_clean = df_clean[df_clean.iloc[:, 5] != "#NUM!"]
        # declaring the variable self.df_clean for use in the next function:
        self.df_clean = df_clean
        return df_clean

    # Add a description for the compile function:
    def compile(self):
        # declaring a data frame as our previous data frame used in the self.clean() function:
        df = self.df_clean
        # Converting the elements of the data frame into the appropriate variable type:
        df["Day"] = df["Day"].astype(int)
        df["Month"] = df["Month"].astype(int)
        df["Year"] = df["Year"].astype(int)
        df["Hour"] = df["Hour"].astype(int)
        df["Minute"] = df["Minute"].astype(int)
        df["WindSpd_m/s"] = df["WindSpd_m/s"].astype(float)
        # Creating a separate column that contains the calculated wind power values based on the the [WindSpd_m/s]:
        df_append = (self.calc(df["WindSpd_m/s"]))
        # Adding this new column to the existing data frame df:
        df["Power_Output/MWt"] = df_append.values
        # Creating a new, more condensed data frame the contains only the valuable data for visualization,
        # ["datetime"], ["WindSpd_m/s"] and ["Power_Output/MWt"]
        df_calc = df[["datetime", "WindSpd_m/s", "Power_Output/MWt"]]
        self.csv = df_calc
        return df_calc

    # Creating a simple function that writes the now cleaned and compiled data frame to a .csv:
    def output(self, f_name):
        df = self.csv
        self.f_name = f_name
        df.to_csv(self.f_name, index=False)


# Executing the class Wind:
Frame = Wind(1.23, 52, 0.4)
(Frame.clean("Cassia_Wind_Data_Dirty.csv"))
print(Frame.compile())
Frame.output("Cassia_Compiled_Wind_Data.csv")

