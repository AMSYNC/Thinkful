# Unit2: lesson 1 - calculating summary statistics on a pandas dataframe

from scipy import stats
import pandas as pd

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''.splitlines()

data = [i.split(', ') for i in data]
column_names = data[0] # creating header
data_rows = data[1::] # reading values
df = pd.DataFrame(data_rows, columns=column_names)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alcmean = df['Alcohol'].mean()
alcmedian = df['Alcohol'].median()
alcmode = stats.mode(df['Alcohol'])
alcmin = min(df["Alcohol"])
alcmax = max(df["Alcohol"])
alcrange = (alcmax - alcmin)
alcvar = df["Alcohol"].var()
alcstd = df["Alcohol"].std()
alcrelvar = (alcstd/alcvar)

tobmean = df["Tobacco"].mean()
tobmedian = df["Tobacco"].median()
tobmode = stats.mode(df["Tobacco"])
tobmin = min(df["Tobacco"])
tobmax = max(df["Tobacco"])
tobrange = (tobmax - tobmin)
tobvar = df["Tobacco"].var()
tobstd = df["Tobacco"].std()
tobrelvar = (tobstd/tobvar)

print "The following are a series of summary descriptive statistics for a dataset outlining the Alcohol and Tobacco consumption in the UK\n"
print "Average weekly household spending (in British pounds) on alcohol and tobacco products\n"
print df
print ""

statnames = ["Measure", "Alcohol", "Tobacco"]
statrows = [["Mean", alcmean, tobmean], ["Median", alcmedian, tobmedian], ["Mode", alcmode, tobmode], ["Minimum", alcmin, tobmin], ["Maximum", alcmax, tobmax], ["Range", alcrange, tobrange], ["Variance", alcvar, tobvar], ["Std. Deviation", alcstd, tobstd], ["Relative Variance", alcrelvar, tobrelvar]]
statdf = pd.DataFrame(statrows, columns=statnames)

print "Summary Statistics\n"
print statdf