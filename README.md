# First Contributions

This project aims to simplify and guide the way beginners make their first contribution. If you are looking to make your first contribution, follow the steps below.

#### If you don't have git on your machine, [install it](https://docs.github.com/en/get-started/quickstart/set-up-git).
## Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

![01_fork](https://github.com/user-attachments/assets/786e150a-98c7-489d-a2db-57f55a688b8f)

## Clone the repository
Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the `Code` button, then click the _copy to clipboard_ icon.

![02_code](https://github.com/user-attachments/assets/dfbdb862-b9b2-464c-baa8-eb86f55b8410)

<img align="right" width="300" src="https://github.com/user-attachments/assets/d335f2f8-39b6-4aa9-8fe4-293c41299e95" alt="copy URL" />

Open a terminal and run the following git command:

```bash
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

<!--img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" /-->

For example:

```bash
git clone https://github.com/this-is-you/first-contributions.git
```

where `this-is-you` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```bash
cd first-contributions
```

Now create a branch using the `git checkout` command:

```bash
git checkout -b your-new-branch-name
```

For example:

```bash
git checkout -b add-alonzo-church
```

## Make necessary changes and commit those changes

Now open the `Contributors.md` file in a text editor, and add your name to it. Don't add it at the beginning or end of the file. Put it anywhere in between. Now, save the file.

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```bash
git add Contributors.md
```

Now commit those changes using the `git commit` command:

```bash
git commit -m "Add your-name to Contributors list"
```

replacing `your-name` with your name.

## Push changes to GitHub

Push your changes using the command `git push`:

```bash
git push -u origin your-branch-name
```

replacing `your-branch-name` with the name of the branch you created earlier.

<details>
  <summary> <strong>If you get an errors while pushing, click here:</strong> </summary>
     
  If you get the below error:
  ```
  remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'
  ```
  
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

  If you try to push at this point, you'll still get prompted for username and password and get authentication error.
  To fix this, you'll need to change the remote address on your repo.
  Start by running `git remote -v` to check your remote address.
  
  If it looks anything like this:
  ```
  origin	https://github.com/your-username/your_repo.git (fetch)
  origin	https://github.com/your-username/your_repo.git (push)
  ```
  
  <img align="right" width="300" src="https://github.com/user-attachments/assets/02f8aabd-4d38-4cf3-87d6-0a56794855cd" alt="copy URL" />
  
  Then you will change it using this command:
  ```bash
  git remote set-url origin git@github.com:your-username/your_repo.git
  ```

  The exact url (after `origin`) can be obtained on your GitHub repo, similar to the steps taken when originally [cloning the repo](#clone-the-repository).
  Only difference is, once you have clicked on the `Code` button, you should switch to the `SSH` tab, and click the _copy to clipboard_ icon there.
</details>
