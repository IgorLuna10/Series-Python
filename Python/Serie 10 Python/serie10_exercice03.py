import requests

def recuperer_posts(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(e)
        return []

def calculer_stats_par_user(posts):
    stats = {}
    for post in posts:
        user_id = post.get('userId')
        titre = post.get('title', '')
        
        if user_id not in stats:
            stats[user_id] = {
                "nb_posts": 0,
                "longueur_totale": 0,
            }

        stats[user_id]['nb_posts'] += 1
        stats[user_id]['longueur_totale'] += len(titre)  # ✅ Bonne clé
    
    # Calculer les moyennes
    for user_id in stats:
        total = stats[user_id]["longueur_totale"]
        nb = stats[user_id]["nb_posts"]
        stats[user_id]["longueur_moyenne_titre"] = total / nb if nb > 0 else 0
        del stats[user_id]["longueur_totale"]
    
    return stats

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    call_posts = recuperer_posts(url)
    
    # Calculer les statistiques
    stats = calculer_stats_par_user(call_posts)
    
    # ✅ Trier par nombre de posts décroissant
    stats_triees = sorted(stats.items(), 
                          key=lambda x: x[1]['nb_posts'], 
                          reverse=True)
    
    # ✅ Afficher seulement le top 3
    print("Top 3 des utilisateurs les plus actifs :")
    for user_id, data in stats_triees[:3]:
        nb = data['nb_posts']
        longueur_moy = data['longueur_moyenne_titre']
        print(f"User {user_id} : {nb} posts (longueur moyenne titre : {longueur_moy:.1f})")
