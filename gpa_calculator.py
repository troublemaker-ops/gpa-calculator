import streamlit as st
import pandas as pd


st.title('welcome to gpa calculator')

#amount:amount of subject
def stpm_gpa_calculator(amounts,grade_point):
    total_grade=sum(grade_point)
    gpa=total_grade/amounts
    return round(gpa,2)

def university_gpa_calculator(credit_hour,grade_point):
    total_credit_hour=sum(credit_hour)
    total_grade=sum(g*c for g,c in zip(grade_point,credit_hour))
    gpa=total_grade/total_credit_hour
    return round(gpa,2)

def point_table_marks(marks):
    if 80<marks<100:
        grade_point=4.00
    elif 76<marks<79.99:
        grade_point=3.67
    elif 72<marks<75.99:
        grade_point=3.33
    elif 68<marks<71.99:
        grade_point=3.00
    elif 65<marks<67.99:
        grade_point=2.67
    elif 60<marks<64.99:
        grade_point=2.33
    elif 56<marks<59.99:
        grade_point=2.00
    elif 50<marks<55.99:
        grade_point=1.67
    elif 40<marks<49.99:
        grade_point=1.00
    else:
        grade_point=0
    return grade_point

def point_table_grade(grade):
    grade.upper()
    if grade=="A+" or grade=="A":
         grade_point=4.00
    elif grade=="A-":
         grade_point=3.67
    elif grade=="B+":
        grade_point=3.33
    elif grade=="B":
        grade_point=3.00
    elif grade=="B-":
        grade_point=2.67
    elif grade=="C+":
        grade_point=2.33
    elif grade=="C":
        grade_point=2.00
    elif grade=="C-":
        grade_point=1.67
    elif grade=="D+":
        grade_point=1.00
    else:
        grade_point=0
    return grade_point



table={
    "Letter Grade":["A+","A","A-","B+","B","B-","C+","C","C-","D+","F"],
    "Score Range(%)":["90-100","80-89.99","76-79.99","72-75.99","68-71.99","65-67.99","60-64.99","56-59.99","50-55.99","40-49.99","0-39.99"],
    "Grade Point":[4.00,4.00,3.67,3.33,3.00,2.67,2.33,2.00,1.67,1.00,0.00]
}
st.subheader('this is a calculator for stpm and university student to count their GPA')


if st.checkbox("grade point table"):
    point_table=pd.DataFrame(table)
    st.dataframe(point_table)

st.write("we can help you convert marks or grades into grade points.if you need help ,please click the 'marks or grade converter")

if st.expander("marks/grade converter"):
    choice=st.radio("Choose conversion",("mark -> grade point","grade -> grade point"))
    if choice=="mark -> grade point":
        mark=st.number_input("enter marks :",0,100)
        gp=point_table_grade(mark)
    else:
        grades_=st.selectbox("choose your grade:",table["Letter Grade"])
        gp=point_table_grade(grades_)
    st.success(f"your grade is {gp}")

school=st.radio('are you prefer to calculate GPA for?',["STPM","UNIVERSITY"])
amount=st.slider('enter amount of subject',1,10,5)
if "gra_points" not in st.session_state:
    st.session_state["gra_points"]=[0.0]*amount
if "cre_hours" not in st.session_state:
    st.session_state["cre_hours"]=[1]*amount

st.subheader("Enter your subject:")

for i in range (amount):
    st.markdown(f"Subject: {i+1}")
    col1, col2 = st.columns(2)

    with col1:
       st.session_state["gra_points"][i]=st.number_input(f"Grade point for Subject {i+1}",0.0,4.0,st.session_state.gra_points[i],key=f"gp{i}")
    if school=="UNIVERSITY":
        with col2:
            st.session_state["cre-hours"][i]=st.number_input(f"Credit Hour for Subject {i+1}",1,6,st.session_state.cre_hours[i],key=f"cre{i}")
if st.button("calculate"):
    if school=="STPM":
        GPA=stpm_gpa_calculator(amount,st.session_state.gra_points[:amount])
    elif school=="UNIVERSITY":
        GPA=university_gpa_calculator(st.session_state.cre_hour[:amount],st.session_state.gra_point[:amount])
    else:
        GPA=0
    st.success(f"your GPA is {GPA}")