import git
from getpass import getpass

def git_push(repo_path='.'):
    # Initialize the repository
    repo = git.Repo(repo_path)

    # Check if there are any changes
    if repo.is_dirty():
        # Add all changes
        repo.git.add(A=True)
        
        # Commit
        commit_message = input("Enter commit message: ")
        repo.index.commit(commit_message)

        # Push to GitHub
        try:
            origin = repo.remote(name='origin')
            origin.push(refspec='HEAD:main')  # Push to the main branch
            print("Changes pushed to GitHub!")
        except git.exc.GitCommandError as error:
            print(f"Error pushing to GitHub: {error}")
    else:
        print("No changes detected.")

if __name__ == "__main__":
    git_push()
