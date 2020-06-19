Adversarially Regularized Graph Autoencoder (ARGA)
============

This is a TensorFlow implementation of the Adversarially Regularized Graph Autoencoder(ARGA) model as described in our paper:
 
Pan, S., Hu, R., Long, G., Jiang, J., Yao, L., & Zhang, C. (2018). Adversarially Regularized Graph Autoencoder for Graph Embedding, [https://www.ijcai.org/proceedings/2018/0362.pdf], published in IJCAI 2018: 2609-2615.

![Construction of ARGA](https://github.com/Ruiqi-Hu/ARGA/blob/master/ARGA_FLOW.jpg)

We borrowed part of code from T. N. Kipf, M. Welling, Variational Graph Auto-Encoders [https://github.com/tkipf/gae]


## Installation

```bash
pip install -r requirements.txt
```

## Requirements
* TensorFlow
* python 2.7
* networkx
* scikit-learn
* scipy

## Run from

```bash
python run.py [–-dset {cora, citeseer, pubmed}] [--arch {arga, arvga}] [--task {clustering, link_prediction}] [--run_all]
```

## Models

You can choose between the following models: 
* `arga`: Adversarially Regularised Graph Auto-Encoder
* `arvga`: Adversarially Regularised Variational Graph Auto-Encoder 

## Cite

Please cite following papers if you use this code in your own work:

```
@inproceedings{pan2018adversarially,
  title={Adversarially Regularized Graph Autoencoder for Graph Embedding.},
  author={Pan, Shirui and Hu, Ruiqi and Long, Guodong and Jiang, Jing and Yao, Lina and Zhang, Chengqi},
  booktitle={IJCAI},
  pages={2609--2615},
  year={2018}
}
```
