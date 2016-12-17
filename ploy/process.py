import git, yaml
from os.path import join

def processBuild(build, dependencies):
    filesys = dependencies.getFilesystem()
    wcdir = '/tmp/'+build.id
    git.Repo.clone_from(build.repositoryGitUrl, wcdir)
    ymlFileContents = filesys.readfile(join(wcdir, 'ploy.yml'))
    instructions = yaml.load(ymlFileContents)
    build.steps = instructions