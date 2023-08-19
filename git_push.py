import git
from getpass import getpass

def git_push(repo_path='.', remote_url='https://github.com/mirzamukkarambaig/projects.git'):
    # Initialize the repository
    repo = git.Repo(repo_path)
    
    # Set the origin URL
    try:
        origin = repo.remote(name='origin')
        origin.set_url(remote_url)
    except git.exc.NoSuchPathError:
        repo.create_remote('origin', url=remote_url)

    # Check if there are any changes
    if repo.is_dirty():
        # Add all changes
        repo.git.add(A=True)
        
        # Commit
        commit_message = input("Enter commit message: ")
        repo.index.commit(commit_message)

        # Push to GitHub
        try:
            origin.push(refspec='HEAD:main')  # Push to the main branch
            print("Changes pushed to GitHub!")
        except git.exc.GitCommandError as error:
            print(f"Error pushing to GitHub: {error}")
    else:
        print("No changes detected.")

if __name__ == "__main__":
    git_push()
