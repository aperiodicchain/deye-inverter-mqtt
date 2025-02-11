# git - forks

```
# git remote -v
origin      git@github.com:aperiodicchain/deye-inverter-mqtt.git (fetch/push)
upstream    git@github.com:kbialek/deye-inverter-mqtt.git (fetch/push)

# show all branches (local and remote)
git branch --all


# Publish a branch only to my fork (origin) and not to the upstream remote
git checkout -b msa-main
git push origin msa-main

# update+merge my local main branch with upstream main branch
git checkout main
# fetch and merge upstream main
git pull upstream main
# After merging, push the changes to your fork’s main branch on origin:
git push origin main


```

#### Build a new feature-branch

```
git checkout -b feature/my-new-feature
# push the new branch to your local fork on origin:
git push origin feature/my-new-feature
# open PR on Github fork repo

# cherry pick Json-plugin from my msa-main branch:
git checkout msa-main -- ./plugins/deye_plugin_stdout_publisher.py
```