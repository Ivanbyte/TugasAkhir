import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

model = joblib.load('xgb.pkl')
categorical_feature = ['kursus','malam_siang','pernikahan','displaced','educational_special_needs',
                                 'debtor','Tuition','scholarship']

st.title('Status Siswa')

age = st.number_input('Age',min_value=1,step=1)
pernikahan = st.selectbox('Pernikahan',options=['Single','Married','Widower','Divorced','Facto Union','Legally Separated'])
waktu_kuliah = st.selectbox('Jam Belajar',options=['Daytime','Evening'])
debtor = st.selectbox('Berhutang',options=['Yes','No'])
Tuition = st.selectbox('Biaya Pendidikan',options=['Yes','No'])
scholarship = st.selectbox('Scholarship',options=['Yes','No'])
displaced = st.selectbox('Displace',options=['Yes','No'])
educational = st.selectbox('Educational Special Need',options=['Yes','No'])
Course = st.selectbox('Course',options=['Nurising','Management','Social Service','Veterinary Nursing',
                                        'Journalism and Communication',
                                        'Advertising and Marketing Manangement',
                                        'Management (evening attendance)',
                                        'Tourism',
                                        'Communication Design',
                                        'Animation and Multimedia Design',
                                        'Social Service(evening attendance)',
                                        'Agronomy',
                                        'Basic Education',
                                        'Informatics Engineering',
                                        'Equinculture',
                                        'Oral Hygiene',
                                        'Biofuel Production Technologies'])
Curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd sem approved',min_value=0,step=1)
Curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd sem grade',min_value=0,step=1)
Curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd sem evaluations',min_value=0,step=1)
Curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st sem approved',min_value=0,step=1)
Curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st sem grade',min_value=0,step=1)
Curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st sem evaluations',min_value=0,step=1)

input_df = pd.DataFrame([{
    'Age_at_enrollment' : age,
    'Curricular_units_1st_sem_evaluations' : Curricular_units_1st_sem_evaluations,
    'Curricular_units_1st_sem_approved' : Curricular_units_1st_sem_approved,
    'Curricular_units_1st_sem_grade' : Curricular_units_1st_sem_grade,
    'Curricular_units_2nd_sem_evaluations' : Curricular_units_2nd_sem_evaluations,
    'Curricular_units_2nd_sem_approved' : Curricular_units_2nd_sem_approved,
    'Curricular_units_2nd_sem_grade' : Curricular_units_2nd_sem_grade,
    'kursus' : Course,
    'malam_siang' : waktu_kuliah,
    'pernikahan' : pernikahan,
    'displaced' : displaced,
    'educational_special_needs' : educational,
    'debtor' : debtor,
    'Tuition' : Tuition,
    'scholarship' : scholarship
}])

if st.button('Predict'):
    if input_df.isnull().values.any():
        st.error('Tolong isi yang kosong.')
    else:
        input_df[categorical_feature] = input_df[categorical_feature].apply(LabelEncoder().fit_transform)
        prediction = model.predict(input_df)
        if prediction == 0 :
            output = str(prediction)
            st.success(f'Status siswa adalah Dropout')
        elif prediction == 1 :
            output = str(prediction)
            st.success(f'Status siswa adalah Enrolled')
        else :
            output = str(prediction)
            st.success(f'Status siswa adalah Graduate')

