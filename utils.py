import numpy as np

def score_topk(clf, valid_x, valid_y, k=5):
    probs = clf.predict_proba(valid_x)
    top_idx = probs.argsort(axis=1)[:,-k:][:,::-1]
    topk = []
    for row in top_idx:
        topk.append([clf.classes_[i] for i in row])
    hit = 0
    for i in range(len(valid_y)):
        y = valid_y[i]
        if y in topk[i]: hit+=1
    return(hit/valid_y.shape[0])

def score_topk_probs(probs, valid_y, k=5):
    top_idx = probs.argsort(axis=1)[:,-k:][:,::-1]
    topk = []
    for row in top_idx:
        topk.append([i for i in row])
    hit = 0
    for i in range(len(valid_y)):
        y = valid_y[i]
        if y in topk[i]: hit+=1
    return(hit/valid_y.shape[0])