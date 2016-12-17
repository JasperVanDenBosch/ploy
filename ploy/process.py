import git, petname

def processBuild(build):
    git.Repo.clone_from(build.repositoryGitUrl, '/tmp/'+build.id)