# import os

# badhash = os.popen("git log -1 --format=%H").read().strip()
# goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

# os.system(f"git bisect start {badhash} {goodhash}")
# os.system("git bisect run test")


import os

bad_hash = os.popen("git log -1 --format=%H").read().strip()
good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

if not bad_hash or not good_hash:
    print("Error: BAD_COMMIT and GOOD_COMMIT environment variables are required.")
    exit(1)

def run_bisect():
    os.system(f"git bisect start {bad_hash} {good_hash}")
    os.system("git bisect run python manage.py test")
    os.system("git bisect reset")

if __name__ == "__main__":
    run_bisect()