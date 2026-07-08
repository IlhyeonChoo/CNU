import os, sys
REPOSITORY_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(REPOSITORY_ROOT_DIR, "src"))

from question_18 import parse_log, create_logs

def test():
    log_lines = ["2025-05-02 13:00:00 [INFO] User logged in",\
                "2025-05-02 14:00:00 [INFO] User Buy a",\
                "2025-05-02 15:00:00 [INFO] User logged b"]
    
    out = create_logs(log_lines)
    assert 'a' in out[1].message
    assert 'b' in out[2].message