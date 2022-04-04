import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()
plot1 = st.container()
plot2  =st.container()
plot3 = st.container()
plot = st.container()
st.markdown(
    """
    <style>
    .main{
        background-colr: #F5F5F5
        }
    </style>
    """,
    unsafe_allow_html = True
)


# @st.cache
# def get_data():
#     data = pd.read_csv('customer_reduce.csv')
#     return data
# to write in container
with header:
    st.title("DASHBOARD FOR ADMIN PANEL")
    st.text('This dashboard helps the policy makers to make decision for better customer services')


with dataset:
    st.header("Customer - Sentiments (through complaints)")
    data = pd.read_csv('deployment.csv')
    # data.drop(['Unnamed: 0'], axis=1, inplace= True)
    # remove NaN values from sub_issue, tags, state, zipcode, timely_response, complaint_id, consumer_disputed?
    # data["sub_product"] = data["sub_product"].fillna(data["sub_product"].mode()[0])
    # data["sub_issue"]= data["sub_issue"].fillna(data["sub_issue"].mode()[0])
    # data["company_public_response"]= data["company_public_response"].fillna(data["company_public_response"].mode()[0])
    # data["tags"]= data["tags"].fillna(data["tags"].mode()[0])
    # data["clean_text"]= data["clean_text"].fillna(data["clean_text"].mode()[0])
    st.write(data.tail(40)[:5])
    customer_sentiment = pd.DataFrame(data['sentiments'].value_counts())
    st.subheader('Sentiment Analysis Using NLP ')
    st.markdown('* Customer complaints are categorized as the customer sentiments using NLP and nltk library. We have created this feature to understand the customer responses or complaints towards the services')
    st.bar_chart(customer_sentiment)


    # make other plots
    st.subheader('Trend of Complaint Across The Years')
    st.markdown('*  This double line chart is showing value and the products or services over the different period of time of 2015 and 2016 as we observe that in 2015 about 13k debt has been collected the value of money transfer has drop but it has been raised for mortgage.')
    year_cross_tab = pd.crosstab(data['product'], data['year'])
    print(year_cross_tab)
    fig = px.line(year_cross_tab)
    st.write(fig)
    
with plot:
    # make other plots
    st.subheader('Customer Dispute of Specific Company')
    st.markdown('*  Here in this stacked bar chart it is easy to see at a glance what percentage of customers dispute on each company at particular time period. Policy makers can easily detect trend ofthe dispute of customer.')
    year_cross_tab_1 = pd.crosstab(data['sentiments'], data['issue'][:20])
    print(year_cross_tab_1)
    fig1 = px.bar(year_cross_tab_1)
    st.write(fig1)

with plot1:
    # make other plots
    st.subheader('Customer Sentiments Over The Issues')
    st.markdown('*  In this particular stack chart we have visualize the the no of customers and the reasons of disputes how much customers have disputed over which specific dispute here we can see that most of the disputes were over loan servicing, payments, escrow accounts and other most visible issue is debt collection.')
    year = data['year'].unique().tolist()
    fig2 = px.bar(data, x='year',y='consumer_disputed',color='company'[:10], labels={'consumer_disputed':'Customer dispute over the years'}, height=400)

    fig2.update_layout(width=800)
    st.write(fig2) 

with plot2:
    st.subheader('Representing Companies in a range of Complaints')
    comp = data['company'].value_counts()
    scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]
    data1 = [go.Choropleth(
    colorscale = scl,
    autocolorscale = False,
    locations = comp.index,
    z = comp.values,
    locationmode = 'USA-states',
    text = comp.index,
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "Complaints")
    )]

    layout = go.Layout(
    title = go.layout.Title(
        text = 'Complaints by State<br>(Hover for breakdown)'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(100,149,237)'),
)

    fig3 = go.Figure(data = data1, layout = layout)
    st.write(fig3)

with plot3:
    st.subheader('Top 10 Companies receiving most complaints')
    st.markdown('*  In this particular stack chart we have visualize the the no of customers and the reasons of disputes how much customers have disputed over which specific dispute here we can see that most of the disputes were over loan servicing, payments, escrow accounts and other most visible issue is debt collection.')
    comp_dist = data['company'].str.strip("'").value_counts()[0:10]
    fig4 = {
        "data": [
    {
      "values": comp_dist.values,
      "labels": comp_dist.index
      ,
      "domain": {"column": 0},
      "name": "Company Complaints",
      "hoverinfo":"label+percent+name",
      "hole": .4,
      "type": "pie"
    },
    ],
        "layout": {
        "title":"Companies Vs Complaints",
        "grid": {"rows": 1, "columns": 1},
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "Company",
                "x": 0.5,
                "y": 0.5
            }
        ]
    }
}
    fig4 = go.Figure(data = fig4, layout = layout)
    st.write(fig4)
    # st.write(fig4)
    #plot(fig4)
