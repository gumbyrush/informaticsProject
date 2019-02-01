import pandas as pd

#open excel file, skip the meta data at the top and the bottom of the dataset.
divorceData = pd.read_excel("state-divorce-rates.xlsx", skiprows=4, skipfooter=7, index_col=0, header=[0,1])
#change the data from wide format to long format
divorceData = divorceData.stack([0,1]).reset_index()
divorceData.drop(columns=["State"], inplace=True) #inplace=true changes the current dataset, instead of create a copy
#rename columns
divorceData.rename(columns={divorceData.columns[0]:'State',
                            divorceData.columns[1]:'Year',
                            divorceData.columns[2]:"DivorceRate"},
                   inplace=True)
#write to new file
divorceData.to_excel(excel_writer="cleaned_divorce_rates.xlsx", sheet_name="divorceRates")

print(divorceData)


