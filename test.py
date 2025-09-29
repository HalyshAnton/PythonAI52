import pickle


with open('data.pkl', 'rb') as file:
    new_data = pickle.load(file)


print(new_data.info())