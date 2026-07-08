import os
import subprocess
import glob

def main():
    for folder_name in os.listdir('code'):
        code_dir = os.path.join("code", folder_name)
        out_file = os.path.join("testset", f"{folder_name}-out.txt")
        error_file = os.path.join("testset", f"{folder_name}-error.txt")
        exe_path = os.path.join(".", "output.exe")  
        
        c_files = glob.glob(os.path.join(code_dir, "*.c"))
        if not c_files:
            continue

        
        compile_result = subprocess.run(
            ["gcc"] + c_files + ["-o", exe_path],
            capture_output=True,
            text=True
        )

        if os.path.exists(error_file):
            with open(error_file, "r", encoding="utf-8") as f:
                expected_error = f.read()

            actual_error = compile_result.stderr

            if actual_error.strip() == expected_error.strip():
                print(f"[PASS] {folder_name}")
            else:
                print(f"[FAIL] {folder_name}")
                print("=== expected ===")
                print(expected_error)
                print("=== got ===")
                print(actual_error)
            continue
        elif compile_result.returncode != 0:
            print(f"[FAIL] {folder_name}")
            print(compile_result.stderr)
            continue
        
        run_result = subprocess.run(
            [exe_path],
            capture_output=True,
            text=True
        )
        actual_output = run_result.stdout

        if os.path.exists(out_file):
            with open(out_file, "r", encoding="utf-8") as f:
                expected_output = f.read()

        if actual_output.strip() == expected_output.strip():
            print(f"[PASS] {folder_name}")
        else:
            print(f"[FAIL] {folder_name}")
            print("=== expected ===")
            print(expected_output)
            print("=== got ===")
            print(actual_output)

        if os.path.exists(exe_path):
            os.remove(exe_path)

if __name__ == "__main__":
    main()