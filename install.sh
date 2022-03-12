#!/bin/bash
export PATH=/root/miniconda3/bin:$PATH

python -m -pip install -upgrade pip
pip install fabric -i https://pypi.douban.com/simple --trusted-host=pypi.douban.com