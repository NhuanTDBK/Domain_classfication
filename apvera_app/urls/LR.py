from sklearn.externals import joblib
class LR(object):
    def __init__(self):
        self.model = joblib.load('urls/Pipeline.model')
        self.labels = ["Communication","File-sharing","Other"]
        self.tfidf = joblib.load('urls/TFIDFVec.model')
        self.threshold = 0.7513
    # Url with format xxx.xxx or xxx.yyy.zzz
    def split_webname(self,url):
        return url.split('.')[0]
    def check_threshold_other(self,log_proba):
        prob = max(log_proba)
        # If probability is lower than threshold, its label "Other" will be "Other"
        if prob < self.threshold:
            return 2
        return log_proba.argmax()
    def predict(self,url):
        # There are 3 steps to predict
        # First, get website name by split domain
        # Second, transform text to vec
        # Finally, use threshold to check label
        # input_vec = self.tfidf.transform([self.split_webname(url)])
        # label_index = self.check_threshold_other(self.model.predict_proba(input_vec)[0])
        # return self.labels[label_index]
        input_vec = [self.split_webname(url)]
        label_index = self.check_threshold_other(self.model.predict_proba(input_vec)[0])
        return self.labels[label_index]
