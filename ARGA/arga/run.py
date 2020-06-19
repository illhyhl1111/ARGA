import argparse
import settings

from clustering import Clustering_Runner
from link_prediction import Link_pred_Runner

import tensorflow.compat.v1 as tf

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dset', type=str, choices=['cora', 'citeseer', 'pubmed'], default='cora')
parser.add_argument('--arch', type=str, choices=['arga', 'arvga'], default='arga')
parser.add_argument('--task', type=str, choices=['clustering', 'link_prediction'], default='link_prediction')
parser.add_argument('--run_all', action='store_true', default=False)
args = parser.parse_args()

import sys
sys.argv = sys.argv[:1]

if args.run_all:
    dsets = ['cora', 'citeseer'] #'pubmed',
    archs = ['arga', 'arvga']
    tasks = ['clustering', 'link_prediction']

    for task in tasks:
        for arch in archs:
            for dset in dsets:
                setting_dict = settings.get_settings(dset, arch, task)

                if task == 'clustering':
                    runner = Clustering_Runner(setting_dict)
                else:
                    runner = Link_pred_Runner(setting_dict)

                runner.erun()
                print('')
                tf.reset_default_graph()

else:
    setting_dict = settings.get_settings(args.dset, args.arch, args.task)

    if args.task == 'clustering':
        runner = Clustering_Runner(setting_dict)
    else:
        runner = Link_pred_Runner(setting_dict)

    runner.erun()

