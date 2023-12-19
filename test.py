# from Yara.MalwareSig import *

# mal_file_loc = 'Yara/malware_files'
# rule_file_loc = 'Yara/rules'
# yara_scanner = YaraScanner(rule_file_loc, mal_file_loc)
# yara_rule_dict = yara_scanner.make_dict()
# hit_files = yara_scanner.scan_files(yara_rule_dict)

# print(hit_files)


import os

def file_extractor(path):

    files = []
    for _, folders, filenames in os.walk(path):
        files += filenames

    return files

print(file_extractor('Yara'))