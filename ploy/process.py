import git, petname

def processBuild(build):
    git.Repo.clone_from(build.repositoryGitUrl, '/tmp/'+petname.Generate(2, '-'))