from notion.client import notion

def get_all_pages(database_id):
    pages = []
    cursor = None

    while True:
        if cursor:
            response = notion.databases.query(
                database_id=database_id,
                start_cursor=cursor
            )
        else:
            response = notion.databases.query(
                database_id=database_id
            )

        pages.extend(response["results"])

        if not response["has_more"]:
            break

        cursor = response["next_cursor"]

    return pages
