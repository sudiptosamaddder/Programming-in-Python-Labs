resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    if len(resources) == 0:
        print("No resources available")
        return

    for r in resources:
        print(r)



def search_by_category(resources, category):
    for r in resources:
        if r[2].lower() == category.lower():
            print(r)



def find_unavailable(resources):
    for r in resources:
        if r[3] == 0:
            print(r[1], "is unavailable")


display_resources(resources)

print("\nElectronics:")
search_by_category(resources, "Electronics")

print("\nUnavailable:")
find_unavailable(resources)