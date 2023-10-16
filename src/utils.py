import hashlib
import json


# construct sample id from sample
# use md5 hash of requested rewrite
def get_sample_id(sample):
    return hashlib.md5(
        json.dumps(sample["requested_rewrite"]).encode()
    ).hexdigest()
