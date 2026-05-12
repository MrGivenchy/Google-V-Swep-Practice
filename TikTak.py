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
    similarUsers = []  # will store (user, similarity score)

    for user in userCollection:  # loop through all users
        if user == userX:  # skip the same user
            continue

        count = 0  # number of common liked videos
        for vid in userX.likedVids:  # check each video userX liked
            if vid in user.likedVids:  # if the other user also liked it
                count += 1  # increase similarity score

        similarUsers.append((user, count))  # store user and their score

    similarUsers.sort(key=lambda x: x[1], reverse=True)  
    # sort users by similarity score (highest first)

    topUsers = [user for user, count in similarUsers[:5]]  
    # take top 5 most similar users

    recommendations = {}  
    # dictionary to count how many similar users liked each video

    for user in topUsers:  # go through each similar user
        for vid in user.likedVids:  # check videos they liked
            if vid not in userX.viewedVids:  # only if userX hasn’t seen it
                if vid not in recommendations:  # if not already tracked
                    recommendations[vid] = 0  # start count at 0
                recommendations[vid] += 1  # increase popularity count

    sortedVids = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)  
    # sort videos by how many similar users liked them

    return [vid for vid, count in sortedVids]  
    # return just the videos (ignore counts)


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