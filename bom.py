import json
import sys

libraries = sys.stdin.read()
obj = json.loads(libraries)

out_list = []
blacklist = ["AGPL"]
greylist = ["LGPL"]


# TODO: configure the bom scan differently

for lib in obj:
    for blacklist_item in blacklist:
        if blacklist_item in lib["License"]:
            print("Blacklisted license found: ", lib["License"])
            sys.exit(1)

    for greylist_item in greylist:
        if greylist_item in lib["License"]:
            print(
                "Limited approved OSS License found, you might want to check this:",
                lib["License"],
            )

    lib["Integration Mechanism"] = "linked dynamically"
    lib["Usage Scenario"] = "as-is"
    lib["Disribution"] = "yes"
    lib[
        "Fulfillment of OSS license obligations"
    ] = "license, copyright attribution and source code provided with Python package"
    out_list.append(lib)


with open("billofmaterial.json", "w") as f:
    json.dump(out_list, f)
