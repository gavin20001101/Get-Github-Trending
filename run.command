#!/usr/bin/env bash

# Get the curent directory
# https://askubuntu.com/questions/993078/what-does-0-in-shell-scripts-do
dir="${0%/*}"
cd $dir

# https://tomchen.me/2020/03/22/OS/%5BMac&Linux%5D%20bash%20shell%E7%AD%86%E8%A8%98-%20%E7%94%A8shell%20script%E5%9F%B7%E8%A1%8C%E4%BD%A0%E7%9A%84%20Python%E7%A8%8B%E5%BC%8F/
# 設定檔案權限
chmod u+x github_trending.py 

# 執行 github_trending.py
python github_trending.py 

exit