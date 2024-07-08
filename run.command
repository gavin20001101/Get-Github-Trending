#!/usr/bin/env bash

# Get the curent directory
dir="${0%/*}"
cd $dir

# 設定檔案權限
chmod u+x github_trending.py 

# 執行 github_trending.py
python github_trending.py 

exit