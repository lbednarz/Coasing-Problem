# CoastingProblem
 pilot signals research

 # Using Git LFS in this repository

This repository uses Git LFS to store large files. When you clone this repository, the LFS files will not be downloaded by default. Instead, Git LFS will download the files on demand as you use them. To get started with the LFS files, follow these steps:

1. Install Git LFS on your local machine. You can download it from the Git LFS website: https://git-lfs.github.com/

2. Clone this repository to your local machine:

git clone <https://github.com/lbednarz/PhDResearch.git>


3. Navigate to the cloned repository:

cd <PhD-Research>


4. Run the following command to download the LFS files:

git lfs pull 

This command will download all the LFS files in the repository. Depending on the size of the files and your internet connection, this may take some time.

5. You can now use the LFS files as you would any other files in the repository.

Note: If you want to clone this repository and download the LFS files in one step, you can use the `git clone --recurse-submodules <https://github.com/lbednarz/PhDResearch.git>` command instead of step 2. This will download both the repository and the LFS files in one go.
