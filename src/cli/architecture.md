# Create Experiment

#### Create a new experiment

`flock experiment run python train.py lr=0.01 batch_size=32`

#### Re-run an experiment

`flock experiment rerun vw54ym8`

#### Add Pipeline

`flock pipeline add vw54ym8 evaluate.py`

#### Execute Pipelines

`flock pipeline execute (all|vw54ym8)`

#### Query Experiments

`flock query --filter "lr > 0.01" --sort "lr"`

#### Sync Experiments

`flock sync s3://my-bucket/experiments`

#### Web Interface

`flock web --port 8080`
or
`flock tensorboard --port 8080`

#### Rebuild index

`flock index rebuild`
