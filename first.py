import numpy as np
import pandas as pd
import seaborn as sn
import streamlit as st


st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('App for CO2 emission statistics')
st.text(" Here you can find the anaylsis of co2 emission data from 2005 to 2014 in Plymouth")





a= pd.read_csv("co2.csv")

st.dataframe(a)

a1= a.drop(['Transport Total(kt CO2','N. LULUCF Net Emissions kt CO2','Grand Total(kt CO2',
            'Population 000s mid-year estimate',
            'Per Capita Emissions t'],axis=1)
b=a1.mean()
c=b.drop('Year',axis=0)


d=c.idxmax()
e=c.idxmin()




y= st.selectbox('Select',('Average emissions from each contributor',
                           'Highest contributor to CO2 emissions',
                           'Lowest contributor to CO2 emissions'))

if y== 'Average emissions from each contributor':

    av=a1.drop('Year',axis=1)
    avg=av.mean()
    tableav=st.dataframe(avg)
    
    st.write(tableav)


elif y=='Highest contributor to CO2 emissions':



    st.write(d)

elif y=='Lowest contributor to CO2 emissions':

    st.write(e)



y = st.selectbox('Select',('CO2 emission chart for large industrial installations',
                           'CO2 emission chart for road transport',
                           'CO2 emissions chart for rail transport'))

if y== 'CO2 emission chart for large industrial installations':
    
    
    sn.jointplot(x='Year',y='Large Industrial Installations kt CO2',data=a1,kind='scatter')
    st.pyplot()

elif y=='CO2 emission chart for road transport':
    
    sn.jointplot(x='Year',y='Road Transport  A roads kt CO2',data=a1,kind='scatter')
    st.pyplot()



else :
    

    sn.jointplot(x='Year',y='Diesel Railways kt CO2',data=a1,kind='scatter')
    st.pyplot()


    






    
    


              
