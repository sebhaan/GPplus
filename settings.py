"""
Define directories and options, here as an example for modeling crime offences.
Input file requirements: Input csv file must include one column labeled "region_id" which holds the ID number for each location
and two columns "centroid_x" and "centroid_y" which hold the x and y coordinate for each location, respectively.

If shapefiles need to be processed, the requirement are two input files, one containing the numbers for the the model feature data
(e.g. demographic data) for each region, and another file that contains the shape file for each region. 
Both files are linked via same ID's named as "region_id".
"""

# Main input directory:
data_path = "../data/"
# Filename for main input csv file:
fname_input = "results_DV_year11.csv" # 
# Polygon shapefiles of areas boundaries, only needed if coordinates not already calculated and in main input file:
shape_filename = "abs/shape_files/SA2_2011_AUST.shp" # assumes in data_path directory, optional.
shape_region = 'New South Wales' # set to None if no particular region exctracted and all shapedata should be included, optional.
# If center coordinates already calculated, provide data in main file with two column names "centroid_x" and "centroid_y":
# Filename for crime input data including crime numbers and demographic/environment features
# main output directory
outpath = "../testresults/"
# specific output directory for result plots, maps and tables
outmcmc = outpath # add any subdirectory if required

####### Define options for analysis and visualisation

split_traintest = 0.1 # splits data in train and test data, provide fraction of test
simulate = False # Creates simulated data with 2dim spatial coordinates and 2 features and then runs code on this data.
calc_center = False # Calculates centroids from polygons and converts from Lat/Lng to cartesian with center coord below.
                   # If calc_center = False, coordinates have to be provided in main input file [fname_input]
                   # using the two column names "centroid_x" and "centroid_y"
center_lat = -32.163333  # Latitude coordinate for spatial center for conversion into cartesian coordinates, e.g. NSW centroid
center_lng = 147.016667  # Longitude coordinate for spatial center, e.g. NSW centroid
create_maps = False # creates interactive html maps of crime results, not included for simulated data.
# GP setup
kernelname = 'expsquared' # choose from: 'expsquared', 'matern32' or 'rationalq' (Rational Quadratic)
# MCMC setup; see emcee documentation for more details (http://dfm.io/emcee/current/)
nwalkers = 100 # Number of walkers, recommended at least 2 * Nparameter + 1 (recommended more)
niter = 500 # Number of iterations, recommended at least 500
nburn = 200 # Number of iterations, recommended at least 20% of niter, check sampler chains for convergence.
nfold_cross = 1 # Number of x-fold for cross-validation for test-train sets; set to 1 for only one run 
#(Notes: test first with nfold-cross = 1; computational time ~ nfold_cross; also not all plotting availabable yet for nfold_cross>1)
use_log = False # select false if input features need NOT to be converted into log-space.
# Note that all input features will be normalized from 0 to 1, whether log-space enabled or not. 


###### List of input features

# use population number by area of region instead of just absolute population numbers?
#pop_per_area = True

target_name = 'log_crime_rate'

# Identify features in data that should be used for linear regression
# Names must match column names in header, replace names below accordingly:
x_feature_names = ['Med_tot_hh_inc_wee_C2011',
                   'Med_mortg_rep_mon_C2011',
                   'Med_rent_weekly_C2011',
                  'C11_No_religion_Tot',
                  'C11_Tot_Sep_M',
                  'Med_age_persns_C2011',
                  'Percnt_Unemploy_C11_P',
                   'Brthplace_Elsewhere_2011_Ce_P',
                    'LSH_Eng_only_2011_Ce_P',
                    'C11_P_CL_C_I_II_Tot',
                    'C11_Tot_T',
                    'Tot_persons_C11_P']

# Optionally provide additional description names for features, replace names accordingly:
x_feature_desc = ["Median Tot hhd inc weekly",
                           "Median Mortgage Repay monthly",
                           "Median Rent Weekly",
                           "No Religion",
                           "Male Separated",
                           "Median Age Persons",
                           "Percent Unemployment",
                           "Birthplace Elsewhere",
                           "English Speaking Only",
                           "Education Level Cert12",
                           "Family One Parent",
                           "Population"]

#######################################
