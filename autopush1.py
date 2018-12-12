import os
import git
from git import *
import git,os,shutil
Folder="/home/ec2-user"
repo=Repo(Folder)
msg='Auto push'
repo.git.add('--all')
repo.index.commit(msg)
origin=repo.remote('origin')
origin.push('master')
