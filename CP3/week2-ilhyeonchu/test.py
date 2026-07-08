import os, subprocess

files = {
    '1-1': [''],
    '1-2': [''],
    '1-3': [''],
    '2-1': [''],
    '2-2': [''],
    '2-3': [''],
    '2-4': [''],
    '3-1': [''],
    '3-2': [''],
    '3-3': [''],
    '3-4': [''],
    '4-1': [0,1,2,3],
    '4-2': [''],
    '4-3': [0,1,2,3],
}

path_code = 'code'
path_testset = 'testset'
CC = 'gcc'

for file, testset in files.items():
    try:
        os.system(f'{CC} {path_code}/{file}.c -o {path_code}/{file}.exe')
    except:
        pass
    
    for test in testset:
        test_in = ''
        try:
            with open(f'{path_testset}/{file}-in{test}.txt') as f:
                test_in = f.read()
        except:
            pass
        
        try:
            result = subprocess.run(
                [f'{path_code}/{file}'],
                input=test_in,
                capture_output=True,
                text=True
            )
        except:
            print(f'{file}-out{test}.txt FAIL')
            continue

        test_out = ''
        try:
            with open(f'{path_testset}/{file}-out{test}.txt') as f:
                test_out = f.read()
        except:
            pass

        if test_out == result.stdout:
            print(f'{file}-out{test}.txt PASS')
        else:
            print(f'{file}-out{test}.txt FAIL')