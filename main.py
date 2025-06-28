
from rich.console import Console
from rich.syntax import Syntax
from datetime import datetime
import questionary
import json

users:list= []
movies:list= []
bookings:list= []
admins:list= []

try:
    with open('users.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        users= json.loads(content)
except Exception as e:
    print("file not found")

    
try:
    with open('movies.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        movies= json.loads(content)
except Exception as e:
    print("file not found")

try:
    with open('bookings.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        bookings= json.loads(content)
except Exception as e:
    print("file not found")

try:
    with open('admins.json', 'r', encoding='UTF-8') as File:
        content = File.read()
        admins= json.loads(content)
except Exception as e:
    print("file not found")

    
    
    



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
    emailFinded = False
    for user in users:
        if user['email'] == user_email:
            emailFinded = True
            console.print('[bold green]ً welcome back ! [/bold green]')
            continue
    if emailFinded == False:
        new_user_data = {
        "email": user_email,
        "movies": []
    }
        users.append(new_user_data)
        console.print('\n[bold blue] Welcome ! new account created [/bold blue]')
    

    msg = console.print('''\n[bold green]ًWelcome to Movie CLI Project ![/bold green]ً
            
Please choose an option:
''')
    user_choices = [
    "1) Search for movie by name",
    "2) Show available movies",
    "3) Book a movie",
    "4) Cancel a book",
    "5) Show booking history",
    "6) Smart search for a movie (AI-powered)" ,
    "7) Get AI movie recommendations (AI-powered)",
    "8) Smart chatbot (AI-powered)",
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
                if movie['title'] == movie_title:
                    movie_find = True
                    console.print("[yellow] Movie Found ! [/yellow]\n")
                    ratings = movie['ratings']
                    total_score = sum(r['score'] for r in ratings)
                    console.print(f'''[blue]
 Title: {movie['title']}                              
 description: {movie['description']}                              
 release_year: {movie['release_year']}                              
 average_ratings : [bold yellow]{total_score / len(ratings)} [/bold yellow]       
 Genres: {(', '.join(movie['genres']))}
 Ratings: 
 [/blue]''')
                    i = 0
                    for rating in ratings:
                        i+=1
                        description = rating['description']
                        score = rating['score']
                        console.print(f"[bold]{i}[/bold]- {description}: {score}")

            if movie_find==False:
                console.print("[bold red] Sorry! movie not found [/bold red]")
        if selected2 == user_choices[1]:
            print('----------------')
            for movie in movies:
                    ratings = movie['ratings']
                    total_score = sum(r['score'] for r in ratings)
                    console.print(f'''[blue]\n
 [bold green]{movie['title']}[/bold green]
 description: {movie['description']}                              
 release_year: {movie['release_year']}                              
 average_ratings : [bold yellow]{total_score / len(ratings)} [/bold yellow]       
 Genres: {(', '.join(movie['genres']))}
 Ratings:[/blue]''')
                    i = 0
                    for rating in ratings:
                        i+=1
                        description = rating['description']
                        score = rating['score']
                        console.print(f" [bold]{i}[/bold]- {description}: {score}")
            print('----------------')
        if selected2 == user_choices[2]:
            select_movie_choise = []
            for index, movie in enumerate(movies):
                title = movie['title']
                desc = movie['description']
                year = movie['release_year']
                ratings = movie['ratings']
                avg = (sum(r['score'] for r in ratings)/ len(ratings))

                choice_line = f"{title} | {desc} - {year} - Rating : {avg}"
                select_movie_choise.append(
                questionary.Choice(title=choice_line, value=index)
                )


            selected_movie_index = questionary.select("choose one of the following movies:",
            choices=select_movie_choise,use_arrow_keys=True).ask()

            selected_movie = movies[selected_movie_index]
            console.print("\n            Screen  \n")
            console.print("   1  2  3  4  5  6  7  8  9  10 ")
           
            booked_seats = {
                (booking["row"], booking["seat"])
                for booking in bookings
                if booking["movie_title"] == selected_movie['title']}
            
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

            new_booking = {
                "movie_title": selected_movie['title'],
                "user_email": user_email,
                "row": selected_row,
                "seat": selected_seat
            }
            bookings.append(new_booking)
            console.print(f'''[bold green]Booked successfully !
Movie Title: {selected_movie['title']}
email: {user_email}
row: {selected_row}
seat: {selected_seat}
[/bold green]''')
            

            
        if selected2 == user_choices[3]:
            user_bookings = []
            for index, booking in enumerate(bookings):
                if booking['user_email'].lower() == user_email.lower():
                    user_bookings.append((index, booking))

            if not user_bookings:
                console.print("[red] Sorry no bookings found.[/red]")
            else:
                bookings_choices = []
                for index, booking in user_bookings:
                    choice_title = f"{booking['movie_title']} - Row {booking['row']} Seat {booking['seat']}"
                    choice = questionary.Choice(title=choice_title, value=index)
                    bookings_choices.append(choice)

                selected_index = questionary.select("Choose a booking to cancel:",choices=bookings_choices).ask()

                removed = bookings.pop(selected_index)
                console.print(f'''[bold red]Booking canceled successfully !
Movie Title: {removed['movie_title']}
email: {user_email}
row: {removed['row']}
seat: {removed['seat']}
[/bold red]''')
        
        
        
        if selected2 == user_choices[4]:
            user_bookings = []
            for index, booking in enumerate(bookings):
                if booking['user_email'].lower() == user_email.lower():
                    user_bookings.append((index, booking))

            if not user_bookings:
                console.print("[red] Sorry no bookings found.[/red]")
            else:
                console.print("\nBookings list:")
                for index, booking in user_bookings:
                    console.print(f"{booking['movie_title']} - Row {booking['row']} Seat {booking['seat']}")
   





           



        selected2 = questionary.select(
        "\n Please choose an option:",
        choices=user_choices,
        use_arrow_keys=True).ask()
    else:
        with open('users.json','w', encoding='UTF-8') as File:
            content = json.dumps(users, indent=2)
            File.write(content)
            File.close()

        with open('movies.json','w', encoding='UTF-8') as File:
            content = json.dumps(movies, indent=2)
            File.write(content)
            File.close()

        with open('bookings.json','w', encoding='UTF-8') as File:
            content = json.dumps(bookings, indent=2)
            File.write(content)
            File.close()
            

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
    "0) Search for movie by name",
    "1) Add new movie",
    "2) Delete a movie ",
    "3) Edit existing movie information",
    "4) Book a movie for customer",
    "5) Cancel a movie booking for customer",
    "6) View customer bookings",
    "7) Reschedule a movie date/time",
    "8) View movies Statistics & Reports",
    "9) View Movie Feedback & Ratings",
    "10) Smart Analytics & Predictions (AI-powered)",
    "11) Exit",
]

        selected3 = questionary.select(
        " Please choose an option:",
        choices=admin_choices,
        use_arrow_keys=True).ask()
   
        while selected3 != admin_choices[10]:
            if selected3 == admin_choices[0]:
                print("hi")

        else:
            with open('admins.json','w', encoding='UTF-8') as File:
                content = json.dumps(admins, indent=2)
                File.write(content)
                File.close()
                
            selected3 = questionary.select(" Please choose an option:",
            choices=admin_choices,
            use_arrow_keys=True ).ask()
          
          
        