import json
import urllib.request
from collections import Counter
from datetime import datetime

try:
    url = "https://jsonplaceholder.typicode.com/posts"
    print("Загрузка данных...")
    response = urllib.request.urlopen(url)
    posts = json.loads(response.read().decode())
    print(f"Загружено {len(posts)} постов")

    total_posts = len(posts)

    user_posts_count = Counter(post['userId'] for post in posts)
    posts_per_user = dict(user_posts_count)

    avg_body_length = sum(len(post['body']) for post in posts) / total_posts

    most_active_user_id = user_posts_count.most_common(1)[0][0]

    title_lengths = sorted([len(post['title']) for post in posts])
    n = len(title_lengths)
    if n % 2 == 0:
        median_title_length = (title_lengths[n // 2 - 1] + title_lengths[n // 2]) / 2
    else:
        median_title_length = title_lengths[n // 2]

    posts_with_length = []
    for post in posts:
        total_length = len(post['title']) + len(post['body'])
        posts_with_length.append({
            'id': post['id'],
            'userId': post['userId'],
            'total_length': total_length
        })

    posts_with_length.sort(key=lambda x: x['total_length'], reverse=True)
    top_longest_posts = posts_with_length[:5]

    report = {
        "generated_at": datetime.now().isoformat() + "Z",
        "source": url,
        "summary": {
            "total_posts": total_posts,
            "avg_body_length": round(avg_body_length, 1),
            "most_active_user_id": most_active_user_id,
            "median_title_length": median_title_length
        },
        "posts_per_user": posts_per_user,
        "top_longest_posts": top_longest_posts
    }

    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("\n=== Статистика ===")
    print(f"Всего постов: {total_posts}")
    print(f"Средняя длина body: {round(avg_body_length, 1)}")
    print(f"Самый активный пользователь: {most_active_user_id}")
    print(f"Медианная длина заголовка: {median_title_length}")
    print(f"\nФайл report.json создан!")

except Exception as e:
    print(f"Ошибка: {e}")