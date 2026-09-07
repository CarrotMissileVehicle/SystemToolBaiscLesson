import json
import subprocess

proc = subprocess.Popen(
    ["/home/joe/lab/venv/bin/pylsp"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)


def send(msg):
    body = json.dumps(msg).encode("utf-8")
    header = f"Content-Length: {len(body)}\r\n\r\n".encode("ascii")
    proc.stdin.write(header + body)
    proc.stdin.flush()


def read_frame():
    headers = {}
    line = proc.stdout.readline()
    while line != b"\r\n":
        if line.startswith(b"Content-Length:"):
            headers["len"] = int(line.split(b":")[1].strip())
        line = proc.stdout.readline()
    return json.loads(proc.stdout.read(headers["len"]))


def read_until_id():
    while True:
        headers = {}
        line = proc.stdout.readline()
        while line != b"\r\n":
            if line.startswith(b"Content-Length:"):
                headers["len"] = int(line.split(b":")[1].strip())
            line = proc.stdout.readline()
        msg = json.loads(proc.stdout.read(headers["len"]))
        if "id" in msg:
            return msg


send({"jsonrpc": "2.0", "id": 1, "method": "initialize",
      "params": {"processId": None, "rootUri": "file:///home/joe/lab/practice3",
                 "capabilities": {}}})
init = read_until_id()
print("INIT ok, server:", init["result"]["serverInfo"])

send({"jsonrpc": "2.0", "method": "initialized", "params": {}})

uri = "file:///home/joe/lab/practice3/main.py"
text = open("/home/joe/lab/practice3/main.py").read()
send({"jsonrpc": "2.0", "method": "textDocument/didOpen",
      "params": {"textDocument": {"uri": uri, "languageId": "python",
                                  "version": 1, "text": text}}})


def definition(line, char):
    send({"jsonrpc": "2.0", "id": f"def-{line}-{char}",
          "method": "textDocument/definition",
          "params": {"textDocument": {"uri": uri},
                     "position": {"line": line, "character": char}}})
    return read_until_id()


def references(line, char):
    send({"jsonrpc": "2.0", "id": "refs",
          "method": "textDocument/references",
          "params": {"textDocument": {"uri": uri},
                     "position": {"line": line, "character": char},
                     "context": {"includeDeclaration": True}}})
    return read_until_id()


r = definition(4, 6)
print("=== goto definition: calc() ===")
for loc in r["result"]:
    print(loc["uri"].replace("file://", ""), "line", loc["range"]["start"]["line"] + 1)

r = definition(6, 19)
print("=== goto definition: torch.nn.Linear (library) ===")
for loc in r["result"]:
    print(loc["uri"].replace("file://", ""), "line", loc["range"]["start"]["line"] + 1)

r = references(4, 6)
print("=== find references: calc (main.py + utils.py only) ===")
for loc in r["result"]:
    p = loc["uri"].replace("file://", "")
    if p.startswith("/home/joe/lab/practice3"):
        line = loc["range"]["start"]["line"] + 1
        print(p.split("practice3/")[1], "line", line)

proc.terminate()