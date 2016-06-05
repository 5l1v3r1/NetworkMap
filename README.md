Post-exploitation network mapping
=================================

The purpose of this tool is to produce a network diagram by collating network information gathered on remote hosts.

Example:

 * Compromise host A
 * Dump the routing table, ARP table
 * Feed the dumps into this tool
 * Pivot on host B
 * Dump tables
 * Feed tables
 * ...rinse, repeat

 * Ultimately, this tool produces a network diagram showing all hosts reachable
   from A and B. Ideally with pretty icons


Usage
-----

This command draws a simple graph from a windows ARP file dump:

    python src/netgrapher.py samples/arp/windows_7_arp.txt  -t arp -o windows --force

It's work in progress so you have to specify type and OS for now.


Possible alternatives
---------------------

P2NMAP (it's a book, comes with source code): https://python-forensics.org/p2nmap/

Design blurb
------------

 1. Write a python parsing tool able to digest windows route dumps, linux route dumps, etc.
    * Must be able to recognise dupes, specify nearest-neighbours
    * CIDRize to parse IPs? https://pypi.python.org/pypi/cidrize/
    * *persistence!* the tool should use an existing database (SQLite?) for
      storage, with options to recreate
 2. Use a graph library to set up the data structure. Candidates:
    * igraph http://igraph.org/python/
    * networkX https://networkx.readthedocs.io/en/stable/index.html
    * graphviz (pydot or python's graphviz module): http://graphviz.readthedocs.io/en/latest/
    * graph-tool: https://graph-tool.skewed.de/
    * pygraphviz (seems related to networkX - no clean install?)
 3. Dump into SVG
 4. ...
 5. Profit!

Keep in mind:

 * ARP tables show nearest hosts
 * Routing tables show static routes, default routes
 * SNMP can provide info from switches?
 * Traceroute is useful to see hops; but if they are blocked or ICMP restricted, maybe low-level TCP CONNECT and measure decrease in packet TTL? Do a reverse tcpdump from a remote host?

Future:

 * Dump into Excel spreadsheet or SQL database
 * Import into Microsoft Visio? https://support.office.com/en-gb/article/Create-a-detailed-network-diagram-by-using-external-data-in-Visio-Professional-1d43d1a0-e1ac-42bf-ad32-be436411dc08#bm2


Interesting to look at:

 * Graphviz can also do clustering? http://www.graphviz.org/Gallery/undirected/gd_1994_2007.html
 * Graphviz and network maps (icons are a bit ugly tho): http://www.graphviz.org/Gallery/undirected/networkmap_twopi.html
 * For manual graphs (meh) - requires probably generating an output properly formatted like XML. Pain to maintain: https://community.spiceworks.com/topic/521280-i-need-software-that-make-my-whole-network-diagram-automatically
