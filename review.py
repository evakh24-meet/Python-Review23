def create_youtube_video(title, description):
	youtube_video = {'title': title, 'description': description, 'likes': 0, 'dislikes': 0, 'comments': {}}
	return youtube_video

def like(youtube_video):
	if 'likes' in youtube_video:
		youtube_video['likes'] +=1

def dislikes(youtube_video):
	if 'dislikes' in youtube_video:
		youtube_video['dislikes'] +=1

def add_comment(youtubevideo, username, comment_text):


