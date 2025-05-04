#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        j_obj = r.json()

        for i in j_obj:
            print(i["title"])

def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")

    posts = r.json()
    post = []

    if r.status_code == 200:
        for i in posts:
            post.append({'id': i['id'],
                           'title': i['title'],
                           'body': i['body']})

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(post)
