## Workbooks for DEVNET-3620 DNAC Workshop
These iypthon workbooks will be used during the workshop

## Installation
To install

```
virtualenv -p python3 env
source env/bin/activate

pip install -r requirements.txt
(cd uniq; python setup.py install)

```

Alternatively, you can execure the express installation into your home directory (if using a DevNet workstation)
```
cd
git clone https://github.com/aradford123/DEVNET-3620.git
cd DEVNET-3620
./install.sh
git clone https://github.com/CiscoDevNet/dnac-samples-aradford.git
```

After installation:

## Running
./RUN to run the Juypter notebook server

## Cleanup

Can run ./cleanup.sh to clear all the output cells and produce a clean notebook.
