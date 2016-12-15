import git, petname

def processJob(job):
    git.Repo.clone_from(job.repositoryGitUrl, '/tmp/'+petname.Generate(2, '-'))