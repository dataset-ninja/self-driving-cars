Dataset **Self Driving Cars** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzE0NzVfU2VsZiBEcml2aW5nIENhcnMvc2VsZi1kcml2aW5nLWNhcnMtRGF0YXNldE5pbmphLnRhciIsICJzaWciOiAiR0FmcVB3T2xvbUtuWWkxaHE3RWR4QlBmc2dEbkhYYmQzNjJNd3JyMjJ2UT0ifQ==)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Self Driving Cars', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge/download?datasetVersionNumber=1).