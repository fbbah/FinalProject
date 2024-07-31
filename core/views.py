from django.shortcuts import render

#import plotting libraries
import pandas as pd
import plotly.express as px

#Read in CSV as a DataFrame
dataframe = pd.read_csv('core/data/opioid_related_overdose_deaths_2013_2022.csv')

unintentional_overdose_deaths= pd.read_csv('core/data/Strategic_Measure_Number_of_unintentional_overdose_deaths.csv')

k4g8= pd.read_csv('core/data/k4g8-b3sf_version_30.csv')

Hospital_Entries_Overdoses=pd.read_csv('core/data/Drug_Use_Data_from_Selected_Hospitals_20240722.csv')


#function for data analysis of CSV - choose one graph / feature per function.
def chart(request):
    Hospital_Entries_Overdoses_columns = Hospital_Entries_Overdoses.columns
    Hospital_Entries_Overdoses.rename(columns=lambda x: x.strip())
    Hospital_Entries_Overdoses.dropna(subset=[Hospital_Entries_Overdoses_columns[2]], inplace=True)
    Hospital_Entries_Overdoses['INDICATOR'] =Hospital_Entries_Overdoses['INDICATOR'].astype('str')

    #plot variables into a graph
    fig = px.histogram(dataframe, x="Calender_Year", y="Opioid-Related Overdose deaths")

    fig2 = px.scatter(unintentional_overdose_deaths, x="Count of Deaths", y="Unintentional Overdose Death Rate")

    fig3 = px.bar(k4g8, x="race_ethnicity", y="overdose_death_rate", color="race_ethnicity")

    
    fig4 = px.line(Hospital_Entries_Overdoses, x=Hospital_Entries_Overdoses_columns[2], y=Hospital_Entries_Overdoses_columns[8], color=Hospital_Entries_Overdoses_columns[2])
    

    #convert graph to an html object
    chart = fig.to_html()

    chart2 = fig2.to_html()

    chart3 = fig3.to_html()

    chart4 = fig4.to_html()


    #send html object to the url page
    context = {'chart': chart,
                'chart2' : chart2,
                'chart3' :chart3,
                'chart4' : chart4 
    }
    return render(request, 'core/chart.html', context)

