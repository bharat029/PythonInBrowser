from browser import document

def print(s):
    document['display'] <= s

def run(s):
    s.preventDefault()
    try:
        exec(document['python'].value)
    except Exception as e:
        print(f'{e}')

document['form'].bind('submit', run)