comments = {}


class User:
    def __init__(self, username, password, email, created_at):
        self.username = username
        self.password = password
        self.email = email
        self.created_at = created_at

    def leave_comment(self, id, text):
        print(f"Left comment {id}")
        comments.setdefault(id, {self.username: text})

    def login(self, username, password):
        pass

    def logout(self):
        pass

    def signup(self, username, password):
        pass


class Admin(User):
    def __init__(self, username, password, email, created_at, role, permissions):
        super().__init__(username, password, email, created_at)
        self.role = role
        self.permissions = permissions

    def delete_comment(self, id):
        if id in comments:
            del comments[id]
            print(f"Deleted comment {id}")


user1 = User("hamed", "123", "hamed@gmail.com", "2023-07-16")
user2 = User("aria", "456", "aria@gmail.com", "2023-11-26")

admin1 = Admin("mohammad", "756", "mohammad@gmail.com", "2024-01-05", "comment manager", ["deleting comments"])

user1.leave_comment("10101", "eyval")
user1.leave_comment("10102", "damet garm")

print(comments)

admin1.delete_comment("10101")

print(comments)
