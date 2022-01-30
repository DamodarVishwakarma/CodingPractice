def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(f"kwargs function has {key} {value}")


normal = "this is a normal argument in the function"
args = "damodar", "is", "my", "name", "from", "banda"
kwargs = {"name": "damodar", "sirname": "vishwakarma"}
funargs(normal, args, kwargs)
