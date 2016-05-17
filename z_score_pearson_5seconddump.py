import numpy as np
from scipy.stats import pearsonr
import cPickle

z_scores = np.load('raw_z_npdump.dump')

channels_data = []


def calculate_pearson(start):
    for interval in range(len(z_scores[start])/5000 + 1):
        j = 5000*interval
        print j, interval
        if interval == len(z_scores[start])/5000 + 1:
            for index in range(64):
                if start < index:
                    channels_data.append(pearsonr(z_scores[start][j:], z_scores[index][j:])[0])
        else:
            for index in range(64):
                if start < index:
                    channels_data.append(pearsonr(z_scores[start][j:j+5000], z_scores[index][j:j+5000])[0])


def dump_z_score_pearson():
    with open('z_score_pearson_5second_dump.dump', 'wb') as f:
        cPickle.dump(channels_data, f)


if __name__ == '__main__':
    for i in range(64):
        print 'Calculating Channel %s' % i
        calculate_pearson(i)
    dump_z_score_pearson()

