import heapq


class webpage:
    def __init__(self, url: str, title: str, body: str, headings: list[str], links: list[str]):
        self.url = url
        self.title = title
        self.body = body
        self.headings = headings
        self.links = links

    def __repr__(self):
        return self.url


def search(keywords: list[str], pages: list[webpage]) -> list[webpage]:
    search_result = []  # max heap using negative numbers
    added_pages = set()

    for page in pages:
        title = page.title.lower()
        body = page.body.lower()

        headings_text = ""
        for heading in page.headings:
            headings_text += heading.lower() + " "

        best_score = 0

        for keyword in keywords:
            keyword = keyword.lower()

            if keyword in title:
                best_score = max(best_score, 3)
            elif keyword in headings_text:
                best_score = max(best_score, 2)
            elif keyword in body:
                best_score = max(best_score, 1)

        if best_score > 0 and page.url not in added_pages:
            heapq.heappush(search_result, (-best_score, page.url, page))
            added_pages.add(page.url)

    result = []

    while len(search_result) > 0:
        score, url, page = heapq.heappop(search_result)
        result.append(page)

    return result


def verify(keywords: list[str], pages: list[webpage]) -> list[webpage]:
    result = []  # max heap using negative numbers
    search_result = search(keywords, pages)

    for page in search_result:
        count = 0

        for other_page in search_result:
            if page.url in other_page.links:
                count += 1

        heapq.heappush(result, (count * -1, page.url, page))

    result2 = []

    while len(result) > 0:
        count, url, page = heapq.heappop(result)
        result2.append(page)

    return result2


def page_rank(pages: list[webpage], rounds: int = 10) -> list[webpage]:
    ranks = {}

    # Give every page a starting score
    for page in pages:
        ranks[page.url] = 1

    # Repeat the rank updates
    for i in range(rounds):
        new_ranks = {}

        # Reset scores each round
        for page in pages:
            new_ranks[page.url] = 0

        for page in pages:
            # Skip pages with no links
            if len(page.links) == 0:
                continue

            # Split score between links
            amount_to_give = ranks[page.url] / len(page.links)

            # Give score to linked pages
            for link in page.links:
                if link in new_ranks:
                    new_ranks[link] += amount_to_give

        # Save updated scores
        ranks = new_ranks

    result = []  # max heap using negative numbers

    # Put pages into heap by rank
    for page in pages:
        heapq.heappush(result, (ranks[page.url] * -1, page.url, page))

    ranked_pages = []

    # Pull highest ranked pages first
    while len(result) > 0:
        rank, url, page = heapq.heappop(result)
        ranked_pages.append(page)

    return ranked_pages


#Test cases

a = webpage(
    "a",
    "White shirt store",
    "We sell clothes",
    [],
    ["b", "c"]
)

b = webpage(
    "b",
    "Bad title",
    "This page talks about a white shirt",
    [],
    ["a", "c"]
)

c = webpage(
    "c",
    "Bad title",
    "Random body",
    ["How to wash a white shirt"],
    ["a"]
)

d = webpage(
    "d",
    "Bad title",
    "This is about a white shirt",
    [],
    ["a"]
)

e = webpage(
    "e",
    "Cool cars",
    "Nothing about clothes",
    [],
    []
)

pages = [a, b, c, d, e]
keywords = ["white", "shirt"]


print("Part 2 search result:")
print(search(keywords, pages))
# Expected idea: [a, c, b, d]


print("Part 3 link count ranking:")
print(verify(keywords, pages))
# Expected idea: [a, c, b, d]


print("Simplified PageRank result:")
print(page_rank([a, b, c, d]))
# Expected idea: a should be near the top