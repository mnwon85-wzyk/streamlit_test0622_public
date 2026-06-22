import streamlit as st
st.title('3조 건강어플')  #제목 
st.write('이 앱은 의료 데이터를 쉽게 살펴보는 도구입니다!')  #소개이름
name=st.text_input('이름을 입력하세요')  #공란 입력 방법
if name:
    st.write(f'반가워요,{name}님! 함께 시작해요')
else:
    st.info('위에 이름을 입력하시면 다음 질문드릴께요^o^')
    
import pandas as pd
df=pd.read_csv('heart_failure.csv')    
st.subheader('환자 데이터')
st.dataframe(df.head(10)) #상위 10행, st.matric는 숫자지표를 변화량으로 보여줌
st.metric(
    label='전체 환자수',
    value=f'{len(df)}명',
    delta='299건 수집')
avg=df['age'].mean()   #평균 mean
st.metric('평균 나이',f'{avg:.1f}세')  # fstring으로 불러와서 소숫점 .1까지표시

age_max=st.slider('최대 나이',40,95, 70) #마지막 max값이 마지막 70으로
filtered=df[df['age'] <=age_max]
st.write(f'{len(filtered)}')
st.dataframe(filtered)

df=pd.read_csv('heart_failure.csv') 
choice=st.selectbox('성별',['남성','여성'])
code=1 if choice=='남성' else 0
result=df[df['sex']==code]
result1=st.checkbox('사망 환자')
if result1:
    result=result[result['DEATH_EVENT']==1]
st.write(f'{len(result)}명')
st.dataframe(result)
import matplotlib.pyplot as plt
df=pd.read_csv('heart_failure.csv')
fig,ax=plt.subplots()
ax.hist(df['age'],bins=20,color='#5BAFB8')
ax.set_xlabel('age')
ax.set_ylabel('No. of pts')
st.pyplot(fig)

#축 이름 써주기, 표 색깔 지정해주기
counts=df['DEATH_EVENT'].value_counts()
survive1=counts.get(0,0)
death1=counts.get(1,0) 
fig,ax=plt.subplots()
ax.bar(['survive','death'],[survive1,death1],color=["#835BB8","#B85BAC"])
ax.set_ylabel('No. of pts')
ax.set_title('survival vs death count')
st.pyplot(fig)

#표와 차트를 같이 보여주기
st.sidebar.header(" 필터")
age = st.sidebar.slider("최대 나이",
40, 95, 70)
df = df[df['age'] <= age]
c1, c2 = st.columns(2)
c1.metric("환자 수", len(df))
c2.metric("평균 나이", f"{df.age.mean():.0f}")
tab1,tab2=st.tabs(['표', '차트'])
with tab1:
    st.dataframe(df)
with tab2:
    fig,ax=plt.subplots()
    ax.hist(df['age'])
st.pyplot(fig)

