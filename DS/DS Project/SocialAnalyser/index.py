import matplotlib.pyplot as plt

social_media_platforms = ["Instagram", "Facebook", "Snapchat", "WhatsApp"]
user_counts = [2000, 3049, 293, 2000] 

plt.figure(figsize=(10, 6))
plt.bar(social_media_platforms, user_counts, color=['blue', 'green', 'yellow', 'purple'])
plt.title('Number of Users on Social Media Platforms')
plt.xlabel('Social Media Platforms')
plt.ylabel('Number of Users (in millions)')
plt.show()
