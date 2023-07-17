def create_youtube_video(title, description):
	youtube_video = {'title': title, 'description': description, 'likes': 0, 'dislikes': 0, 'comments': {}}
	return youtube_video

def like(youtube_video):
	if 'likes' in youtube_video:
		youtube_video['likes'] +=1

def dislikes(youtube_video):
	if 'dislikes' in youtube_video:
		youtube_video['dislikes'] +=1

def add_comment(video, username, comment_text):
	video['comments'][username] = comment_text

video = create_youtube_video('Goats are amazing', 'Find out why goats are superior to humans')
like(video)
dislikes(video)
add_comment(video, 'eva','I agree, goats are superior to humans')

for i in range (495):
	like(video)

print(video)