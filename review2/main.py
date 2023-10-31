from getParameters import AskUser
from filewriter import FileWriter
from api_service import DataService

def getAllPosts():
    # Retrieve all posts
    d = DataService('http://jsonplaceholder.typicode.com/posts')
    posts_l = d.getData()
    posts_file = 'all_posts.txt'
    f = FileWriter()
    for post in posts_l:
        f.writeToFile(posts_file, f'{post}')


def getUserPosts():
    # ask which user id then retrieve posts for that user
    g = AskUser()
    u = g.askUser()
    url = f'https://jsonplaceholder.typicode.com/users/{u}/posts'
    d = DataService(url)
    posts_u = d.getData()
    posts_file = f'user{u}_posts.txt'
    f = FileWriter()
    for post in posts_u:
        f.writeToFile(posts_file, f'{post}')
        f.writeToFile(posts_file, '\n')

def main():
    # getAllPosts()
    getUserPosts()
    
if __name__ == '__main__':
    main()
