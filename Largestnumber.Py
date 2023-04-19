import streamlit as st
a=st.number_input(int(input("first number")))
b=st.number_input(int(input("second number")))
c=st.number_input(int(input("third number")))
if(a>=b) and (a>=c):
  la=a
elif (b>=a) and (b>=c):
  la=b
else:
  la=c
!st.write("largest number",la)
