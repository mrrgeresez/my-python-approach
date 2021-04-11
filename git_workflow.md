# GIT

First, a bash [http://msysgit.github.com/] is installed for windows.

This is a distributed version control system. The first part means that you keep track of the evolution of files, which you can save at any time (as a backup), and then return to that point if required. Saving this state is called commit. Subsequently, you can continue editing and create other commits. A message should be added to each one with a detailed explanation of changes made, in order to take advantage of another feature, which is the comparison between different versions. Distributed refers to the idea that each developer has a local copy of the repository (the container of all commits), and will connect to propose their changes, so you will see the latest version, but you can work independently.

After installation make sure you edit the global config file to add `git config --global user.name "<your name>"` and `git config --global user.email "<your e-mail>"`.

### Basic usage

If the git repository is already created, usually from the webpage, position yourself in the folder you want to work in, and use `git clone <url of repository>`, this url is found when clicking on clone.

If no repository exists yet, let's start by creating a repository in the folder we choose `git init`, then we ask about the branch we are in and if there are files to manage `git status`. When we add a new file to this folder and do a status it will tell us that there is a file but it is not under review (untracked). To take it into account it will be necessary to add it with `git add fileName`, with this it will enter inside the category of possible commit (staging area). To make the commit `git commit -m "description of the commit"`, with this it will give us information of what happened, if we return to a status we will see that nothing comes out because the actions are already done.

As a basic rule only source files (hello.py) and never generated files (hello.pyc) should be uploaded to the repository. The latter are constantly altered, since they are interpreted by the computer, so they could conflict if they are included, and they also take up more space than the source files. This has to do with the way Git works, since it does not store complete copies of each version, but saves the changes between them, saving space. For binary files (such as images or audios) they will normally be stored complete.

### Staging area and .gitignore

The mentioned staging area is an index, the way to keep track of the changes you want to make in the next commit. If you add them they go from _untracked_ to _to be commited_. At the time you enter this area by doing an _add_ it will have its exact contents, but if you make any changes now we will see that a _status_ tells us that it is both _staged_ and _unstaged_. So there can be three versions of a file: (i) the one you are editing, (ii) the one that was saved in the _staging_ and (iii) the last one that was checked into the repository. A commit will cause these versions to be synchronized.

Each time we do a _status_ it will inform us of the situation, if it comes the case that we don't want some files to be recognized there is a way. Suppose we create a local module that will call our master, for this Python compiles a bytecode (.pyc) and leaves it in the system. From this point on a _pycache_ directory is created to store these files. To ignore the information of this directory we have to include it in a file that we will create in this same folder _.gitignore_, inside we will write `__pycache__`. Now we will also have to commit it. It is especially useful when the editor creates temporary files or copies appear.

### SHA and log

Every time something is stored in the repository a hash function creates a 20 byte SHA ID for the items. It is used to have an index of each item, as well as for each directory. Changes to a file in a directory also produce changes to the directory. Each commit shows the SHA of the top-level directory affected. Often instead of the full 20 bytes you can take those that allow to distinguish it, 7 is usually enough.

With the `git log` command we can list in chronological order the commits made so far. All of them will start with _commit SHA_. 

### Versions and branches

With the log information if we want to check out a previous version of the code we will use git checkout SHA. In this context several terms appear; HEAD refers to the commit you are checking out (referring to an SHA); branch marks a tag over an SHA, identifying its task. If there is one that Git doesn't have, it will ask you to fix it, although sometimes you can work without it. To return to the last commit we can do the same with a checkout indicating the SHA of this one, or the name of its branch, which is always called master to begin with.

The main purpose of these branches is to separate the different parts of a development, instead of uploading it to the master you can work in another branch so as not to interfere with the work of others. If we want to create another branch git checkout -b new_branch that takes us directly to it. This is created wherever we are, if the case is at the beginning of master and we make a log we would see all the previous commits made with master. If now we make a change in a file and we apply add+commit, with later a log we will see that a new element appears. To change to another branch git checkout master, if we make a log, this last change will not appear. To see the differences between two branches we use git show-branch new_rama master, this can give something similar to:

```shell
* [new_branch] commit 4
 ! master] commit 3
--
* [new_branch] commit 4
* [new_rama^] commit 1
* [new_rama~2] added code for feature x
 + [master] commit 3
 + [master^] commit 2
*+ [new_rama~3] created .gitignore
```

The first line indicates the most recent commit in that branch and its description (* will refer to that branch), the second the last commit in the indicated branch. From the separator we see the existing differences. * for new_branch and + for master, if both appear it is the first common commit. The branch names and their variations are a method identifier, if we want to see them as SHA we write git show-branch --sha1-name new_rama master. Once you want to send those changes there are three ways to commit from one branch to another:

+ Merge. The last two SHA of each branch are combined. If in the destination branch the HEAD points to the last SHA a quick merge will be done, positioning the new commits there. To do this:

```shell
git checkout master
git merge new_branch
````

Be careful with conflicts, because if the same section was edited in both branches, git would not know what to do. You could do the reverse path. If someone is working on a different branch and the master is updated affecting your current work, you can commit it to your branch. Being non-destructive it has the problem that it can accumulate a lot of commits and make tracking difficult.

+ Rebasing. Moving a series of commits to a new base, the whole flow is placed in front, integrating different branches. You can achieve a linear history and avoid adding local commits. Care must be taken as it can overwrite other branches and break the workflow.

```shell
git checkout feature
git rebase master
```

+ Cherry-Picking. When you want to add the change of a single commit, not a whole branch. To do this you stand on the branch you want to add and tell it what the SHA of the commit is:

```shell
git cherry-pick SHA
git cherry-pick SHA
```

### Remote repositories

In our github page one of the most interesting options is to make a fork to a repository, that is, we can copy it to our account and experiment with it without affecting the original project. This can be used to propose changes or serve as a starting point for another project. 

The commands described above only work in local repositories, if you want to communicate with a server or over the network there are four main commands:

+ `clone` when you have the repository address and want a local copy. There is a button on github to get this address. The ideal is to make a previous fork and place it in our account, since this way we work with a copy that does not interfere in any way.

  ```shell
  git clone https://github.com/yyy/some.git relay_forked
  ```

  At the end we can include the name of the folder that will contain it. An addition is that we can keep this repository updated. Once it is finished cloning we go to the `cd relay_forked` folder and tell it that it comes from a remote repository (the original), plus a name, _upstream_ is classic.

  ```shell
  git remote add upstream https://github.com/xxx/some.git
  ```

  Once this is done you can update with the following flow, where first you get the updated branches, to take those changes to the master branch (or the one we are working on our forked) we must make a merge (merge original-copy), previously we must ensure that we are in the branch we want:

  ```shell
  git fetch upstream
  git checkout master
  git merge upstream/master
  ```

+ `fetch` to understand it first we have to explain that cloning a repository creates a similar one locally. What it doesn't do is to show locally the branches except master, however it keeps track of the ones that were on the server. To do this it establishes an index that will have a structure like _remotes/origin/<branch_name>_. When a branch is created and its name matches one of the remote one, it will be marked as a tracking branch, it will be useful for _pull_. So what `git fetch` does is to update the branches in _remotes/origin_ and does not touch the local ones.

+ `pull` is the combination of _fetch+merge_. First it updates the branches in _remotes/origin_, if the branch you are tracking does a merge of the corresponding one in _remote/origin_ with yours. Suppose you are on your _new_branch_ and someone has added something to it on the server, with a `git pull` you update the remote branches and do a _git merge remotes/origin/new_branch_. One limitation is that you cannot do this if you have modified files on your local system, however if commits have already been made there is no problem, merge commit.

+ The `push` sends information about the branch you propose to add and asks the remote if they would like to update their version with yours.

### Workflow

It is assumed that you are working on a local repository and have a remote one to push to, plus it will have already been cloned:

1. `git status` the current area is clean.
2. `git pull` get the latest version from the remote, saves merging problems.
3. Edit files.
4. `git status` find changes and watch untracked.
5. `git add [files]` add modified files to staging.
6. `git commit -m "message"` commit.
7. `git push origin [branch-name]` upload the changes to the remote.

