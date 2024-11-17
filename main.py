import streamlit as st

st.title('Điền Thông Tin Giới Thiệu Bản Thân')
my_bar = st.progress(0)

quiz = ['Ho va ten:', 'Ngay thang nam sinh:', 'So thich:']
answers = []
len_quiz = len(quiz)

for i in range(len_quiz):
    answer = st.text_input(quiz[i], '')
    if answer != '':
        answers.append(answer)

if st.button('Confirm'):
    if len(answers) == len_quiz:
        my_bar.progress(100)
        st.write('Ban da hoan thanh day du thong tin!')
        st.balloons()
    else:
        my_bar.progress(len(answers)/len_quiz)
        st.write('Bạn chưa hoàn thành đầy đủ thông tin!')

for i in range(len(answers)):
    st.write(quiz[i], answers[i])
        