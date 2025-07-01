
from rich.console import Console
import questionary
import json
import google.generativeai as genai

import csv
import movie as MOVIE
import rating as RATING
import booking as BOOKING
import genres as GENRES
import user as USER
import random
import platform
import subprocess

users:list= []
movies:list= []
ratings:list= []
genres:list= []
bookings:list= []
admins:list= []

genai.configure(api_key="AIzaSyAUQSI2i9HibXAZkRS6Z0H_VDY1Ug8dmj8")
model = genai.GenerativeModel('gemini-2.0-flash')





try:
    with open('users.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        users_json= json.loads(content)
        for User in users_json:
            user = USER.User.from_dict(User)
            users.append(user)
        File.close()
except Exception as e:
    print(e)


try:
    with open('movies.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        movies_json= json.loads(content)
        for movie in movies_json:
            movie = MOVIE.Movie(movie['id'], movie['title'],movie['description'], movie['release_year'])
            movies.append(movie)
        File.close()
except Exception as e:
    print(e)


def isUser(email):
    for user in users:
        if user.getEmail() == email:
            return user.getId()
    return False

def isUserById(id):
    for user in users:
        if user.getId() == id:
            return user
    return False

def findMovie(movieId):
    for m in movies:
        if m.getId() == movieId:
            return m
    return None



try:
    with open('bookings.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        booking_json=  json.loads(content)
        for book in booking_json:
            bookObj = BOOKING.Booking(book['id'],book['movie_id'],book['user_id'],book['row'],book['seat'])
            bookings.append(bookObj)
        File.close()
except Exception as e:
    print(e)


try:
    with open('ratings.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        ratings_json=  json.loads(content)
        for rate in ratings_json:
            ratingOBJ = RATING.Rating.from_dict(rate)
            ratings.append(ratingOBJ)
        File.close()
except Exception as e:
    print(e)

try:
    with open('genres.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        genres_json=  json.loads(content)
        for genre in genres_json:
            genresOBJ = GENRES.Genres.from_dict(genre)
            genres.append(genresOBJ)
        File.close()
except Exception as e:
    print(e)


try:
    with open('admins.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        admins= json.loads(content)
        File.close()
except Exception as e:
    print(e)

    
    
    
def SmartSearch(user_input):
    movie_data = ""
    for m in movies:
        movie_data += f"Title: {m.getTitle()}\nDescription: {m.getDescription()}\nGenres: {', '.join(g.getName() for g in m.getGenres(genres))}\n\n"

    prompt = f"""
I have the following list of movies with title, description and genres:

{movie_data}

Now based on the following user request, suggest the best matching movies (top 3) from the list above only. Return just the movie titles.

User request: "{user_input}"
"""  
    try:
        response = model.generate_content(prompt)
        return response.text.strip().split("\n")
    except Exception as e:
        print("AI Error:", e)
        return []


def getAiRecommendations(user_input):
    prompt = f"""
    Recommend 5 popular movies based on the following preferences or keywords:
    {user_input}

    Please provide only the movie titles separated by commas, each movie in line.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip().split("\n")
    except Exception as e:
        print("AI Error:", e)
        return []

def SummarizeMovie(movie_id, movie_title):
    movie_reviews = [
        f"{r.getDescription()}: {r.getScore()} stars"
        for r in ratings if r.getMovieId() == movie_id
    ]
    if not movie_reviews:
        return "No reviews available to summarize."

    prompt = f"""Summarize the following user ratings and reviews for the movie "{movie_title}":
{chr(10).join(movie_reviews)}
Highlight common opinions, praise, and criticism. Be concise."""

    try:
        response = model.generate_content(prompt)
        return response.text.strip().split("\n")
    except Exception as e:
        print("AI Error:", e)
        return []


def getSimilarMovies( movie_title):
    movie_genres = movie.getGenres(genres)
    genre_names = [g.getName() for g in movie_genres]

 

    prompt = f"""
    List 10 movies similar to "{movie_title}" based on these genres: {", ".join(genre_names)}.
    Only return movie titles and release years. Format them exactly like this:
    - Movie Title (Year)
    Do not include any introduction or explanation.
    """
    try:
        response = model.generate_content(prompt)
        print(response.text.strip().split("\n"))
        return response.text.strip().split("\n")
    except Exception as e:
        print("AI Error:", e)
        return []

console = Console()


first_msg = console.print('''
[bold green]ًWelcome to Movie CLI Project ![/bold green]ً
 [bold blue]Sign in [/bold blue]
    
''')
choices = [
        "1) As user",
        "2) As admin",
]

selected = questionary.select(
        " you are Admin or User?:",
        choices=choices,
        use_arrow_keys=True 
    ).ask()
    
if selected == choices[0]:

    user_email  = console.input("enter your email: ")
    if isUser(user_email):
        console.print('[bold green]ً welcome back ! [/bold green]')
 
    else:
        user = USER.User.from_dict({'id':random.randint(100000, 999999) , "email":user_email})
        console.print('\n[bold blue] Welcome ! new account created [/bold blue]')
        users.append(user)

            
   
    msg = console.print('''\n[bold green]ًWelcome to Movie CLI Project ![/bold green]ً
            
Please choose an option:
''')
    user_choices = [
    "1) Show available movies",
    "2) Book a movie",
    "3) Cancel a book",
    "4) Show booking history",
    "5) Smart search for a movie (using AI)" ,
    "6) Get AI movie recommendations (using AI)",
    "7) Summarize reviews (using AI)",
    "8) Recommend Similar Movies (using AI)",
    "9) Rate & review a movie",
    "10) Exit",
]

    selected2 = questionary.select(
        " Please choose an option:",
        choices=user_choices,
        use_arrow_keys=True 
    ).ask()
    while selected2 != user_choices[9]:
       
        if selected2 == user_choices[0]:
            print('----------------')
            for movie in movies:
                        movie_bookings = [b for b in bookings if b.getMovieId() == movie.getId()]
                   
                        if len(movie_bookings) < 100:
                            movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                            try:
                                total_score = sum(r.getScore() for r in movie_ratings)
                                average_score = total_score / len(movie_ratings)
                            except Exception as e:
                                total_score =0
                                average_score = 0

                            movie_genres = movie.getGenres(genres)
                            genre_names = [g.getName() for g in movie_genres]

                            console.print(f'''[blue]\n
[bold green] {movie.getTitle()}[/bold green]
description: [black]{movie.getDescription()}        [/black]                       
release_year: [bold yellow]{movie.getReleaseYear()}        [/bold yellow]                       
average_ratings : [bold yellow]{average_score} ★ [/bold yellow]       
Avaliable Seats : [bold yellow]{len(movie_bookings)}[/bold yellow]   
Genres: [black] {(" - ".join(genre_names))} [/black]
Ratings:[/blue]''')
                            i = 0
                            movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                            for ratin in movie_ratings:
                                i+=1
                                description = ratin.getDescription()
                                score = ratin.getScore()
                                console.print(f" [bold]{i}[/bold]- {description}: {score}")
                                print('----------------')
        elif selected2 == user_choices[1]:
            select_movie_choise = []
            for index, movie in enumerate(movies):
                title = movie.getTitle()
                desc = movie.getDescription()
                year = movie.getReleaseYear()
                        
                movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                try:
                    total_score = sum(r.getScore() for r in movie_ratings)
                    average_score = total_score / len(movie_ratings)
                except Exception as e:
                    total_score =0
                    average_score = 0

                choice_line = f"{title} | {year} - Rating : {average_score}"
                select_movie_choise.append(
                questionary.Choice(title=choice_line, value=index)
                )


            selected_movie_index = questionary.select("choose one of the following movies:",
            choices=select_movie_choise,use_arrow_keys=True).ask()

            selected_movie = movies[selected_movie_index]
            user_booked_seats = [(b.getRow(), b.getSeat()) for b in bookings if b.getMovieId() == selected_movie.getId() and b.getUserId() == isUser(user_email)]   
            
            if len(user_booked_seats) > 0:
                    console.print("[red]Sorry ! you already book for this movie before. [/red]")
            else:
                   
                console.print("\n            Screen  \n")
                console.print("   1  2  3  4  5  6  7  8  9  10 ")
            
                booked_seats = [(b.getRow(), b.getSeat()) for b in bookings if b.getMovieId() == selected_movie.getId()]    
                for row in range(10):
                    row = chr(65 + row)
                    seat_display = []
                    for seat in range(1, 11): 
                        if (row, seat) in booked_seats:
                            seat_display.append("🚫")
                        else:
                            seat_display.append("🟩")
                    print(f"{row}  {' '.join(seat_display)}")

            
                while True:
                    seat_input = console.input("enter a row and seat to book: (EX : A5) ").upper()
                    if len(seat_input) < 2 or not seat_input[1:].isdigit():
                        console.print("[red] invalid seat (e.g., A5)[/red]")
                        continue
                    row = seat_input[0]
                    seat = int(seat_input[1:])
                    if (row, seat) in booked_seats:
                        console.print("[red] seat is taken.[/red]")
                    elif seat < 1 or seat > 10 or row not in "ABCDEFGHIJ":
                        console.print("[red] seat is invalid.[/red]")
                    else:
                        break



                selected_row = seat_input[0]
                selected_seat = int(seat_input[1:])
                if (selected_row, selected_seat) in booked_seats:
                    console.print(f"[red] Sorry its already booked![/red]")
                    seat_input =console.input("provide a row and seat to book: (EX : A5)")


        
                else:
                    new_booking = BOOKING.Booking(random.randint(100000, 999999),selected_movie.getId(),isUser(user_email),selected_row,selected_seat)
                    bookings.append(new_booking)
                    console.print(f'''[bold green]Booked successfully !
    Movie Title: {selected_movie.getTitle()}
    email: {user_email}
    row: {selected_row}
    seat: {selected_seat}
    [/bold green]''')
            

            
        elif selected2 == user_choices[2]:
            user_bookings = [b for b in bookings if b.getUserId() == isUser(user_email)]   
            if len(user_bookings) < 0:
                console.print("[red] Sorry no bookings found.[/red]")
            else:
                console.print("\nBookings list:")
                bookings_choices = []
                for b in user_bookings:
                    movie = findMovie(b.getMovieId())
                    choice_title = f"{movie.getTitle()} - Row {b.getRow()} Seat {b.getSeat()}"
                    choice = questionary.Choice(title=choice_title, value=b.getId())
                    bookings_choices.append(choice)

                selected_index = questionary.select("Choose a booking to cancel:",choices=bookings_choices).ask()
                for i, booking in enumerate(bookings):
                    if booking.getId() == selected_index:
                     removed = bookings.pop(i)
                     console.print(f'''[bold red]Booking canceled successfully !
Movie Title: {movie.getTitle()}
email: {user_email}
row: {removed.getRow()}
seat: {removed.getSeat()}
[/bold red]''')
        
        
        
        elif selected2 == user_choices[3]:
            user_bookings = [b for b in bookings if b.getUserId() == isUser(user_email)]   
            if len(user_bookings) < 0:
                console.print("[red] Sorry no bookings found.[/red]")
            else:
                console.print("\nBookings list:")
                for b in user_bookings:
                    movie = findMovie(b.getMovieId())
                    console.print(f"{movie.getTitle()} - Row {b.getRow()} Seat {b.getSeat()}")
        

        elif selected2 == user_choices[4]:
            console.print("[bold blue]\n Smart Search (using AI)[/bold blue]")
            user_query = console.input("🔍 What are you looking for in a movie?\n> ")

            result_titles = SmartSearch(user_query)

            if not result_titles:
                console.print("[red]⚠️ No matching movies found.[/red]")
            else:
                console.print("[bold yellow]\nAI Recommended Matches:[/bold yellow]")
                for title in result_titles:
                    console.print(f"- [bold]{title}[/bold]")

        elif selected2 == user_choices[5]:
            console.print("[bold blue]\n get AI Recommendations (using AI) [/bold blue]")
            user_query = console.input(" Enter your favorite genres, actors, or keywords:\n> ")

            result_titles = getAiRecommendations(user_query)

            if not result_titles:
                console.print("[red]⚠️ No matching movies found.[/red]")
            else:
                console.print("[bold yellow]\nAI Recommendations:[/bold yellow]")
                for title in result_titles:
                    console.print(f"- [bold]{title}[/bold]")


        elif selected2 == user_choices[6]:
            select_movie_choise = []
            for movie in movies:
                title = movie.getTitle()
                desc = movie.getDescription()
                year = movie.getReleaseYear()


                choice_line = f"{title} | {desc} - {year} "
                select_movie_choise.append(
                questionary.Choice(title=choice_line, value=movie.getId()))


            selected_movie_index = questionary.select("choose one of the following movies:",
            choices=select_movie_choise,use_arrow_keys=True).ask()
            selected_movie = next((m for m in movies if m.getId() == selected_movie_index), None)
            summary = SummarizeMovie(selected_movie.getId(),selected_movie.getTitle())

            console.print(f"\n[bold blue]Summary of Reviews for {selected_movie.getTitle()}[/bold blue]:")
            console.print(summary[0])





        elif selected2 == user_choices[7]:
            select_movie_choise = []
            for movie in movies:
                title = movie.getTitle()
                desc = movie.getDescription()
                year = movie.getReleaseYear()


                choice_line = f"{title} | {desc} - {year} "
                select_movie_choise.append(questionary.Choice(title=choice_line, value=movie.getId()))


            selected_movie_index = questionary.select("choose one of the following movies:",
            choices=select_movie_choise,use_arrow_keys=True).ask()
            selected_movie = next((m for m in movies if m.getId() == selected_movie_index), None)
            similar_movies = getSimilarMovies(selected_movie.getTitle())
            console.print(f"\n[bold blue]Similar movies for {selected_movie.getTitle()}[/bold blue]:")
            for movie_line in similar_movies:
                print(movie_line)







        elif selected2 == user_choices[8]:
            select_movie_choise = []
            user_bookings = [b for b in bookings if b.getUserId() == isUser(user_email)]   
            if len(user_bookings) > 0:
                for book in user_bookings:
                    movie = findMovie(book.getMovieId())
                    title = movie.getTitle()
                    desc = movie.getDescription()
                    year = movie.getReleaseYear()


                    choice_line = f"{title} | {desc} - {year} "
                    select_movie_choise.append(
                    questionary.Choice(title=choice_line, value=movie.getId())
                    )


                selected_movie_index = questionary.select("choose one of the following movies:",
                choices=select_movie_choise,use_arrow_keys=True).ask()

                rate_movie = console.input("write your opinion about movie: ")
                rating = questionary.select("How many stars would you rate this movie?",
                choices=[
                "1 ★☆☆☆☆",
                "2 ★★☆☆☆",
                "3 ★★★☆☆",
                "4 ★★★★☆",
                "5 ★★★★★"]).ask()

                rating_number = int(rating[0])
                console.print(f"\n you rated: {rating_number} stars!")
                console.print("[bold green]Thanks for rating, see you again. [/bold green]")
                rating_number = int(rating_number) 

                rating_data = {
                    "id": random.randint(100000, 999999),
                    "movie_id": selected_movie_index,
                    "user_id": isUser(user_email),
                    "description": rate_movie,
                    "score": rating_number
                }

                new_rating = RATING.Rating.from_dict(rating_data)

                ratings.append(new_rating)
            
            else:
                console.print("[red] Sorry no bookings found.[/red]")



            
            





           



        selected2 = questionary.select(
        "\n Please choose an option:",
        choices=user_choices,
        use_arrow_keys=True).ask()
    else:
        with open('users.json', 'w', encoding='UTF-8') as file:
            content = json.dumps([u.to_dict() for u in users], indent=2, ensure_ascii=False)
            file.write(content)

        # Save movies
        with open('movies.json', 'w', encoding='UTF-8') as file:
            content = json.dumps([m.to_dict() for m in movies], indent=2, ensure_ascii=False)
            file.write(content)

        # Save bookings
        with open('bookings.json', 'w', encoding='UTF-8') as file:
            content = json.dumps([b.to_dict() for b in bookings], indent=2, ensure_ascii=False)
            file.write(content)

        with open('ratings.json', 'w', encoding='UTF-8') as file:
            content = json.dumps([r.to_dict() for r in ratings], indent=2, ensure_ascii=False)
            file.write(content)
                    
        with open('genres.json', 'w', encoding='UTF-8') as file:
            content = json.dumps([g.to_dict() for g in genres], indent=2, ensure_ascii=False)
            file.write(content)

elif selected == choices[1]:

    admin_email  = console.input("enter your email: ")
    emailFinded = False
    for admin in admins:
        if admin['email'] == admin_email:
            emailFinded = True
            console.print('[bold green]ً welcome back ! [/bold green]')
            continue
    if emailFinded == False:
        console.print('[bold red] Sorry ! email not found [/bold red]')
    else:

        msg = console.print('''\n[bold red]ًWelcome to Movie CLI Project ! (Signed As Admin) [/bold red]ً
Please choose an option:
''')
        admin_choices = [
    "1) Show available movies",
    "2) Add new movie",
    "3) Delete a movie",
    "4) Edit existing movie information",
    "5) Book a movie for customer",
    "6) Cancel a movie booking for customer",
    "7) View customer booking history",
    "8) View movies Statistics & Reports",
    "9) Smart Analytics & Predictions (using AI)",
    "10) AI Forecast: Future Booking Predictions (using AI)",
    "11) Movie Success Predictor (using AI)",
    "12) Summarize reviews (using AI)",
    "13) Exit",
]

        selected3 = questionary.select(
        " Please choose an option:",
        choices=admin_choices,
        use_arrow_keys=True).ask()
   
        while selected3 != admin_choices[12]:
            if selected3 == admin_choices[0]:
                    for movie in movies:
                        movie_bookings = [b for b in bookings if b.getMovieId() == movie.getId()]
                   
                        if len(movie_bookings) < 100:
                            movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                            try:
                                total_score = sum(r.getScore() for r in movie_ratings)
                                average_score = total_score / len(movie_ratings)
                            except Exception as e:
                                total_score =0
                                average_score = 0

                            movie_genres = movie.getGenres(genres)
                            genre_names = [g.getName() for g in movie_genres]

                            console.print(f'''[blue]\n
[bold green] {movie.getTitle()}[/bold green]
description: [black]{movie.getDescription()}        [/black]                       
release_year: [bold yellow]{movie.getReleaseYear()}        [/bold yellow]                       
average_ratings : [bold yellow]{average_score} ★ [/bold yellow]       
Avaliable Seats : [bold yellow]{len(movie_bookings)}[/bold yellow]   
Genres: [black] {(" - ".join(genre_names))} [/black]
Ratings:[/blue]''')
                            i = 0
                            movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                            for ratin in movie_ratings:
                                i+=1
                                description = ratin.getDescription()
                                score = ratin.getScore()
                                console.print(f" [bold]{i}[/bold]- {description}: {score}")
                                print('----------------')
            elif selected3 == admin_choices[1]:
                movie_name= console.input("enter movie name\n")
                for m in movies:
                    while m.getTitle() == movie_name:
                        console.print("Sorry ! movie already added.")
                        movie_name= console.input("enter movie name\n")
                        

                use_ai_description = questionary.confirm("Do you want to generate the movie description using AI ?").ask()
                if use_ai_description:
                    try:
                        ai_prompt = f"Write a short, professional movie description for a film titled '{movie_name}'."
                        response = model.generate_content(ai_prompt)
                        movie_description = response.text.strip()
                        console.print(f"[bold green] AI-generated description:[/bold green] {movie_description}")
                    except Exception as e:
                        console.print("[red] Failed to generate description using AI. Please enter manually.[/red]")
                        movie_description = console.input(" Enter movie description:\n")
                else:
                    movie_description = console.input("Enter movie description:\n")
    
                movie_release_year= console.input("enter a release year (ex : 2025) \n")
                while movie_release_year.isdigit() == False:
                        console.print("Sorry ! enter correct release year")
                        movie_release_year= console.input("enter a release year (ex : 2025) \n")

                added_genres = []
                movie_id =random.randint(100000, 999999)
                movie_genres_input = console.input('Write movie genres (comma separated): ')
                added_genres = [g.strip() for g in movie_genres_input.split(',')]

                for genre_name in added_genres:
                    existing_genre = next((g for g in genres if g.getName().lower() == genre_name.lower()), None)
                    
                    if existing_genre:
                        added = existing_genre.addMovie(movie_id)
                        if added:
                            console.print(f"Added movie {movie_id} to genre '{existing_genre.getName()}'")
                        else:
                            console.print(f"Movie {movie_id} already in genre '{existing_genre.getName()}'")
                    else:
                        genre_data = {
                            "id": random.randint(100000, 999999),
                            "name": genre_name,
                            "movies": [movie_id]
                        }
                        new_genre = GENRES.Genres.from_dict(genre_data)
                        genres.append(new_genre)
                        console.print(f"new genre created: '{genre_name}' and added movie {movie_id}")

                console.print("[blue] Genres stored successfully! [/blue]")

                
                    
                
                movie_data = {
                    "id": movie_id,
                    "title": movie_name,
                    "description": movie_description,
                    "release_year": movie_release_year,
                }

                new_movie = MOVIE.Movie.from_dict(movie_data)

                movies.append(new_movie)
                movie_genres = movie.getGenres(genres)
                genre_names = [g.getName() for g in movie_genres]


                console.print(f'''[bold green]movie added successfully !
Movie Title: {movie_name}
Movie Description: {movie_description}
release_year: {movie_release_year}
genres: {(" - ".join(genre_names))}
[/bold green]''')
                


            elif selected3 == admin_choices[2]:
                if not movies:
                    console.print("[red]No movies to delete.[/red]")
                else:
                    movie_choices = [
                        questionary.Choice(title=f"{m.getTitle()} ({m.getReleaseYear()})", value=m.getId())
                        for m in movies
                    ]
                    selected_id = questionary.select(
                        "Select a movie to delete:", choices=movie_choices
                    ).ask()

                    selected_movie = next((m for m in movies if m.getId() == selected_id), None)

                    if selected_movie:
                        confirm = questionary.confirm(f"Are you sure you want to delete '{selected_movie.getTitle()}'?").ask()
                        if confirm:
                            movies.remove(selected_movie)

                            ratings = [r for r in ratings if r.getMovieId() != selected_movie.getId()]

                            bookings = [b for b in bookings if b.getMovieId() != selected_movie.getId()]

                            for g in genres:
                                g.removeMovie(selected_movie.getId())

                            console.print(f"[bold red]Movie '{selected_movie.getTitle()}' deleted.[/bold red]")


            elif selected3 == admin_choices[3]:
                if not movies:
                    console.print("[red]No movies to edit.[/red]")
                else:
                    movie_choices = [
                        questionary.Choice(title=f"{m.getTitle()} ({m.getReleaseYear()})", value=m.getId())
                        for m in movies
                    ]
                    selected_id = questionary.select(
                        "Select a movie to edit:", choices=movie_choices
                    ).ask()

                    selected_movie = next((m for m in movies if m.getId() == selected_id), None)

                    if selected_movie:
                        new_title = console.input(f"Enter new title [{selected_movie.getTitle()}]: ") or selected_movie.getTitle()
                        new_description = console.input(f"Enter new description [{selected_movie.getDescription()}]: ") or selected_movie.getDescription()
                        new_year = console.input(f"Enter new release year [{selected_movie.getReleaseYear()}]: ") or selected_movie.getReleaseYear()

                        while new_year.isdigit() == False:
                            console.print("[red]Please enter a valid year[/red]")
                            new_year = console.input("Enter new release year: ")

                        selected_movie.setTitle(new_title)
                        selected_movie.setDescription(new_description)
                        selected_movie.setReleaseYear(new_year)
                        console.print(f"[blue]current genres: {', '.join([g.getName() for g in selected_movie.getGenres(genres)])}[/blue]")

                        genre_input = console.input("enter new genres (write , to seprate): ")
                        new_genre_names = [g.strip().lower() for g in genre_input.split(',') if g.strip()]
                        


                        for g in genres:
                            g.removeMovie(selected_movie.getId())
                            for genre_name in new_genre_names:
                                genre_obj = next((g for g in genres if g.getName().lower() == genre_name), None)

                                if genre_obj:
                                    genre_obj.addMovie(selected_movie.getId())
                                else:
                                    new_genre = GENRES.Genres(
                                    id=random.randint(100000, 999999),
                                    name=genre_name,
                                    movies=[selected_movie.getId()]
                                    )
                                    genres.append(new_genre)

                        console.print(f"[bold green] Movie updated successfully![/bold green]")



            elif selected3 == admin_choices[4]:
                if not users or not movies:
                    console.print("[red] sorry ! no users or movies found[/red]")
                else:
                    user_choices = [questionary.Choice(title=u.getEmail(), value=u.getId()) for u in users]
                    selected_user_id = questionary.select(" select user: ", choices=user_choices).ask()

                    select_movie_choise = []
                    for i, movie in enumerate(movies):
                        title = movie.getTitle()
                        desc = movie.getDescription()
                        year = movie.getReleaseYear()
                                
                        movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                        try:
                            total_score = sum(r.getScore() for r in movie_ratings)
                            average_score = total_score / len(movie_ratings)
                        except Exception as e:
                            total_score =0
                            average_score = 0

                        choice_line = f"{title} | {year} - Rating : {average_score} \n Description: {desc}"
                        select_movie_choise.append(
                        questionary.Choice(title=choice_line, value=i)
                        )


                    selected_movie_index = questionary.select("choose one of the following movies:",
                    choices=select_movie_choise,use_arrow_keys=True).ask()
                    selected_movie = movies[selected_movie_index]

                    booked_seats = [(b.getRow(), b.getSeat()) for b in bookings if b.getMovieId() == selected_movie_index]
                    for row in range(10):
                        row_letter = chr(65 + row)
                        seat_display = []
                        for seat in range(1, 11):
                            if (row_letter, seat) in booked_seats:
                                seat_display.append("🚫")
                            else:
                                seat_display.append("🟩")
                        print(f"{row_letter}  {' '.join(seat_display)}")

                    while True:
                        seat_input = console.input("enter a row and seat to book: (EX : A5) ").upper()
                        if len(seat_input) < 2 or not seat_input[1:].isdigit():
                            console.print("[red] invalid seat (e.g., A5)[/red]")
                            continue
                        row = seat_input[0]
                        seat = int(seat_input[1:])
                        if (row, seat) in booked_seats:
                            console.print("[red] Sorry ! seat is taken.[/red]")
                        elif seat < 1 or seat > 10 or row not in "ABCDEFGHIJ":
                            console.print("[red] seat is invalid.[/red]")
                        else:
                            break

                    new_booking = BOOKING.Booking.from_dict({
                        "id": random.randint(100000, 999999),
                        "movie_id": selected_movie_index,
                        "user_id": selected_user_id,
                        "row": row,
                        "seat": seat
                    })
                    
                    bookings.append(new_booking)
                    console.print(f'''[bold green]Booked successfully !
row: {row}
seat: {seat}
[/bold green]''')


            elif selected3 == admin_choices[5]:
                if not users or not bookings:
                    console.print("[red] sorry ! no users or movies found[/red]")
                else:
                    user_choices = [questionary.Choice(title=u.getEmail(), value=u.getId()) for u in users]
                    selected_user_id = questionary.select("Select user: ", choices=user_choices).ask()

                    user_bookings = [b for b in bookings if b.getUserId() == selected_user_id]
                    if not user_bookings:
                        console.print("[red] sorry ! there is no bookings for selected user[/red]")
                    else:
                        booking_choices = []
                        for b in user_bookings:
                            movie = findMovie(b.getMovieId()) 
                            title = f"{movie.getTitle()} - Row {b.getRow()} Seat {b.getSeat()}"
                            booking_choices.append(questionary.Choice(title=title, value=b.getId()))

                        selected_booking_id = questionary.select("select a booking:", choices=booking_choices).ask()

                        for i, b in enumerate(bookings):
                            if b.getId() == selected_booking_id:
                                removed = bookings.pop(i)
                                console.print(f"[bold red] booking canceled: {removed.getRow()}{removed.getSeat()}[/bold red]")
                                continue

            elif selected3 == admin_choices[6]:
                if not users or not bookings:
                    console.print("[red] sorry ! no users or movies found[/red]")
                else:
                    user_choices = [questionary.Choice(title=u.getEmail(), value=u.getId()) for u in users]
                    selected_user_id = questionary.select("Select user: ", choices=user_choices).ask()

                    user_bookings = [b for b in bookings if b.getUserId() == selected_user_id]

                    if not user_bookings:
                        console.print("[red] sorry ! there is no bookings for selected user[/red]")
                    else:
                        user_selected_email = isUserById(selected_user_id)

                        console.print(f"\n[bold blue] booking history for user: {user_selected_email.getEmail()}[/bold blue]\n")
                        for i, b in enumerate(user_bookings, start=1):
                            movie = findMovie(b.getMovieId()) 
                            console.print(f"""
[green]#{i}[/green]
🎬 Movie: [bold]{movie.getTitle()}[/bold]
🪑 Seat: Row {b.getRow()} - Seat {b.getSeat()}
            """)

 
            elif selected3 == admin_choices[7]:
                if not movies:
                    console.print("[red] no movies found.[/red]")
                else:
                    console.print("[bold cyan]\n Movies Statistics & Reports[/bold cyan]\n")

                    top_rated_movie = None
                    highest_avg_rating = 0

                    for movie in movies:
                        movie_title = movie.getTitle()
                        movie_id = movie.getId()

                        movie_bookings = [b for b in bookings if b.getMovieId() == movie_id]
                        booked_seats = len(movie_bookings)
                        remaining_seats = 100 - booked_seats

                        movie_ratings = [r for r in ratings if r.getMovieId() == movie_id]
                        if len(movie_ratings) > 0:
                            avg_rating = sum(r.getScore() for r in movie_ratings) / len(movie_ratings)
                        else:
                            avg_rating = 0
                        
                        
                        if avg_rating > highest_avg_rating:
                            highest_avg_rating = avg_rating
                            top_rated_movie = movie

                        console.print(f"""[bold]{movie_title}[/bold]
[green]Booked Seats:[/green] {booked_seats}
[yellow]Available Seats:[/yellow] {remaining_seats}
[magenta]Average Rating:[/magenta] {round(avg_rating, 2)} ★
            ------------------------""")

                    if top_rated_movie:
                        console.print(f"\n[bold yellow]Top Rated Movie:[/bold yellow] [green]{top_rated_movie.getTitle()}[/green] with [yellow]{round(highest_avg_rating, 2)}[/yellow] ★ \n")
                    export_choice = questionary.confirm("export report as .csv file ?").ask()

                    if export_choice:
                        with open('movie_report.csv', mode='w', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow(['Movie Title', 'Number of Booked Seats', 'Number of Available Seats', 'Average Rating'])

                            for movie in movies:
                                movie_title = movie.getTitle()
                                movie_id = movie.getId()
                                movie_bookings = [b for b in bookings if b.getMovieId() == movie_id]
                                booked_seats = len(movie_bookings)
                                remaining_seats = 100 - booked_seats
                                movie_ratings = [r for r in ratings if r.getMovieId() == movie_id]
                                avg_rating = sum(r.getScore() for r in movie_ratings) / len(movie_ratings) if movie_ratings else 0

                                writer.writerow([movie_title, booked_seats, remaining_seats, round(avg_rating, 2)])
                        system = platform.system()
                        subprocess.run(['open', 'movie_report.csv'])

                        console.print("[bold green]Report generated successfully! [/bold green]")

            elif selected3 == admin_choices[8]:
                #smart analytics using AI
                pass 

            elif selected3 == admin_choices[9]:
                #Ai Forecast
                pass

            elif selected3 == admin_choices[10]:
                # movie success predictor
                pass


            elif selected3 == admin_choices[11]:
                select_movie_choise = []
                for movie in movies:
                    title = movie.getTitle()
                    desc = movie.getDescription()
                    year = movie.getReleaseYear()


                    choice_line = f"{title} | {desc} - {year} "
                    select_movie_choise.append(
                    questionary.Choice(title=choice_line, value=movie.getId()))


                selected_movie_index = questionary.select("choose one of the following movies:",
                choices=select_movie_choise,use_arrow_keys=True).ask()
                selected_movie = next((m for m in movies if m.getId() == selected_movie_index), None)
                summary = SummarizeMovie(selected_movie.getId(),selected_movie.getTitle())

                console.print(f"\n[bold blue]Summary of Reviews for {selected_movie.getTitle()}[/bold blue]:")
                console.print(summary[0])
                
            



                

            



            selected3 = questionary.select(" Please choose an option:",
            choices=admin_choices,
            use_arrow_keys=True ).ask()
        
        else:
            with open('admins.json','w', encoding='UTF-8') as File:
                content = json.dumps(admins, indent=2)
                File.write(content)
                File.close()
                
            with open('users.json', 'w', encoding='UTF-8') as file:
                content = json.dumps([u.to_dict() for u in users], indent=2, ensure_ascii=False)
                file.write(content)

            with open('genres.json', 'w', encoding='UTF-8') as file:
                content = json.dumps([g.to_dict() for g in genres], indent=2, ensure_ascii=False)
                file.write(content)

            with open('movies.json', 'w', encoding='UTF-8') as file:
                content = json.dumps([m.to_dict() for m in movies], indent=2, ensure_ascii=False)
                file.write(content)

            with open('bookings.json', 'w', encoding='UTF-8') as file:
                content = json.dumps([b.to_dict() for b in bookings], indent=2, ensure_ascii=False)
                file.write(content)

            with open('ratings.json', 'w', encoding='UTF-8') as file:
                content = json.dumps([r.to_dict() for r in ratings], indent=2, ensure_ascii=False)
                file.write(content)
            
                    
            
          
          
        