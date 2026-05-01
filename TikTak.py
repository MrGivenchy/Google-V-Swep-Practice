from typing import List

class Video:
    def __init__(self, uniqueID: int, viewCount: int):
        self.uniqueId = uniqueID
        self.views = viewCount

class User:
    def __init__(self, uniqueHandle: str, viewedVids: List[Video], likedVids: List[Video]):
        self.Handle = uniqueHandle
        self.viewedVids = viewedVids
        self.likedVids = likedVids


def unseenVids(userA: User, userB: User):
    unseenVideos = []

    for video in userA.likedVids:
        if video not in userB.viewedVids:
            unseenVideos.append(video)

    return unseenVideos


def inCommon(user1: User, userCollection: List[User]):
    maxCount = 0
    userInCommon = ""

    for user in userCollection:
        count = 0

        for i in user1.likedVids:
            if i in user.likedVids:
                count += 1

        if maxCount < count:
            maxCount = count
            userInCommon = user

    return userInCommon


def recommendVideos(userX: User, userCollection: List[User]):
    similarUsers = []

    for user in userCollection:
        if user == userX:
            continue

        count = 0
        for vid in userX.likedVids:
            if vid in user.likedVids:
                count += 1

        similarUsers.append((user, count))

    similarUsers.sort(key=lambda x: x[1], reverse=True)
    topUsers = [user for user, count in similarUsers[:5]]

    recommendations = {}

    for user in topUsers:
        for vid in user.likedVids:
            if vid not in userX.viewedVids:
                if vid not in recommendations:
                    recommendations[vid] = 0
                recommendations[vid] += 1

    sortedVids = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

    return [vid for vid, count in sortedVids]


# ---------------- TEST CASES ----------------

v1 = Video(1, 100)
v2 = Video(2, 200)
v3 = Video(3, 300)
v4 = Video(4, 400)
v5 = Video(5, 500)
v6 = Video(6, 600)

alice = User("@alice", [v1, v2], [v1, v2, v3])
reuben = User("@reuben", [v1], [v1, v2, v5, v6])
tife = User("@tife", [v3], [v3, v4, v5])
bob = User("@bob", [v2], [v2, v3, v6])

users = [reuben, tife, bob]

print("Unseen videos:")
for video in unseenVids(reuben, alice):
    print(video.uniqueId)

print("Most in common:")
print(inCommon(alice, users).Handle)

print("Recommended videos:")
for video in recommendVideos(alice, users):
    print(video.uniqueId)