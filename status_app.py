import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Course, encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Displaced, encoder_Educational_special_needs, encoder_Fathers_occupation, encoder_Fathers_qualification, encoder_Mothers_occupation, encoder_Mothers_qualification, encoder_Scholarship_holder, encoder_Tuition_fees_up_to_date
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/169/169856.png", width=120)
with col2:
    st.header('Empowering Student Growth: Analyzing Academic Status')


data = pd.DataFrame()
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Course = st.selectbox(label='Course', options=encoder_Course.classes_, index=1)
    data["Course"] = [Course]
 
with col2:
    Daytime_evening_attendance = st.selectbox(label='Attendance', options=encoder_Daytime_evening_attendance.classes_, index=1)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
 
with col3:
    Mothers_qualification = st.selectbox(label='Mothers qualification', options=encoder_Mothers_qualification.classes_, index=5)
    data["Mothers_qualification"] = [Mothers_qualification]

with col4:
    Fathers_qualification = st.selectbox(label='Fathers qualification', options=encoder_Fathers_qualification.classes_, index=5)
    data["Fathers_qualification"] = [Fathers_qualification]

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Mothers_occupation = st.selectbox(label='Mothers occupation', options=encoder_Mothers_occupation.classes_, index=1)
    data["Mothers_occupation"] = [Mothers_occupation]
 
with col2:
    Fathers_occupation = st.selectbox(label='Fathers occupation', options=encoder_Fathers_occupation.classes_, index=1)
    data["Fathers_occupation"] = [Fathers_occupation]
 
with col3:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=0)
    data["Displaced"] = [Displaced]

with col4:
    Educational_special_needs = st.selectbox(label='Educational special needs', options=encoder_Educational_special_needs.classes_, index=0)
    data["Educational_special_needs"] = [Educational_special_needs]

col1, col2, col3 = st.columns(3)
 
with col1:
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=1)
    data["Debtor"] = [Debtor]
 
with col2:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition fees up to date', options=encoder_Tuition_fees_up_to_date.classes_, index=1)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
 
with col3:
    Scholarship_holder = st.selectbox(label='Scholarship holder', options=encoder_Scholarship_holder.classes_, index=1)
    data["Scholarship_holder"] = [Scholarship_holder]

col1, col2, col3, col4 = st.columns(4)
 
with col1:
       
    Age_at_enrollment = int(st.number_input(label='Age at enrollment', value=23))
    data["Age_at_enrollment"] = Age_at_enrollment
 
with col2:
    Curricular_units_1st_sem_credited = int(st.number_input(label='1st sem credited', value=3))
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited
 
with col3:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='1st sem enrolled', value=4))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled
 
with col4:
    Curricular_units_1st_sem_evaluations = int(st.number_input(label='1st sem evaluations', value=3))
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations

col1, col2 = st.columns(2)
 
with col1:
    Curricular_units_1st_sem_grade = float(st.number_input(label='1st sem grade', value=169.2))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade
 
with col2:
    Curricular_units_1st_sem_without_evaluations = int(st.number_input(label='1st sem without evals', value=4))
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Previous_qualification_grade = float(st.number_input(label='Qualification grade', value=122.7))
    data["Previous_qualification_grade"] = Previous_qualification_grade
 
with col2:
    Admission_grade = float(st.number_input(label='Admission grade', value=156.3))
    data["Admission_grade"] = Admission_grade
 
with col3:
    Curricular_units_2nd_sem_credited = int(st.number_input(label='2nd sem credited', value=7))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited
 
with col4:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='2nd sem enrolled', value=3))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled
 
col1, col2, col3 = st.columns(3)
 
with col1:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(label='2nd sem evaluations', value=5))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations
 
with col2:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='2nd sem grade', value=809.98))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade
 
with col3:
    Curricular_units_2nd_sem_without_evaluations = int(st.number_input(label='2nd sem without evals', value=2))
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations
 
 

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Status: {}".format(prediction(new_data)))

