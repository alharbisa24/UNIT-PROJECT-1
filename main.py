
from rich.console import Console
from rich.syntax import Syntax
from datetime import datetime
import questionary
import json

import movie as MOVIE
import rating as RATING
import booking as BOOKING
import genres as GENRES
import user as USER
import random

users:list= []
movies:list= []
ratings:list= []
genres:list= []
bookings:list= []
admins:list= []

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
            genresOBJ = GENRES.Genres(genre['id'],genre['movie_id'],genre['name'])
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
    "1) Search for movie by title",
    "2) Show available movies",
    "3) Book a movie",
    "4) Cancel a book",
    "5) Show booking history",
    "6) Smart search for a movie (using AI)" ,
    "7) Get AI movie recommendations (using AI)",
    "8) Smart chatbot (using AI)",
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
            movie_title = console.input('Enter a movie name:')
            movie_find=False
            for movie in movies:
                if movie.getTitle() == movie_title:
                    movie_find = True
                    console.print("[yellow] Movie Found ! [/yellow]\n")
                    movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                    
                    try:
                        total_score = sum(r.getScore() for r in movie_ratings)
                        average_score = total_score / len(movie_ratings)
                    except Exception as e:
                        total_score =0
                        average_score = 0

                    movie_genres = [g for g in genres if g.getMovieId() == movie.getId()]
                    genre_names = [g.getName() for g in movie_genres]


                    
                    
                    console.print(f'''[blue]
 Title: {movie.getTitle()}                              
 description: [bold yellow]{movie.getDescription()}        [/bold yellow]                       
 release_year: [bold yellow]{movie.getReleaseYear()}        [/bold yellow]                             
 average_ratings : [bold yellow]{average_score} ★ [/bold yellow]       
 Genres: {(" - ".join(genre_names))}
 Ratings: 
 [/blue]''')
                    i = 0
                    for rating in ratings:
                        i+=1
                        description = rating.getDescription()
                        score = rating.getScore()
                        console.print(f"[bold]{i}[/bold]- {description}: {score}")

            if movie_find==False:
                console.print("[bold red] Sorry! movie not found [/bold red]")
        if selected2 == user_choices[1]:
            print('----------------')
            for movie in movies:
                    movie_bookings = []
                    for b in bookings:
                        movie_bookings = [b for b in bookings if b.getMovieId() == movie.getId()]
                   
                    if len(movie_bookings) < 100:
                        
                        movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                        try:
                            total_score = sum(r.getScore() for r in movie_ratings)
                            average_score = total_score / len(movie_ratings)
                        except Exception as e:
                            total_score =0
                            average_score = 0

                        movie_genres = [g for g in genres if g.getMovieId() == movie.getId()]
                        genre_names = [g.getName() for g in movie_genres]

                        console.print(f'''[blue]\n
 [bold green] {movie.getTitle()}[/bold green]
 description: [bold yellow]{movie.getDescription()}        [/bold yellow]                       
 release_year: [bold yellow]{movie.getReleaseYear()}        [/bold yellow]                       
 average_ratings : [bold yellow]{average_score} ★ [/bold yellow]       
 Avaliable Seats : [bold yellow]{len(movie_bookings)}[/bold yellow]   
 Genres: {(" - ".join(genre_names))}
 Ratings:[/blue]''')
                        i = 0
                        for ratin in ratings:
                            i+=1
                            description = ratin.getDescription()
                            score = ratin.getScore()
                            console.print(f" [bold]{i}[/bold]- {description}: {score}")
                            print('----------------')
        if selected2 == user_choices[2]:
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

                choice_line = f"{title} | {desc} - {year} - Rating : {average_score}"
                select_movie_choise.append(
                questionary.Choice(title=choice_line, value=index)
                )


            selected_movie_index = questionary.select("choose one of the following movies:",
            choices=select_movie_choise,use_arrow_keys=True).ask()

            selected_movie = movies[selected_movie_index]
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

            selected_seat_row =console.input("provide a row and seat to book: (EX : A5)")
           
            while(len(selected_seat_row) > 2 or len(selected_seat_row) < 1):
                selected_seat_row =console.input("provide a row and seat to book: (EX : A5)")



            selected_row = selected_seat_row[0]
            selected_seat = int(selected_seat_row[1:])
            if (selected_row, selected_seat) in booked_seats:
                console.print(f"[red] Sorry its already booked![/red]")
                selected_seat_row =console.input("provide a row and seat to book: (EX : A5)")


            booked_seats = [(b.getRow(), b.getSeat()) for b in bookings if b.getMovieId() == selected_movie.getId() and b.getUserId() == isUser(user_email)]   
            
            if len(booked_seats) > 0:
                    console.print("Sorry ! you already book for this movie before.")
                   
            else:
                new_booking = BOOKING.Booking(random.randint(100000, 999999),selected_movie.getId(),isUser(user_email),selected_row,selected_seat)
                bookings.append(new_booking)
                console.print(f'''[bold green]Booked successfully !
Movie Title: {selected_movie.getTitle()}
email: {user_email}
row: {selected_row}
seat: {selected_seat}
[/bold green]''')
            

            
        if selected2 == user_choices[3]:
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
        
        
        
        if selected2 == user_choices[4]:
            user_bookings = [b for b in bookings if b.getUserId() == isUser(user_email)]   
            if len(user_bookings) < 0:
                console.print("[red] Sorry no bookings found.[/red]")
            else:
                console.print("\nBookings list:")
                for b in user_bookings:
                    movie = findMovie(b.getMovieId())
                    console.print(f"{movie.getTitle()} - Row {b.getRow()} Seat {b.getSeat()}")
   
        if selected2 == user_choices[8]:
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
                console.print(f"\n✅ you rated: {rating_number} stars!")
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
        console.print('\n[bold blue] Welcome back [/bold blue]')

        msg = console.print('''\n[bold red]ًWelcome to Movie CLI Project ! (Signed As Admin) [/bold red]ً
Please choose an option:
''')
        admin_choices = [
    "0) Search for movie by title",
    "1) Add new movie",
    "2) Delete a movie",
    "3) Edit existing movie information",
    "4) Book a movie for customer",
    "5) Cancel a movie booking for customer",
    "6) View customer bookings",
    "7) View movies Statistics & Reports",
    "8) Smart Analytics & Predictions (AI-powered)",
    "9) Exit",
]

        selected3 = questionary.select(
        " Please choose an option:",
        choices=admin_choices,
        use_arrow_keys=True).ask()
   
        while selected3 != admin_choices[8]:
            if selected3 == admin_choices[0]:
                
                movie_title = console.input('Enter a movie name:')
                movie_find=False
                for movie in movies:
                    if movie.getTitle() == movie_title:
                        movie_find = True
                        console.print("[yellow] Movie Found ! [/yellow]\n")
                        movie_ratings = [r for r in ratings if r.getMovieId() == movie.getId()]
                        
                        try:
                            total_score = sum(r.getScore() for r in movie_ratings)
                            average_score = total_score / len(movie_ratings)
                        except Exception as e:
                            total_score =0
                            average_score = 0

                        movie_genres = [g for g in genres if g.getMovieId() == movie.getId()]
                        genre_names = [g.getName() for g in movie_genres]


                        
                        
                        console.print(f'''[blue]
    Title: {movie.getTitle()}                              
    description: [bold yellow]{movie.getDescription()}        [/bold yellow]                       
    release_year: [bold yellow]{movie.getReleaseYear()}        [/bold yellow]                             
    average_ratings : [bold yellow]{average_score} ★ [/bold yellow]       
    Genres: {(" - ".join(genre_names))}
    Ratings: 
    [/blue]''')
                        i = 0
                        for rating in ratings:
                            i+=1
                            description = rating.getDescription()
                            score = rating.getScore()
                            console.print(f"[bold]{i}[/bold]- {description}: {score}")

          
            with open('admins.json','w', encoding='UTF-8') as File:
                content = json.dumps(admins, indent=2)
                File.write(content)
                File.close()
                
            selected3 = questionary.select(" Please choose an option:",
            choices=admin_choices,
            use_arrow_keys=True ).ask()
          
          
        