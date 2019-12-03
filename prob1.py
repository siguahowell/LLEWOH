import pandas as pd
Math=pd.DataFrame({'Student':['Ice Bear', 'Pandas', "Grizzly"],'Math':[80,95,79]})
Electronics=pd.DataFrame({'Student':['Ice Bear', 'Pandas', "Grizzly"],'Electronics':[85,81,83]})
Geas=pd.DataFrame({'Student':['Ice Bear', 'Pandas', "Grizzly"],'GEAS':[90,79,93]})
Esat=pd.DataFrame({'Student':['Ice Bear', 'Pandas', "Grizzly"],'ESAT':[93,89,88]})
Bears_Left=pd.merge(Math,Electronics, on='Student')
Bears_Right=pd.merge(Geas,Esat, on='Student')
Bears_Grades=pd.merge(Bears_Left,Bears_Right, on='Student')
long=pd.melt(Bears_Grades,id_vars=['Student'],var_name='Subject',value_name='Grades')


