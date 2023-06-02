import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

st.title('시각화 예제')
st.subheader('테스트를 해보자꾸나')

file=st.file_uploader('파일 업로드', type=['csv'])

option=None

with st.sidebar:
    if file:
        df=pd.read_csv(file)
        st.dataframe(df)

        st.subheader('컬럼 선택')

        option = st.selectbox('컬럼 선택',tuple(df.columns))

if option:
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(10,6)
    sns.barplot(x=option, y='survived', data=df, ax=ax)
    # sns.barplot(x=option2,y='survived',data=df, ax=ax[0,1])
    # sns.barplot(x='embarked',y='survived',data=df, ax=ax[1,0])
    # sns.barplot(x='adult_male',y='survived',data=df, ax=ax[1,1])
    st.pyplot(fig)

    # if option:
    #         # fig, ax = plt.subplots(2, 2)
    #         fig, ax = plt.subplots(1, 1)
    #         fig.set_size_inches(10, 6)
    #         sns.barplot(x=option, y='survived', data=df, ax=ax)
    #         # sns.barplot(x='class', y='survived', data=df, ax=ax[0, 1])
    #         # sns.barplot(x='embarked', y='survived', data=df, ax=ax[1, 0])
    #         # sns.barplot(x='adult_male', y='survived', data=df, ax=ax[1, 1])
    #         st.pyplot(fig)