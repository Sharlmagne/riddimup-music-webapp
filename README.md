# RiddimUp

#### Video Demo:  https://youtu.be/aHhwnyBzrQE

#### Description:. RiddimUp is an audio streaming web application that was developed using the Django framework. The intention of this web application is to become a purposeful platform for organic ranking of music based on the general public. This is a prototype of a revolutionary way of gamifying musical works. Ultimately, riddim up will become the platform for upcoming artists to make a following that wholeheartedly believes in their talent and rewards them accordingly.


#### Templates

Home - This is the main page that can be accessed without logging in. It contains all the audio uploads of all the users. From here, you can listen to tracks and share. However, to like and comment on each track, login is required. On the desktop view, to the right of the page, users can see a top 10 chart for the singles uploaded. The ranking of the singles is dependent on the number of likes for each track.

Charts - There is a dedicated page for charts to access all the details of the top 10 tracks. My intention was to add special features like showing the movement of each track and the number of weeks present on the charts. However, the complexity and development time prevented me from overcomplicating the data shown.

Uploads - This is the page where tracks are uploaded for each user. Login is required for this to be available in the navbar. Here, users are required to upload track and artist name along with the mp3 and cover art for the track.

Profile - After uploading tracks, users will be directed to their profile with all of their previously uploaded tracks. Ideally, the intention was to make each profile accessible to other users, unfortunately, only users can view their profile.

Login - Use username and password to login, if you don’t have a profile, there is an option to access the register page.

Register - New users can enter name, email, and password.

Track - Clicking the cover art for each track will take you to the detailed view for that track. Here you will see the comments of that single track.

Search - Search for any track and the algorithm will query both the artist name and track title.

Accounts - Users can change name, email and profile information.


#### Databases

Users - All users information is stored here. This include username, email, password

Comments - All comments are linked to both users and tracks to keep track of all the comments under each track and all the comments of a specific user.

Profile - This is linked to each user and includes the profile picture.

Tracks - This contains all the mp3 audio files with cover art and artist name, linked to users responsible for uploads.
