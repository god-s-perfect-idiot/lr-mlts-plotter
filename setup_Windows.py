import cx_Freeze
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("LR=mLTS-plotter.py", base=base, icon="gui.png")]

cx_Freeze.setup(
    name = "PowerSIM-GUI",
    options = {"build_exe":{"packages":["tkinter","PIL"], "include_files":["","asm_dir.py","assembler.py","first_pass.py","gui.py","input.s","main.py","memory_manage.py","processor.py","second_pass.py","simple.s"]}},
    version = "0.65",
    description = "POWER ISA simulator",
    executables = executables
)
