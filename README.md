# 📟 MoriahTestRun: Moriah's Hello World Walkthrough

```
A quick end-to-end walkthrough of using the Moriah's cluster. 
```


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



6. Run the following command to run the script (inside the venv):

    `python [lib PATH]/main.py`


### B) Moriah's Cluster Installation


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










###  MAMBA INSTALLATION (recommended for Cluster use because it is fast and light-weight):
```
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
./bin/micromamba shell init -s zsh -r ~/micromamba          # # this is for using the zsh shell, which became the default
./bin/micromamba shell init -s bash -r ~/micromamba       # this is for sbatch scripts, if written in bash
source ~/.zshrc
```







## 🧪 Quick Start




