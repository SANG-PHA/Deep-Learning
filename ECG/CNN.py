import numpy as np
import pandas as pd
import wfdb

def load_ecg(file):
    record = wfdb.rdrecord(file)
    annotation = wfdb.rdann(file,'atr')
    p_signal = record.p_signal

    assert record.fs == 360, 'sampling freq is not 360'

    symbols = annotation.symbol
    symbol_samples = annotation.sample

    return p_signal, symbols, symbol_samples

def make_dataset(pts, num_sec, fs, abnormal):
    # function for making dataset ignoring non-beats
    num_cols = 2 * num_sec * fs
    X_all = np.zeros((1,num_cols))
    Y_all = np.zeros((1,1))
    sym_all = []

    max_rows = []

    for pt in pts:
        file = data_path + pt
        p_signal, atr_sym, atr_sample = load_ecg(file)

        #grab the first signal
        p_signal = p_signal[:,0]

        #make df to exclude nonbeats
        df_ann = pd.DataFrame({'atr_sym':atr_sym, 'atr_sample':atr_sample})
        df_ann = df_ann.loc[df_ann.atr_sym.isin(abnormal + ['N'])]

        X,Y,sym = build_XY(p_signal, df_ann, num_cols, abnormal)
        sym_all = sym_all + sym
        max_rows.append((X.shape[0]))
        X_all = np.append(X_all, X, axis = 0)
        Y_all = np.append(Y_all, Y, axis=0)

    X_all = X_all[1:, :]
    Y_all = Y_all[1:, :]

    assert np.sum(max_rows) == X_all.shape[0], 'number of X, max_rows rows messed up'
    assert Y_all.shape[0] == X_all.shape[0], 'number of X, Y rows messed up'
    assert Y_all.shape[0] == len(sym_all), 'number of Y, sym rows messed up'
    return X_all, Y_all, sym_all

def build_XY(p_signal, df_ann, num_cols, abnormal):
    #this function builds the X,Y martices for each beat
    #it also returns the original symbols for Y

    num_rows = len(df_ann)
    X = np.zeros((num_rows, num_cols))
    Y = np.zeros((num_rows, 1))
    sym = []

    #keep track of rows
    max_row = 0
    for atr_sample, atr_sym in zip(df_ann.atr_sample.value, df_ann.atr_sym.value):
        left = max([0, (atr_sample - num_sec * fs)])
        right = min([len(p_signal), (atr_sample + num_sec * fs)])
        x = p_signal[left: right]
        if len(x) == num_cols:
            X[max_row, :] = x
            Y[max_row, :] = int(atr_sym in abnormal)
            sym.append(atr_sym)
            max_row += 1
    X = X[:max_row, :]
    Y = Y[:max_row, :]
    return X,Y,sym


data_path = 'ECG 데이터 폴더 경로 입력'
pts = ['환자 번호 배열로 입력']

file = data_path+pts[0]
p_signal, symbols, symbol_samples = load_ecg(file)

#make datasets
num_sec = 3
fs = 360
X_all, Y_all, sym_all = make_dataset(pts, num_sec, fs, abnormal)

# split data into test set and train set
from sklearn.medel_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_all, Y_all, test_size = 0.2, stratify = Y_all, random_state = 12)

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# CNN modeling
from keras.layers import Conv1D, Dense, Flatten, Dropout
from keras.models import Sequential

model = Sequential()
model.add(Conv1D(128, 5, padding='same', activation = 'relu', input_shape(2160,1)))
model.add(Dropout(rate=0.25))
model.add(Flatten(0)
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

model.fit(X_train, Y_train, batch_size=32, epochs=10, verbose=1)

loss, acc = model.evaluate(X_test, Y_test)

print(acc)
