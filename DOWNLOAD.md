Dataset **Self Driving Cars** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/j/V/sY/uu5UHdkCvlxExHxKNVgu9dBJyqto9AQKM0Lje15nSsY59M012EhB4cIu0WGzpBeIYkpL2G7LVgfYM7FEaxZjyJ6UyXiwJInNAbOMUHT9cJDkZSww51khInAwHKSn.tar)

As an alternative, it can be downloaded with dataset-tools package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Self Driving Cars', dst_dir='~/dtools/datasets/Self Driving Cars')
```
The data in original format can be :link: [downloaded here](https://www.kaggle.com/datasets/kumaresanmanickavelu/lyft-udacity-challenge/download?datasetVersionNumber=1)