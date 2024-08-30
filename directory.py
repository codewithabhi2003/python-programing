bsc_it = {
    "fyit": {
        "sem1": {
            "sub1": "dbms",
            "sub2": "cpp",
            "sub3": "greenit"
        },
        "sem2": {
            "sub1": "history",
            "sub2": "hindi",
            "sub3": "english"
        }
    },
    "syit": {
        "sem3": {
            "sub1": "python",
            "sub2": "ds",
            "sub3": "maths"
        },
        "sem4": {
            "sub1": "hap",
            "sub2": "cognosy",
            "sub3": "bio"
        }
    },
    "tyit": {
        "sem5": {
            "sub1": "cn",
            "sub2": "os",
            "sub3": "java"
        },
        "sem6": {
            "sub1": "physics",
            "sub2": "chemistry",
            "sub3": "electronics"
        }
    }
}

bsc_it["fyit"]["sem1"]["sub1"] = "hap"
del bsc_it["fyit"]["sem1"]

print(bsc_it)
