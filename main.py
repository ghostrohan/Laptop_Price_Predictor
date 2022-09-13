import streamlit as st
import numpy as np
import pickle

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")
# Brand
Brand = st.selectbox('Brand', df['Company'].unique())
# Type of Laptop
Type = st.selectbox('Type', df['TypeName'].unique())

# RAM
ram = st.selectbox('RAM(in GB)', df['Ram'].unique())
# Weight
w = st.number_input('Weight of Laptop')
# Touch Screen
touchscreen = st.selectbox('TouchScreen', ['No', 'Yes'])
# IPS Display
ips = st.selectbox('IPS', ['No', 'Yes'])
# Screen Size
screen_size = st.number_input('Screen_Size')
# resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

# cpu
cpu = st.selectbox('CPU', df['Cpu_Name'].unique())

hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])

gpu = st.selectbox('GPU', df['Gpu'].unique())

os = st.selectbox('OS', df['OS'].unique())

if st.button('Predict Price'):
    # query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([Brand, Type, ram, gpu, w, touchscreen, ips, ppi, cpu, hdd, ssd, os])

    query = query.reshape(1, 12)
    st.subheader("The predicted price of this configuration is: Rupee " + str(int(np.exp(pipe.predict(query)[0]))))