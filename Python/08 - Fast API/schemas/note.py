def note_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"]
    }


def note_entities(data) -> list:
    return [note_entity(item) for item in data]
