import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCB4MFDnWcaAXHuhMGMiTrp0-EizjR6Hlc")

for m in genai.list_models():
    print(m.name)