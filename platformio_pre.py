import os
os.environ["IDF_COMPONENT_MANAGER"] = "0"

from scripts.dump_html import dump

dump(
    file_from="./main/packet_forwarder/webpage.html",
    file_to="./main/packet_forwarder/webpage.h",
    var_name="webpage_str",
)
