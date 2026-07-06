import socket
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

DEFAULT_IP = "192.168.137.250"
DEFAULT_PORT = 9021
BASE_DIR = Path(__file__).resolve().parent.parent
PAYLOAD_DIR = BASE_DIR / "payloads"

def send_file(path: Path):
    ip = ip_var.get().strip()
    try:
        port = int(port_var.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Port must be a number")
        return

    if not path.exists():
        messagebox.showerror("Missing ELF", f"File not found:\n{path}")
        return

    try:
        data = path.read_bytes()
        with socket.create_connection((ip, port), timeout=8) as s:
            s.sendall(data)
        status_var.set(f"Sent {path.name} ({len(data)} bytes) -> {ip}:{port}")
    except Exception as e:
        status_var.set("Failed")
        messagebox.showerror("Send failed", str(e))

def send_named(name: str):
    send_file(PAYLOAD_DIR / name)

def browse_send():
    f = filedialog.askopenfilename(title="Select ELF payload", filetypes=[("ELF payload", "*.elf"), ("All files", "*.*")])
    if f:
        send_file(Path(f))

root = tk.Tk()
root.title("PS5 Power ELF Sender 9021")
root.geometry("460x250")
root.resizable(False, False)

ip_var = tk.StringVar(value=DEFAULT_IP)
port_var = tk.StringVar(value=str(DEFAULT_PORT))
status_var = tk.StringVar(value="Ready")

tk.Label(root, text="PS5 IP:").pack(anchor="w", padx=12, pady=(12,0))
tk.Entry(root, textvariable=ip_var).pack(fill="x", padx=12)

tk.Label(root, text="Port:").pack(anchor="w", padx=12, pady=(8,0))
tk.Entry(root, textvariable=port_var).pack(fill="x", padx=12)

frame = tk.Frame(root)
frame.pack(fill="x", padx=12, pady=14)

tk.Button(frame, text="Restart\nreboot.elf", command=lambda: send_named("reboot.elf"), height=3).pack(side="left", expand=True, fill="x", padx=3)
tk.Button(frame, text="Rest Mode\nsuspend.elf", command=lambda: send_named("suspend.elf"), height=3).pack(side="left", expand=True, fill="x", padx=3)
tk.Button(frame, text="Turn Off\npoweroff.elf", command=lambda: send_named("poweroff.elf"), height=3).pack(side="left", expand=True, fill="x", padx=3)

tk.Button(root, text="Browse and Send ELF", command=browse_send).pack(fill="x", padx=12, pady=4)
tk.Label(root, textvariable=status_var, fg="blue").pack(anchor="w", padx=12, pady=(8,0))

root.mainloop()
