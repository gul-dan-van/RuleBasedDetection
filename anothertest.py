import os
import joblib
import pickle

# def run_PE(file):
#     os.system("python MLScanner\Extract\PE_main.py {}".format(file))

# run_PE('t.exe')


joblib.load('MLScanner/Classifier/classifier.pkl')
# features = pickle.loads(open(os.path.join('MLScanner/Classifier/features.pkl'),'rb').read())