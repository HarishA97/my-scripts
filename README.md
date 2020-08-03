# yarn-deduplication
Removes duplicates in yarn.lock.

A duplicate package is when two dependencies are resolved to a different version, even when a single version matches the range specified in the dependencies.

## Usage
Clone the repo.

Run deduplicate.py and supply the file name.

```python3 deduplicate.py```