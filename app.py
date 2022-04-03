import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()
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
    st.markdown('* Customer complaints are categorized as the customer sentiments using NLP and nltk lib. We have created this feature to understand the customer response towards the services')
    st.bar_chart(customer_sentiment)


    # make other plots
    st.subheader('Trend of Complaint across the years')
    st.markdown('*  Here we can see that in 2017, customer complaints are very high. By clicking on a particular year, you will get specific insights')
    year_cross_tab = pd.crosstab(data['product'], data['year'])
    print(year_cross_tab)
    fig = px.line(year_cross_tab)
    st.write(fig)
    
with plot:
    # make other plots
    st.subheader('Customer sentiments over the issues')
    st.markdown('*  We should make some policies to cater the issues which lies in the negative sentiments of the customer')
    year_cross_tab_1 = pd.crosstab(data['sentiments'], data['issue'][:20])
    print(year_cross_tab_1)
    fig1 = px.bar(year_cross_tab_1)
    st.write(fig1)




    # fig.go.Layout(
    #     show_legend = False,
    #     width=800,
    #     height = 500)
    # margin = dict(
    #     l=1,
    #     r=1
    #     b=1
    #     t=1
    # ),
    # font = dict(
    #     color = "#383635"
    #     size = 15
    # )
    # )
    #st.bar_chart(res, height = 500)

    





    # company_options =data['company'].unique().tolist()
    # company_sec = st.multiselect('Which country complains you want to see',company_options,'Bank of America')
    # print(company_sec)
    # # company1 = data[data['company'] == company_sec[0]]
    # # response = company1[company1['timely_response'] == 'Yes']
    # # data1 = response.filter(['timely_response','company'])
    # # res = company1['timely_response'].value_counts()
    # response = data[data['timely_response'] == 'Yes']
    # res = pd.DataFrame(response['company'].value_counts()).head(20)