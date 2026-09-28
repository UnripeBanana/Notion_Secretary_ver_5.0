def rich_text(value):
    return {
        "rich_text": [
            {
                "type": "text",
                "text": {
                    "content": "" if value is None else str(value)
                }
            }
        ]
    }
