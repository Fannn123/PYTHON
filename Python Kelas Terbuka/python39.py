buah = {
    'manggo' : 'mangga',
    'orange' : 'jeruk',
    'apple'  : 'apel',
    'banana' : 'pisang'
}

buah_buahan = buah.copy()

print(f"data normal: {buah}")
print(f"data copy: {buah_buahan}")

buah['manggo'] = 'jackfruit'
print(f"data normal: {buah}")
print(f"data copy: {buah_buahan}")

#pop dictionary
apple = buah.pop('apple')
print(f"data normal: {apple}")
print(f"data copy: {buah_buahan}")

#popitem dictionary
banana = buah.popitem()
print(f"data normal: {banana}")
print(f"data copy: {buah_buahan}")