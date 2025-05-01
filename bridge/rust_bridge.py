import os
import platform
import ctypes
from cffi import FFI

ffi = FFI()

system = platform.system()
lib_name = {
    "Darwin": "librust.dylib",
    "Linux": "librust.so",
    "Windows": "rust.dll", 
}[system]

lib_path = os.path.join("rust", "target", "release", lib_name)

print(f"[RustBridge] Library path: {lib_path}")

if not os.path.isfile(lib_path):
    print(f"[RustBridge] ERROR: Library not found at {lib_path}")
else:
    print(f"[RustBridge] Library exists, attempting to load...")

if system == "Windows":
    dll_dir = os.path.abspath(os.path.dirname(lib_path))
    os.add_dll_directory(dll_dir)

try:
    print("[RustBridge] Attempting to load the Rust library with ctypes...")
    lib = ctypes.CDLL(lib_path)
    print("[RustBridge] DLL loaded successfully with ctypes.")

    lib.greet.argtypes = [ctypes.c_char_p]
    lib.greet.restype = ctypes.c_char_p

    def get_welcome_message(name: str) -> str:
        c_name = ctypes.c_char_p(name.encode("utf-8"))
        result_ptr = lib.greet(c_name)
        return result_ptr.decode("utf-8")

except OSError as e:
    print(f"[RustBridge] ERROR: Failed to load library with ctypes. {e}")
    print("[RustBridge] Using fallback Python implementation.")

    def get_welcome_message(name: str) -> str:
        return f"rust error {name}"
