import os
import subprocess
import time

def run(cmd, capture=False):
    print(f"Running: {cmd}")
    if capture:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    else:
        subprocess.run(cmd, shell=True, check=True)

print("Starting Achievement Unlocking Script...")

# 1. Quick Draw (Open an issue and close it immediately)
print("\n--- Getting Quick Draw ---")
try:
    run("gh issue create --title 'Quick Draw trigger' --body 'This issue is created and closed immediately to trigger the Quick Draw achievement.'")
    issue_num = run("gh issue list --state open --limit 1 --json number --jq '.[0].number'", capture=True)
    if issue_num:
        run(f"gh issue close {issue_num}")
except Exception as e:
    print(f"Error in Quick Draw: {e}")

# 2. Heart On Your Sleeve (React to an issue/PR)
print("\n--- Getting Heart On Your Sleeve ---")
try:
    if issue_num:
        # Use GitHub CLI to add a reaction
        run(f"gh api -X POST /repos/anishmusician/Advanced-Tg-Uploader/issues/{issue_num}/reactions -f content=heart -H 'Accept: application/vnd.github.squirrel-girl-preview+json'")
except Exception as e:
    print(f"Error in Heart On Your Sleeve: {e}")

# 3. YOLO, Pull Shark, and Pair Extraordinaire
print("\n--- Getting YOLO, Pull Shark, Pair Extraordinaire ---")
try:
    # We will create 2 PRs (2 PRs triggers the bronze Pull Shark)
    for i in range(1, 3):
        branch_name = f"achievement-branch-{i}"
        run(f"git checkout -b {branch_name} main")
        
        with open(f"achievement_dummy_{i}.txt", "w") as f:
            f.write(f"Triggering achievements {i}")
            
        run("git add .")
        
        # Add a Co-author to trigger 'Pair Extraordinaire'
        commit_msg = f"Add dummy file {i} for achievements\n\nCo-authored-by: Octocat <octocat@github.com>"
        with open("msg.txt", "w") as f:
            f.write(commit_msg)
            
        run("git commit -F msg.txt")
        run(f"git push -u origin {branch_name}")
        
        # Create PR
        run(f"gh pr create --title 'Achievement PR {i}' --body 'Merging for achievements'")
        time.sleep(2)
        
        # Merge PR immediately to trigger YOLO (Merging without review)
        run(f"gh pr merge {branch_name} --merge --admin --delete-branch")
        
        run("git checkout main")
        run("git pull origin main")
        time.sleep(2)
        
except Exception as e:
    print(f"Error in PR achievements: {e}")

# Cleanup
if os.path.exists("msg.txt"):
    os.remove("msg.txt")

print("\nDone! Check your GitHub profile achievements page.")
