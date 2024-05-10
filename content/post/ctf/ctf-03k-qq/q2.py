import zipfile

z = zipfile.ZipFile('what.zip')
for x in range(1000000):
    x = f'{x:06d}'
    try:
        z.extractall(pwd=x.encode())
    except Exception:
        continue
    print(x)
    break
else:
    raise RuntimeError
