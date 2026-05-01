from collections import deque

class User:  # for one user
	def __init__(self, username: str, followinglist: list[str]):
		self.username = username
		self.followinglist = followinglist
	

class Post:  # for one person
	def __init__(self, username: str, post: str, timestamp: int):
		self.username = username
		self.post = post
		self.timestamp = timestamp


class WrittenPosts:  # collection of posts
	def __init__(self, writtenposts: dict[str, list[Post]], users: dict[str, User]):
		self.writtenposts = writtenposts
		self.users = users

	def from_handle(self, handle: str) -> list[Post]:
		# Return all the posts written by the user with the given handle
		if handle in self.writtenposts:
			return self.writtenposts[handle]
		return []

	def followingPage(self, user: User) -> list[Post]:
		result = []
		for u in user.followinglist:
			if u in self.writtenposts:
				result.extend(self.writtenposts[u])

		result.sort(key=lambda p: p.timestamp, reverse=True)
		return result

	def postsWithinDistance(self, user: User, n: int) -> list[Post]:
		result = []  # stores resulting post
		queue = deque()  
		visited = set()  # to prevent revisitng same user

		queue.append((user.username, 0))  # start from the given user at distance 0
		visited.add(user.username)  

		while queue:
			current, dist = queue.popleft()  #  take the next user to process

			if dist > n:
				continue  # if  user is too far away then skip

			if current in self.writtenposts:
				result.extend(self.writtenposts[current])  #add posts to result

			if current in self.users:
				for person in self.users[current].followinglist:  #  look at who user follows
					if person not in visited:
						visited.add(person)
						queue.append((person, dist + 1))  # add them with distance incremented by 1

		result.sort(key=lambda p: p.timestamp, reverse=True)  # newest posts should come first
		return result


#  Test
users = {
	"Alice": User("Alice", ["Bob"]),
	"Bob": User("Bob", ["Claire", "Dave"]),
	"Claire": User("Claire", ["Dave"]),
	"Dave": User("Dave", [])
}

writtenposts = {
	"Alice": [Post("Alice", "hello from alice", 1)],
	"Bob": [Post("Bob", "bob post 1", 3), Post("Bob", "bob post 2", 7)],
	"Claire": [Post("Claire", "claire post", 5)],
	"Dave": [Post("Dave", "dave post", 6)]
}

wp = WrittenPosts(writtenposts, users)

print([p.post for p in wp.followingPage(users["Alice"])])
print([p.post for p in wp.postsWithinDistance(users["Alice"], 2)])


