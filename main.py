from browser import document

def print(s):
    document['display'] <= s

def run(s):
    s.preventDefault()
    exec(document['python'].value)

document['form'].bind('submit', run)