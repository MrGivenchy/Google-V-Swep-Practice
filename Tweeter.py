import heapq
from collections import deque


class Post:
    def __init__(self, post: str, date: int, likes: int, dislikes: int, replies=None):
        self.post = post
        self.date = date
        self.likes = likes
        self.dislikes = dislikes
        self.replies = replies if replies is not None else []


def PopularPost(date: int, posts: list[Post]) -> list[Post]:
    maxHeap = []

    for post in posts:
        if date == post.date:
            popularity = post.likes - post.dislikes
            heapq.heappush(maxHeap, (popularity * -1, post.post, post))

    result = []

    for i in range(len(maxHeap)):
        popularity, title, post = heapq.heappop(maxHeap)
        result.append(post)

    return result


def engagement(post: Post) -> int:
    if post == "":
        return 0

    queue = deque([post])
    count = 0

    while queue:
        curr = queue.popleft()

        count += len(curr.replies)

        for reply in curr.replies:
            queue.append(reply)

    return count



reply1 = Post("no way, it's sausage", 1, 5, 1)
reply2 = Post("i like cheese", 1, 3, 0)
reply3 = Post("you are a bad person", 1, 2, 5)

pepperoni = Post("pepperoni", 1, 10, 2, [reply1, reply2])
pineapple = Post("pineapple", 1, 7, 10, [reply3])

main_post = Post("what's the best pizza?", 1, 20, 3, [pepperoni, pineapple])

post2 = Post("Python is fun", 1, 15, 1)
post3 = Post("Java is better", 1, 8, 5)
post4 = Post("Old post", 2, 100, 1)

posts = [main_post, post2, post3, post4]


print("Popular posts on date 1:")
print(PopularPost(1, posts))



print("Engagement of pepperoni:")
print(engagement(pepperoni))
# Expected: 2


print("Engagement of pineapple:")
print(engagement(pineapple))



print("Engagement of main post:")
print(engagement(main_post))
