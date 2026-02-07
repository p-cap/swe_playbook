### The story of divergent branches
- Early mornining that consists of beautiful weather of 40 degrees and the screeching sound coming from our pet turtles, I logged into my digital world of inside the Solarized Dark vscode environment, I was about to save an unsaved jupyter notebook that had a snippet of two sum approach in brute force fashion. This solution was still an acceptabl approach according to my buddy leetcode. I gracefully saved my file and was ready to update my repo with the file addition. I called `git status` and it told me that I have an untracked file and I need to use `git add <file>` pointing to the file that will be committed. Why in the world would I need to add a file first before committing my changes? Well, let me phone a friend? Gemini, "What does add really mean". Gemini comes back to me and says, it's like saying, Hey, Git, take a look at these changes-- I want these included in the next snapshot. This process is known as staging. Snapshot? Yes, git add tracks the state of the file at the moment we ran the command. git add takes the snapshot for the file. So I run `git add .` to take the snapshot of my file. Then I ran git commit -m'*******'. Git tells me, 1 file change, 83 insertions. My buddy, Gemini, also mentioned that `git commit -m yada,yada,yada` essentially takes a snapshot of the project. After that commitment, I'm ready to shove my changes via `git push` and I thought all was find and dandy until I hit git scolding me and essentially saying 'You have divergent branches and need to specify how to reconcile them.' To git's credit, git gave me a couple of options, I can either merge, rebase, or fast-forward only. I blindly picked `git config pull.rebase false`. This sets my git config and say that on every pull, I will not rebase but instead create a new merge commit that brings the last commit from my remote repo and the last commmit from my local. So now, I pull the changes from my remote repo and now it is reflected on my local repo. The changes were mostly additions so setting the pull rebase attribute was not an issue. Now, let's shove those changes to our remote repo. All worx. Nice. 

[07:45:42] ~/dsa/python/repo/swe_playbook main>> git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        redos/two-sum-BF.ipynb

nothing added to commit but untracked files present (use "git add" to track)
[07:45:45] ~/dsa/python/repo/swe_playbook main>> git add . 
[07:45:50] ~/dsa/python/repo/swe_playbook main>> git commit -m 'brute force to two sum'
[main da80437] brute force to two sum
 1 file changed, 83 insertions(+)
 create mode 100644 redos/two-sum-BF.ipynb
[07:46:16] ~/dsa/python/repo/swe_playbook main>> git push
To https://github.com/p-cap/swe_playbook.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/p-cap/swe_playbook.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
[07:46:19] ~/dsa/python/repo/swe_playbook main>> git pull
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (7/7), done.
remote: Total 9 (delta 2), reused 9 (delta 2), pack-reused 0 (from 0)
Unpacking objects: 100% (9/9), 2.78 KiB | 219.00 KiB/s, done.
From https://github.com/p-cap/swe_playbook
   71b31bf..b35a578  main       -> origin/main
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
[07:46:28] ~/dsa/python/repo/swe_playbook main>> git config pull.rebase false 
[07:47:14] ~/dsa/python/repo/swe_playbook main>> git pull                    
Merge made by the 'ort' strategy.
 stacks/minstack.ipynb                | 110 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 stacks/reverse-polish-notation.ipynb |  88 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 stacks/valid-stacks.ipynb            | 100 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 298 insertions(+)
 create mode 100644 stacks/minstack.ipynb
 create mode 100644 stacks/reverse-polish-notation.ipynb
 create mode 100644 stacks/valid-stacks.ipynb
[07:47:42] ~/dsa/python/repo/swe_playbook main>> 




### The story of the unverified commits
It all started when I was looking all of my commit-"MENTS".....scary. I realized that the git commits for my repo are "unverified"....Unverified? According to my friend, git, I'm git's buddy so I call her gitty. So gitty's docs says, because I enabled vigilant mode, all my commits are tagged "unverified" if it's any of the following:
- the commit is signed but the signature could not be verified
- the commit is NOT signed and the committer has vigilant mode is enabled
- the commit is NOT signed and the author has vigilant mode enabled

[08:35:03] ~/dsa/python/repo/swe_playbook main>> ssh-keygen -t ed25519 -C "slashedeye@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/pckap/.ssh/id_ed25519): .ssh/my_key
Enter passphrase for ".ssh/my_key" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in .ssh/my_key
Your public key has been saved in .ssh/my_key.pub
The key fingerprint is:
SHA256:QkWVx+D7oOLkzTEJJANx8Iq4kjSEgPRg8qaiMdixCgY slashedeye@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|=++o.  .o.o+     |
|*.o+   . .. o    |
|E.+.+ o   ..     |
|== + =     .     |
|X++   o S o      |
|**.    o o o     |
|*     o =   .    |
|.    + + o       |
|      o o        |
+----[SHA256]-----+
[08:35:33] ~/dsa/python/repo/swe_playbook main>> git config core.sshCommand "ssh -i $(pwd)/.ssh/my_key"    


08:41:02] ~/dsa/python/repo/swe_playbook main>> git remote -v
origin  https://github.com/p-cap/swe_playbook.git (fetch)
origin  https://github.com/p-cap/swe_playbook.git (push)
[08:42:54] ~/dsa/python/repo/swe_playbook main>> git remote set-url origin git@github.com:p-cap/swe_playbook.git
[08:43:07] ~/dsa/python/repo/swe_playbook main>> git config -l
credential.helper=osxkeychain
init.defaultbranch=main
includeif.gitdir:~/personal/.path=~/.gitconfig-personal
includeif.gitdir:~/work/.path=~/.gitconfig-work
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true
core.sshcommand=ssh -i /Users/pckap/dsa/python/repo/swe_playbook/.ssh/my_key
remote.origin.url=git@github.com:p-cap/swe_playbook.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.main.remote=origin
branch.main.merge=refs/heads/main
user.name=p-cap
user.email=slashedeye@gmail.com
pull.rebase=false
[08:43:44] ~/dsa/python/repo/swe_playbook main>> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   readme.md

no changes added to commit (use "git add" and/or "git commit -a")
[08:44:10] ~/dsa/python/repo/swe_playbook main>> git commit -a
[main f9d22c4] testing ssh config
 1 file changed, 3 deletions(-)
[08:44:24] ~/dsa/python/repo/swe_playbook main>> git push
Enter passphrase for key '/Users/pckap/dsa/python/repo/swe_playbook/.ssh/my_key': 
Enter passphrase for key '/Users/pckap/dsa/python/repo/swe_playbook/.ssh/my_key': 
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 290 bytes | 290.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To github.com:p-cap/swe_playbook.git
   4ca2a7f..f9d22c4  main -> main
[08:44:43] ~/dsa/python/repo/swe_playbook main>> 

reference:
 git config core.sshCommand "ssh -i $(pwd)/.ssh/my_key" 