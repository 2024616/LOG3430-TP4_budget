import os

badhash = os.popen("git log -1 --format=%H").read().strip()
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

os.system("git bisect start $badhash $goodhash")
os.system("git bisect run test")