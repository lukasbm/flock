# Flock

The idea is to address the pain-points of the current experiment tracking software,
such as WandB, Comet, Neptune, MLFlow, etc.

They all suffer from the same problem. Centralization. They all require you to use their servers to store everything.
The data they log and generate is often not easily accessible and not easily queryable.
Sometimes they even duplicate the data for their own purposes.

Also, often times the runs are not mutable and following up on a run is not easy, as queries become messy.
Other quality of life features such as re-running a run with a different hyperparameter or renaming a tag are not
supported.

Furthermore, these services often lack a proper offline mode, which makes using them on HPC clusters hard.

With *Flock*, we propose a research-first approach.
By focusing on proper offline support, we can ensure that the data is always accessible and queryable.
We also ensure that the data is stored in a way that is easily accessible and queryable by other tools by using
simple format such as CSV rather than a binary database.

## Features

- Track Experiment
- Monitor Hardware Usage
- Re-run Experiments
- Evaluate and Follow up on an experiment

## Design Principles

- Offline First
- Bring your own storage
- Queryable
- Simple
- Language Agnostic (e.g. Python, R, Go, etc.)
- Local Text Files Only
- Configuration agnostic (e.g. you can choose to use hydra, argparse, etc.)
