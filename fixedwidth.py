import pandas as pd

# This is just a script to expiriment with dataframes and ability to handle fixed width files 

# widths = [42,5,8,16]

colspecs = [(0, 41), (41, 46), (46, 54), (54, 69)]
names = ["name", "status", "date", "value"]
df = pd.read_fwf("fixedwidth.txt", colspecs=colspecs, names=names,index_col=False, parse_dates=[3], infer_datetime_format=True)

# how do I deal with the index column that is created when exporting from a dataframe?
df[2:].to_csv("timeseries_delimited.txt",sep="|",quoting=2,quotechar='^')