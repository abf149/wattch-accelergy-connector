gem5_class = "DerivO3CPU"
accelergy_class = "cpu_regfile"
path = "system.chip.cpu"
name_append = "regfile_fp"

criteria = True

constants = [("type", "fp")]

attributes = [
    ("phys_size", "numPhysFloatRegs"),
    ("issue_width", "issueWidth")
]

actions = [
    ("read", ["fp_regfile_reads"]),
    ("write", ["fp_regfile_writes"])
]
