import gzip
import pickle

# Đường dẫn tới file .train
file_path = '/Users/nguyenhien/Downloads/content-2/content/slt-master/data/asllvd.train'

# Đọc file
with gzip.open(file_path, 'rb') as f:
    data = pickle.load(f)

print(data[0])





