Dataset **Self Driving Cars** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/S/c/pc/ARUOJDCIurBKNBvfu6wK0Lw45Bu6IQH2HANJWHaFxKZ0VDn0hCC5e7gd24B2bh5ffqjCB6HAp4ceYcaL1yC7fiZUo0OeElXceI0rmLmUoC0XJbICwrtHTiPzUFlB.tar)

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