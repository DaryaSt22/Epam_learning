# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import xml.etree.ElementTree as ET
import json as json_module
import html


class UnhandledException(Exception):
    pass


def rss_parser(
        xml: str,
        limit: Optional[int] = None,
        json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """
    # Your code goes here

    root = ET.fromstring(xml)
    channel = root.find("channel")

    title = channel.findtext("title")
    link = channel.findtext("link")
    description = channel.findtext("description")
    lastBuildDate = channel.findtext("lastBuildDate")
    pubDate = channel.findtext("pubDate")
    language = channel.findtext("language")
    managinEditor = channel.findtext("managingEditor")

    categories = []

    # all_p_tags = channel.findall("category")

    # for tag in all_p_tags:
    #     all_tag = tag.text
    #
    #     if all_tag:
    #         categories.append(all_tag)

    for tag in channel.findall("category"):
        category_text = tag.text
        if category_text:
            categories.append(html.unescape(category_text))

    all_items = channel.findall("item")

    items = []

    for item_one in all_items:
        item_categories = []
        item_category_tags = item_one.findall("category")

        for category_tag in item_category_tags:
            item_categories.append(category_tag.text)

        item_title = item_one.findtext("title")
        item_author = item_one.findtext("author")
        item_pub_date = item_one.findtext("pubDate")
        item_link = item_one.findtext("link")
        item_description = item_one.findtext("description")

        # one_item = {
        #     "title": item_title,
        #     "author": item_author,
        #     "pubDate": item_pub_date,
        #     "link": item_link,
        #     "category": item_categories,
        #     "description": item_description,
        # }

    one_item = {
        "title": item_one.findtext("title"),
        "author": item_one.findtext("author"),
        "pubDate": item_one.findtext("pubDate"),
        "link": item_one.findtext("link"),
        "category": item_categories,
        "description": item_one.findtext("description"),
    }

    items.append(one_item)

    if limit is not None:
        items = items[:limit]

    if json:
        json_dict = {}

        if title:
            json_dict["title"] = html.unescape(title)
        if link:
            json_dict["link"] = html.unescape(link)
        if lastBuildDate:
            json_dict["lastBuildDate"] = html.unescape(lastBuildDate)
        if pubDate:
            json_dict["pubDate"] = html.unescape(pubDate)
        if language:
            json_dict["language"] = html.unescape(language)
        if categories:
            json_dict["category"] = categories
        if managinEditor:
            json_dict["managingEditor"] = html.unescape(managinEditor)
        if description:
            json_dict["description"] = html.unescape(description)

    json_items = []

    for item in items:
        json_item = {}

        if item["title"]:
            json_item["title"] = html.unescape(item["title"])
        if item["author"]:
            json_item["author"] = html.unescape(item["author"])
        if item["pubDate"]:
            json_item["pubDate"] = html.unescape(item["pubDate"])
        if item["link"]:
            json_item["link"] = html.unescape(item["link"])
        if item["category"]:
            json_item["category"] = item["category"]
        if item["description"]:
            json_item["description"] = html.unescape(item["description"])

        json_items.append(json_item)

    if json_items:
        json_dict["items"] = json_items

        json_string = json_module.dumps(
            json_dict,
            indent=2,
            ensure_ascii=False,
    )

        return [json_string]

    result = []

    # if title:
    #     result.append(f"Feed: {title}")
    # if link:
    #     result.append(f"Link: {link}")
    # if lastBuildDate:
    #     result.append(f"Last Build Date: {lastBuildDate}")
    # if pubDate:
    #     result.append(f"Publish Date: {pubDate}")
    # if language:
    #     result.append(f"Language: {language}")
    # if categories:
    #     result.append(f"Categories: {', '.join(categories)}")
    # if managinEditor:
    #     result.append(f"Editor: {managinEditor}")
    # if description:
    #     result.append(f"Description: {description}")

    if title:
        result.append(f"Feed: {html.unescape(title)}")
    if link:
        result.append(f"Link: {html.unescape(link)}")
    if lastBuildDate:
        result.append(f"Last Build Date: {html.unescape(lastBuildDate)}")
    if pubDate:
        result.append(f"Publish Date: {html.unescape(pubDate)}")
    if language:
        result.append(f"Language: {html.unescape(language)}")
    if categories:
        result.append(f"Categories: {', '.join(categories)}")
    if managinEditor:
        result.append(f"Editor: {html.unescape(managinEditor)}")
    if description:
        result.append(f"Description: {html.unescape(description)}")

    if items:
        result.append("")

    for index, item in enumerate(items):
        if index > 0:
            result.append("")

    # for item in items:
    #     if item:
    #         result.append("")
    #     if item["title"]:
    #         result.append(f"Title: {item['title']}")
    #     if item["author"]:
    #         result.append(f"Author: {item['author']}")
    #     if item["pubDate"]:
    #         result.append(f"Published: {item['pubDate']}")
    #     if item["link"]:
    #         result.append(f"Link: {item['link']}")
    #     if item["category"]:
    #         result.append(f"Categories: {', '.join(item['category'])}")
    #
    #     result.append(item["description"] or "")

    # json_dict = {}
    #
    # if json:
    #     json_string = json_module.dumps(json_dict)
    #     return [json_string]
    # else:
    #     return result

    if item["title"]:
        result.append(f"Title: {html.unescape(item['title'])}")
    if item["author"]:
        result.append(f"Author: {html.unescape(item['author'])}")
    if item["pubDate"]:
        result.append(f"Published: {html.unescape(item['pubDate'])}")
    if item["link"]:
        result.append(f"Link: {html.unescape(item['link'])}")
    if item["category"]:
        result.append(f"Categories: {', '.join(item['category'])}")

    if item["description"]:
        result.append("")
        result.append(html.unescape(item["description"]))

    return result


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
