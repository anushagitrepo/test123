print"Hello!"
#abc
from git import Repo,remote
rw_dir='home/ec2-user/testrepo'
repo=Repo(rw_dir)
origin=repo.remote(name='origin')
origin.push()

