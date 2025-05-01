use std::ffi::{CStr, CString};
use std::os::raw::c_char;

#[no_mangle]
pub extern "C" fn greet(ptr: *const c_char) -> *mut c_char {
    let c_str = unsafe { CStr::from_ptr(ptr) };
    let name = c_str.to_str().unwrap_or("Guest");
    let message = format!("Welcome from lib.rs! {}", name);
    CString::new(message).unwrap().into_raw()
}
