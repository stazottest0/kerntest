import os 

def ghSet(varName, content):
    varName = f"GITHUB_{varName}"
    print(f"[+] Writing {json.dumps(content)} to ${varName}")
    if varName in os.environ:
        with open(os.environ[varName], 'at') as f: f.write(content + "\n")

ghSet("OUTPUT", f"targets=targets_test")
ghSet("OUTPUT", f"submission_dir=submission_dir_test")
ghSet("OUTPUT", f"exploits_info=exploits_info_test")
ghSet("OUTPUT", f"artifact_backup_dir=artifact_backup_dir_test")
