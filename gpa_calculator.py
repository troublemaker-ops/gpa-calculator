import streamlit as st
import pandas as pd


st.title('welcome to gpa calculator')

#amount:amount of subject
def stpm_gpa_calculator(amounts,grade_point):
    total_grade=""
    for grades in grade_point:
        total_grade=+grades
    gpa=total_grade/amounts
    return gpa

def university_gpa_calculator(credit_hour,grade_point):
    total_credit_hour=""
    total_grade=""
    i=0
    for credit in credit_hour:
        total_credit_hour=+credit
    for grades in grade_point:
        grade_hour=grades*credit_hour[i]
        total_grade=+grade_hour
        i=+1
    gpa=total_grade/total_credit_hour
    return gpa

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
if st.button("grade point table"):
    point_table=pd.DataFrame(table)
    st.dataframe(point_table)
st.write("we can help you convert marks or grades into grade points.if you need help ,please click the 'marks or grade converter")
if st.button("marks or grade converter "):
    choice=st.radio("",("mark for grade point","grade for grade point"))
    if choice=="mark for grade point":
        mark=st.number_input("enter marks :")
        gp=point_table_grade(mark)
    else:
        grades_=st.radio("choose your grade:",("A+","A","A-","B+","B","B-","C+","C","C-","D+","F"))
        gp=point_table_grade(grades_)
    st.success(f"your grade is {gp}")

school=st.radio('are you prefer to calculate GPA for?',("STPM","UNIVERSITY"))
amount=st.slider('enter amount of subject',1,10,5)
gra_point=[]
cre_hour=[]
col1,col2=st.columns(2)
j=0
while j<amount:
    if school=="STPM":
        st.subheader(f"subject {j+1}")
        st.write("please enter your grade point")
        gra_point[j] = st.number_input("enter grade point:")

    elif school=="UNIVERSITY":
        st.subheader(f"subject {j+1}")
        with col1:
            st.write("please enter your grade point")
            gra_point[j] = st.number_input("grade point:")
        with col2:
            st.write("please enter your credit hour for this subject")
            cre_hour[j]=st.number_input("credit hour")

    j=j+1
if school=="STPM":
    GPA=stpm_gpa_calculator(amount,gra_point)
elif school=="UNIVERSITY":
    GPA=university_gpa_calculator(cre_hour,gra_point)
else:
    GPA=0
st.success(f"your GPA is {GPA}")