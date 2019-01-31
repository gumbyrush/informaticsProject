import pandas as pd


divorceData = pd.read_excel("state-divorce-rates.xlsx", skiprows=4, skipfooter=7, index_col=0, header=[0,1])
divorceData = divorceData.stack([0,1]).reset_index()
divorceData.drop(columns=["State"], inplace=True)
divorceData.rename(columns={divorceData.columns[0]:'State',
                            divorceData.columns[1]:'Year',
                            divorceData.columns[2]:"DivorceRate"},
                   inplace=True)
divorceData.to_excel(excel_writer="cleaned_divorce_rates.xlsx", sheet_name="divorceRates")

print(divorceData)


