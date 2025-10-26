# 📟 MoriahTestRun: Moriah's Hello World Walkthrough

```
A quick end-to-end walkthrough of using the Moriah's cluster. 
```

## ⚠️ Prerequisites

    1. A GitHub account (or other git service account)
    2. Conda/virtualenv/other python library management package
    3. Access to the Moriah's cluster (see miscellaneous section below)
    4. Git setup in your lab folder of Moriah
    5. Micromamba on the Moriah's cluster (see instructions in Miscellaneous Section below)


## 🔍 Instructions 

### A) Local Installation

1. Fork the following repository:

    [https://github.com/kod5kod/MoriahTestRun](https://github.com/kod5kod/MoriahTestRun)

2. Run the following command to clone the forked repository:
    ```
    git clone https://github.com/[username]/MoriahTestRunFork.git
    cd MorahTestRun
    ```

3. Run the following command to create a virtual environment (according to you your preferred library/env manager):

    CONDA Env:  

    `conda create -n moriahtestrun python=3.13`  
    `conda activate moriahtestrun`  


    Python's virtualenv:

    `virtualenv -p python313 moriahtestrun `  
    `source moriahtestrun/bin/activate` # for mac/linux  
    `.\moriahtestrun\Scripts\activate` # for windows    


    Micromamba (recommended in the Cluster - see initial installation instructions below):

    `micromamba create -n moriahtestrun python=3.13`
    `micromamba activate moriahtestrun`

    
4. Install dependencies:

    `pip install -r [lib PATH]/requirements.txt`

5. Add iPython kernel support (optional):

    `ipython kernel install --user --name=moriahtestrun` # adding the kernel to jupyter notebook/lab`


6. Identify your local computer socket host name:

    ```
    import socket
    computer_name = socket.gethostname()
    print(f"\nComputer/node Name: {computer_name}\n")
    ```

7. Edit the `config.json` file according to your user_name and computer_name.


8. Run the following command to run the script (inside the venv):

    `python [lib PATH]/main.py`


9. Commit and push your changes to github. 

    ```
    git add .
    git commit -m "commit message"
    git push
    ```


### B) Moriah's Cluster Installation

    Because the master node is only used for light operations, 
    we will request an interactive session to perform the steps below:

    `srun --mem=10G --pty bash  # Request an interactive session`
    When done:
    `exit`

1. Run the following command to clone the forked repository:

    
    ```
    cd /sci/labs/yuvalb/lee.carlin/[user-name]/ # your Yuval's lab directory
    git clone https://github.com/[username]/MoriahTestRunFork.git
    cd MorahTestRun
    ```

2. Using `micromamba`, create an identical environment as in the local installation:

    `micromamba create -n moriahtestrun python=3.13`
    `micromamba activate moriahtestrun`

3. Install dependencies:

    `pip install -r [lib PATH]/requirements.txt`

4. Deactivate the environment:

    `micromamba deactivate`

5. Run `sbatch` script:

    `sbatch [lib PATH]/sbatch.sh` 

    Review using:  
    `sacct`

    `squeue | grep [user_name]`

    `cat /sci/labs/yuvalb/[user-name]/output/[jobname]_[jobid].out`

6. Check the output file and resource utilization:

    `cat /sci/labs/yuvalb/[user-name]/output/[jobname]_[jobid].out`

    `seff <jobid>`





## Miscellaneous

### Moria's Available resources:

**GPU**:  
    Goldfish: h200 (141 GB).     
    Salmon: L40s (48 GB).   
    catfish: L4 (24 GB).  
     
**CPU**:  
    glacier

    The H200 is for high-performance AI training and HPC, the L40S is a versatile GPU for AI, graphics, and visualization, and the L4 is a low-power, cost-effective GPU primarily for AI inference. The main difference is performance and power, with the H200 offering the most computational power, followed by the L40S, while the L4 focuses on efficiency for inference tasks. 

    

###  MAMBA INSTALLATION (recommended for Cluster use because it is fast and light-weight):

```
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
./bin/micromamba shell init -s zsh -r ~/micromamba          # # this is for using the zsh shell, which became the default
./bin/micromamba shell init -s bash -r ~/micromamba       # this is for sbatch scripts, if written in bash
source ~/.zshrc
```

### zshrc alias setup:

```
alias lab='cd ~/sci/labs/yuvalb/[user_name]'
alias jobs='squeue | grep "user"'
```

### Interactive jbos:
```
srun --mem=10G --pty bash 
srun --gres=gpu:l40s:1 --pty bash # GPU based
```

## Clear user's cache:
`find ~/.cache/ -type f -atime +0 -delete`
Where +0 refers to files accessed in the last 24 hours and more. 
Change the number to the number of days you want to delete.


## Moriah's SSH Config

    For ease of SSHing into Moriah, add the following to your `~/.ssh/config` file:
    (Don't forget to `source ~/.ssh/config` after adding it)

    ```
    ## Moriah config
    # Prevent disconnections
    Host *
        ServerAliveInterval 180
        ServerAliveCountMax 4

    # Configure jump host (for external access)
    Host hurcs-proxy
        User [user_name]
        HostName bava.cs.huji.ac.il
        Port 22

    # Configure cluster access
    Host moriah
        User [user_name]
        HostName moriah-gw.cs.huji.ac.il
        Port 22
        # Comment out ProxyJump when on university network
        ProxyJump hurcs-proxy

    Host moriah-tunnel
        User [user_name]
        HostName moriah-gw.cs.huji.ac.il
        Port 22
        ProxyJump hurcs-proxy
        LocalForward 12345 moriah-gw:22
    ```





## Changelog

## 📌 0.1   2025-10-26
* Adding a base walkthrough for Hello world 
* Added Miscellaneous
* First working version




