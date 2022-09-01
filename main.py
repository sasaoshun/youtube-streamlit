
import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'




left_column, right_column = st.columns(2)
button = left_column.button('Show on the right column')
if button:
    right_column.write('This is right column')

expander1 = st.expander('ask your question1')
expander1.write('write your question')
expander2 = st.expander('ask your question2')
expander2.write('write your question')
expander3 = st.expander('ask your question3')
expander3.write('write your question')






