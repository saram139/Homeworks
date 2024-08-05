def single_root_words(root_world, *other_worlds):
    same_worlds = []
    for i in other_worlds:
        if root_world.lower() in i.lower() or i.lower() in root_world.lower():
            same_worlds.append(i)
    return same_worlds


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
