#!/bin/bash

cd task1
git init

touch 1
touch 2
touch 3
touch 4
touch 5

git add 1
git commit -m "1st"
git add 2
git commit -m "2nd"
git add 3
git commit -m "3rd"
git add 4
git commit -m "4th"
git add 5

git commit -m "5th"
git log --oneline
git checkout -b feature HEAD@{4}

touch 6
touch 7
touch 8
git add 6
git commit -m "6th"
git add 7
git commit -m "7th"
git add 8
git commit -m "8th"

git checkout master
git rebase HEAD~2 --onto feature 

git checkout -b debug HEAD@{11}
touch 9
git add 9
git commit -m "9th"
git reflog
git --no-pager reflog > reflog.txt






