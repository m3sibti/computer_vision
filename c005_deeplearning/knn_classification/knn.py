from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from preprocessing.simplepreprocessor import SimplePreProcessor
from datasets.simpledatasetloader import SimpleDatasetLoader
from imutils import paths
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--dataset', required=True, default='../data/shapes')
ap.add_argument('-n', '--neighbors', type=int, default=1)
ap.add_argument('-j', '--jobs', type=int, default=1)
args = vars(ap.parse_args())

print('[INFO] loading images')
image_paths = list(paths.list_images(args['dataset']))
# print(image_paths)
sp = SimplePreProcessor(32, 32)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels) = sdl.load(image_paths, verbose=500)
data = data.reshape((data.shape[0], 32 * 32 * 3))

print(f'[INFO] feature matrix: {data.nbytes / (1024 * 1024.0):.1f}MB')

le = LabelEncoder()
labels = le.fit_transform(labels)

(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.25, random_state=42)
print(f'[INFO] evaluating KNN Classifier')
model = KNeighborsClassifier(n_neighbors=args['neighbors'], n_jobs=args['jobs'])
model.fit(trainX, trainY)
print(classification_report(testY, model.predict(testX), target_names=le.classes_))
