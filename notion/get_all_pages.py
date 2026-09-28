from notion.client import notion


def get_all_pages(data_source_id):
    pages = []
    cursor = None

    while True:
        if cursor:
            response = notion.data_sources.query(
                data_source_id=data_source_id,
                start_cursor=cursor
            )
        else:
            response = notion.data_sources.query(
                data_source_id=data_source_id
            )

        pages.extend(response["results"])

        if not response["has_more"]:
            break

        cursor = response["next_cursor"]

    return pages
