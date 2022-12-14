# Twitch Highlights Bot

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Twitch](https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

Welcome to the Twitch Highlights Bot!

This Python bot utilizes the Twitch API to retrieve the most viewed clips from a selected game of the week, creates a video compilation of these clips using MoviePy, and then uploads the compilation to YouTube with an automatically generated title, description, and thumbnail. With this bot, you can easily keep up with the most popular clips on Twitch and share them with others on YouTube.
![Youtube Channel](https://i.imgur.com/blU5A32.png)

## 🎥 Features
- Get the specified number of most watched clips of the week. Download the clips and create a video compilation.
- Add an on-screen text to the video compilation with the clip's and broadcaster's names.
- Upload the video compilation to YouTube with an automatically generated title, description, and thumbnail.

## 📋 Prerequisites
Before you begin, ensure you have met the following requirements:
- You have installed the latest version of Python 3.
- Git installed on your machine.
- A Twitch account and a google account.
- A registered application on [dev.twitch.tv](https://dev.twitch.tv/console) with a Twitch API Client ID and Client Secret
- A project created on [Google Cloud](https://cloud.google.com/) and downloaded a json file with the credentials.

If you need help getting credentials from Twitch or Google, you may check the following guides:
- [Twitch API](https://dev.twitch.tv/docs/authentication/register-app)
- [Google's API](https://developers.google.com/people/quickstart/python)


## 💾 Setting up
Clone this repository:
```bash
git clone https://github.com/viniciusenari/automated-twitch-clips-youtube-channel
```
Create a virtual environment and install the requirements:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Create a .env file and add the following variables:
```
CLIENT_SECRET = "your_twitch_client_secret"
CLIENT_ID = "your_twitch_client_id"
```
Create a client_secret.json file and add the credentials from Google Cloud. You can download this from the Google Cloud Console under the credentials tab. Make sure to rename the file to client_secret.json.

## 🔧 Configuration
The configuration file, [config.py](https://github.com/viniciusenari/automated-twitch-clips-youtube-channel/blob/main/project/config.py), is located in the project folder. In this file, you can change the fonts by specifying their file path. You can also change the rendering settings for the video compilation.
You can check what each parameter does in the [MoviePy documentation](https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html?highlight=write_videofile#moviepy.video.compositing.CompositeVideoClip.CompositeVideoClip.write_videofile).


## 📺 How to Use
To run the bot, open the terminal and navigate to the main.py file's directory. Then type the following command:
```bash
python main.py --game <game_name> --amount <amount> --languages <languages>
```
Replace `<game_name>` with the name of the game you want to use the bot for, `<amount>` with the number of clips you want to generate, and `<languages>` with a list of languages separated by spaces (e.g., "en fr de" for English, French, and German).
For example, if you want to generate ten clips for the game "League of Legends" in English and Brazilian Portuguese, you would use the following command:
```bash
python main.py --game "League of Legends" --amount 10 --languages en pt-br
```
You may also use the short versions of the arguments:
```bash
python main.py -g "League of Legends" -a 10 -l en pt-br
```
You'll see logs in the terminal as the bot runs. A progress bar will also show how much of the video has been rendered.

![Logs](https://i.imgur.com/GwXJVgx.png)

To upload your rendered video to YouTube, follow these steps:

1. Click on the link provided in the terminal to log in to your Google account.
2. Select the YouTube channel you want to use to upload the video.
3. After authenticating, you will be redirected to a page with a code. Copy this code.
4. Paste the code into the terminal, and it will upload the video to Youtube YouTube.
5. Follow the link provided in the terminal to access and view the uploaded video.

Note that the downloaded and created files will be in the folder `files`. The folder structure is as follows:
```
files  
  ├── clips  
  ├── overlays  
  ├── thumbnails
  └── youtube 
```
The `clips` folder holds the downloaded Twitch clips, the `overlays` folder has the text overlays for each clip, the `thumbnails` folder has the thumbnails for each clip, and the `youtube` folder contains the video compilation and its thumbnail

## 🤝 Contributing
### 💡 How to contribute
If you want to contribute to this project, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

### ✋ How to propose changes
If you want to propose changes to this project, follow these steps:

1. Open an issue with the tag "enhancement".
2. Describe the changes you want to make.
3. Wait for feedback from the project maintainers.

Alternatively, see the GitHub documentation on [creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issues/creating-an-issue).

### 🐛 How to report a bug
If you want to report a bug to this project, follow these steps:

1. Open an issue with the tag "bug".
2. Describe the bug.
3. Wait for feedback from the project maintainers.

Alternatively, see the GitHub documentation on [creating an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issues/creating-an-issue).

### 🤔 Ideas to Consider
Here are some ideas for contributions:

- Give the user the option to input a Twitch channel instead of a game and create a video compilation of the most viewed clips from that channel.
- Add command line arguments to specify other parameters value, such as the time range in which the clips were created.
- The current font does not support all characters for all languages. Suggest a font with broader language support, or add a way to select a font based on the language dynamically.


## 📜 License
The code for this bot is licensed under the GPL-3.0 License.