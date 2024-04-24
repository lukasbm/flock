# Tracking

- Runtime
- Monitor Hardware
- Monitor Software Env (python etc.)
- Monitor Code / Git version

# Log

have log methods that are a nice wrapper but essentially just write to local files.

# Files

Q: How should files be versioned?
A: up to the user? maybe just use git LFS? (it's all local files, nothing binary) OR use DVC (data version control)

Q: How to deal with file conflicts?
A: Since there isn't a central server or another entity with a single source of truth, this needs to be resolved by the
user.

# Syncing

should support the following for syncing

- S3
- WebDav
- FPT
- SFTP
- SCP / SSH

# Web

- tensorboard integration
- jupyter integration?
- web interface for sorting runs, etc. (this could be essentially equal to CLI)

# Cli

- Start runs (would not work if the run command is something like `python hydra.py --multirun`)
- Restart runs
- Create Index
- Upload/Sync

# Run

- Expose flock config as env variables
- Set working directory
- Create directories

# Post-processing (evaluation / analysis of a run)

- Be able to register pipelines to an experiment (e.g calculating metamer image metrics)
- Using the CLI these pipelines are then started and the results are stored in the experiment directory
- the outputs of a pipeline (should they have to be defined in the pipeline beforehand?) are hashed (the entire output
  folder) to avoid duplicate computation.

# Querying

- Runs should be requested in a simple table format and then filtered in the processing language.
    - E.g pandas in python, data.frame in R, etc.
    - This is the part that should be ported to other languages (e.g R and Go)

# Metrics / Logging

- Support log text and numerical data
- Media data like images and checkpoints should just be saved to disk.
- Steps can be assigned multiple times, the data can be averaged in this case (numerical only) (e.g. this relates to the
  problem with the learning rate curve i have with my current setup)
- 