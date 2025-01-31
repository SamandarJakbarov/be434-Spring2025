# Getting started on the HPC

Not enough compute time on replit? You can use the HPC!

Because you can easily run through all of your hours in replit, I am offering another option for you to use VScode on the campus HPC. Note that VScode also allows you to view and try out the campus 

## What is the HPC?

HPC is an acronym for "high-performance computing," and it generally means using a cluster of computers. Students have access to several clusters (puma, ocelote, elgato) at the University of Arizona. In our case, we are going to use ocelote, our training cluster.

## Steps for HPC access

To get started, please make sure that you have completed these steps:

1. Enroll in Netid+ to access HPC systems. https://webauth.arizona.edu/netid-plus/

2. Create an HPC Account (if you don't already have one). https://account.arizona.edu

3. You should have received an invitation from me to access the HPC and join the bh_class group.

## Accessing VSCode on the HPC

You can write Python code using the VSCode GUI on the HPC. To access VScode use the following steps:

1. Go to the HPC web-portal: https://ood.hpc.arizona.edu/pun/sys/dashboard and login with your UA net-id and password. 

2. On the top menu bar select "My Interactive Sessions" and "VSCode GUI" from the pull-down list.

3. A settings/launch page will open for you. Select "Ocelote" for the cluster and "bh_class" for the PI group, while keeping all other defaults. Next, select launch to start the VSCode session.

## Cloning your GitHub Repository on the HPC

Next, you will need to clone your GitHub repository for the class on the HPC in your home directory. To do this follow these steps:

1. In the VSCode app, select Terminal -> new terminal from the top menu bar.
2. In the terminal window type the following commands:
!!! Be sure to change the link to your repository !!!

cd
git clone git@github.com:[YOUR GITHUB ID]/be434-Spring2025.git

That's it! You should now have a copy of the code on the HPC. Note that the HPC or replit can be your working code repository. They will both write back to your main GitHub code repository when you "commit" and "push" your changes.