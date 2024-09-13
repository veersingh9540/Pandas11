import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    DF = examinations.groupby(['student_id', 'subject_name']).agg(attended_exams= ('student_id','count')).reset_index()
    DF2 = students.merge(subjects, how= 'cross')
    Final_Df = pd.merge(DF, DF2, on= ['student_id', 'subject_name'], how='right')
    Final_Df['attended_exams'] = Final_Df['attended_exams'].fillna(0)

    return Final_Df[['student_id', 'student_name', 'subject_name','attended_exams']].sort_values(['student_id', 'subject_name'])