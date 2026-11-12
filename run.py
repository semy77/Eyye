#!/usr/bin/env python
"""Small Termux launcher for the compiled Guildglory modules."""
import hashlib
import importlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
EXPECTED = {
    'MajorloginReqBuild_pb2.cpython-313-aarch64-linux-android.so': '1a47dc09d461dbe934917980e087c1dcee22b37b0f9912ba25cbbb1af05d92be',
    'MajorloginResp_pb2.cpython-313-aarch64-linux-android.so': '69b2dcecaa10a0521edf44ddd421b5a92d5905cc917e08cff5c41d8c8cbae88d',
    'PorTs_pb2.cpython-313-aarch64-linux-android.so': '10e2f9507097fe73d38627067b904e7beac5a47d470a00beff27eb42aea804b8',
    'core.cpython-313-aarch64-linux-android.so': '0e3f58de2ed296b0ec00d43436d5cf1dfcc29eb37ca4a202b2251fb90e91b316',
    'guest.cpython-313-aarch64-linux-android.so': '4377b1c26b5b8325c3f086b3f13fd4a2b60d70a3f5baa9726a2850203d9fa888',
    'main.cpython-313-aarch64-linux-android.so': '0a5f22cea23234d876cf30a65bf5656abad59501904c38477e8435b72a62962e',
    'match.cpython-313-aarch64-linux-android.so': 'cb7be8104473284885f76b2f04d10cb600539c0ae0802d631f170044e73e1889',
}
for filename, expected in EXPECTED.items():
    path = ROOT / filename
    if not path.is_file():
        print('[SECURITY] Required compiled module missing:', filename)
        raise SystemExit(2)
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        print('[SECURITY] Compiled module was modified:', filename)
        raise SystemExit(3)

sys.path.insert(0, str(ROOT))
try:
    app = importlib.import_module('main')
    app.main_menu()
except KeyboardInterrupt:
    print('\nInterrupted')
