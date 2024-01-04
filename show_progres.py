from tqdm import tqdm
import string
import time
data = string.ascii_uppercase
progress = tqdm(data, desc="Processing", unit=" char")
for item in progress:
    progress.set_description("Processing %s" % item)
    time.sleep(1)