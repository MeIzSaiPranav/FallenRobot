import requests

def anime_search(bot, update):
    url = "https://api.jikan.moe/v4/search/anime?q="
    search_query = update.message.text.split()[1:]
    search_query = "+".join(search_query)
    if search_query:
        res = requests.get(url+search_query)
        if res.status_code == 200:
            anime_list = res.json()["data"]
            for anime in anime_list:
                message = "{}\n\nSynopsis: {}\n\nScore: {}\n\n".format(anime["attributes"]["canonicalTitle"], anime["attributes"]["synopsis"], anime["attributes"]["averageRating"])
                bot.send_message(chat_id=update.message.chat_id, text=message)
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Error: Failed to retrieve data from API")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Error: Please enter a search query")
