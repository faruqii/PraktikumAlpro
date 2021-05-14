blog_posts = [
{'Photos': 3, 'Likes': 21, 'Comments': 2},
{'Likes': 13, 'Comments': 2, 'Shares': 1},
{'Photos': 5,'Likes': 33, 'Comments': 8, 'Shares': 3}, 
{'Comments': 4,'Shares': 2}]
total_likes = 0
postn = 1
for post in blog_posts:
    print("Post ke - ",postn)
    postn+=1
    #Tambahkan code disini
    try:
        sum_of = post['Likes']
        print("Post ini memiliki",sum_of,"likes")
    except KeyError:
        print("Post ini tidak memiliki likes")
    else:
        total_likes = total_likes + post['Likes']
print("Jumlah total likes adalah ", total_likes)


