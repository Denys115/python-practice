class User:
    def __init__(self, name, email, password, current_job_title):
        self.name = name
        self.email = email
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(F"User {self.name} currently works as a {self.current_job_title}. you can contact him at {self.email}")

class Post:
    def __init__(self,message, author):
        self.message = message
        self.author = author
    def get_post_info(self):
        print(f"Post: {self.message} written by {self.author}")


app_user_one = User("Denis DDC", "Denis@DDC", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("Denyz Learns", "dd@ll", "supersecret", "Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()