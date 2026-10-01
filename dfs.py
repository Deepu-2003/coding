folders = {
    "Main": ["photos", "docs"],
    "photos": ["2025", "2026"],
    "docs": ["projects", "personal"],
    "2025": [],
    "2026": [],
    "projects": ["gen-ai", "vision-ai"],
    "personal": [],
    "gen-ai": [],
    "vision-ai": []
}


def explore(folder, level=0):
    print(" " * level + folder)
    for subfolder in folders[folder]:
        explore(subfolder, level + 1)


explore("Main")