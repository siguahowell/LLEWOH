import pandas as pd
boxes=pd.DataFrame({'Box':['Box 1','Box 1','Box 1', 'Box 2','Box 2', 'Box 2'],'Dimensions':['Length',
                    'Width','Height','Length','Width','Height'],'Value':[6,4,2,5,3,4]})
tidy=boxes.pivot_table(index='Box', columns='Dimensions', values='Value')
tidy["Volume"]=tidy.Length * tidy.Width * tidy.Height



