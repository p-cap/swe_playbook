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