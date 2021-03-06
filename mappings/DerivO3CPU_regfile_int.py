gem5_class = "DerivO3CPU"
accelergy_class = "cpu_regfile"
path = "system.chip.cpu"
name_append = "regfile_int"

criteria = True

constants = [("type", "int")]

attributes = [
    ("phys_size", "numPhysIntRegs"),
    ("issue_width", "issueWidth")
]

actions = [
    ("read", ["int_regfile_reads"]),
    ("write", ["int_regfile_writes"])
]
