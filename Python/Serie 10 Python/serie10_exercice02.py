def recuperer_posts(url):
    import requests

    try: 
        response = requests.get(url)
    
        if response.status_code == 200:
            return response.json()
        else:
            return []
    
    except requests.exceptions.RequestException as e:
        print(e)
        return []

def afficher_resume_posts(posts, n=5):
    for post in posts[:n]: 
        post_id = post.get('id', '?')
        user_id = post.get('userId', '?')
        titre = post.get('title', 'Sans titre')
        print(f"Post #{post_id} (user {user_id}) : {titre}")


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/posts"
    call_posts = recuperer_posts(url)
    print(f"Nombre total : {len(call_posts)}")
    afficher_resume_posts(call_posts)
