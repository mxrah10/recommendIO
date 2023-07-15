from dotenv import load_dotenv
import os
import requests
from db_creation import db, app, Anime

load_dotenv('pass.env')

with app.app_context():
    image='https://cdn.myanimelist.net/images/anime/10/47347.jpg'
    image_data = requests.get(image).content
    attack_on_titan = Anime(
        title='Attack on Titan',
        genre=', '.join(['Action', 'Adventure', 'Drama', 'Fantasy', 'Mystery']),
        tags=', '.join(['Shounen', 'Super Power','Military', 'Revenge', 'Gore', 'Apocalyptics', 'Tragedy']),
        summary='''Hundreds of years ago, horrifying creatures which resembled humans appeared. These mindless, towering giants, called "Titans," proved to be an existential threat, as they preyed on whatever humans they could find in order to satisfy a seemingly unending appetite. Unable to effectively combat the Titans, mankind was forced to barricade themselves within large walls surrounding what may very well be humanity's last safe haven in the world.

In the present day, life within the walls has finally found peace, since the residents have not dealt with Titans for many years. Eren Yeager, Mikasa Ackerman, and Armin Arlert are three young children who dream of experiencing all that the world has to offer, having grown up hearing stories of the wonders beyond the walls. But when the state of tranquility is suddenly shattered by the attack of a massive 60-meter Titan, they quickly learn just how cruel the world can be. On that day, Eren makes a promise to himself that he will do whatever it takes to eradicate every single Titan off the face of the Earth, with the hope that one day, humanity will once again be able to live outside the walls without fear.''',
        year=2013,
        continuity='Ongoing',
        image=image_data
    )

    db.session.add(attack_on_titan)
    db.session.commit()

    print("Anime added to the database.")
    anime = Anime.query.filter_by(title='Attack on Titan').first()
    print(anime.title)
    print(anime.genre)
