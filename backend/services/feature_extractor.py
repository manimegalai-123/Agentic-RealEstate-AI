from collections import Counter


def extract_features(labels):

    c = Counter(labels)

    features = {
        "bathroom": c["bathroom"],
        "bedroom": c["bedroom"],
        "dining": c["dining"],
        "gaming": c["gaming"],
        "kitchen": c["kitchen"],
        "laundry": c["laundry"],
        "living": c["living"],
        "office": c["office"],
        "terrace": c["terrace"],
        "yard": c["yard"]
    }

    return features