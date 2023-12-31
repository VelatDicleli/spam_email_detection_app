import streamlit as st #veri bilimi için kolayca web uygulama yapımını sağlar
import joblib #model kaydetme, tekrar tekrar kullanma işlemini sağlar
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import string
import nltk

nltk.download('stopwords')
nltk.download('punkt')

model = joblib.load("ml_models/model_svc.pkl") #favorimiz olan svc algoritmamızı alalım ...



stop_words = set(stopwords.words('english'))


def clean_text(text):

    text = ''.join([char for char in text if char not in string.punctuation])
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha()]
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)


#web uygulaması

st.title('spam email detection application')
metin = st.text_area("Textbox", value='', height=300)
metin=clean_text(metin)


if st.button('Submit'):
    if len(metin)!=0: #kullanıcı metin girerse
        tahmin = model.predict([metin])
        if tahmin[0] == 1:
            
            st.error("🚫 This is spam mail.")
        
        else: 
        
            st.success("✅ This is not spam mail.")
        
   
    else: #kullanıcı metin girmezse
        st.warning("please fill the textbox !")

        
