#!/bin/bash
read -p "Enter Commit Name: " name
git add .
git commit -m name
git push origin master
