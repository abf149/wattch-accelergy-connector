gem5_class = "Cache"
accelergy_class = "cache"
path = "system.chip"
name_append = ""

def criteria(params):
    return params["name"] == "dcache"

constants = [
    ("cache_type", "dcache"),
    ("n_rd_ports", 1),
    ("n_wr_ports", 1),
    ("n_rdwr_ports", 1),
    ("n_banks", 1),
    ("block_size", 32)
]

attributes = [
    ("size", "size"),
    ("associativity", "assoc"),
    ("data_latency", "response_latency"),
    ("mshr_size", "mshrs"),
    ("tag_size", "tags.entry_size"),
    ("write_buffer_size", "write_buffers"),
]

actions = [
    ("read_hit", ["ReadReq_hits::total"]),
    ("read_miss", ["ReadReq_misses::total"]),
    ("write_hit", ["WriteReq_hits::total"]),
    ("write_miss", ["WriteReq_misses::total"]),
]
