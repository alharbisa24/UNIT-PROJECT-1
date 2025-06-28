
from rich.console import Console
from rich.syntax import Syntax
from datetime import datetime
import questionary
import json

def loadUsers():
    try:
        with open('users.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"❌ file '{'users.json'}' not found.")
        return []
    
def saveUsers(users_data):
    with open('users.json', 'w') as f:
        json.dump(users_data, f, indent=2)



def loadAdmins():
    try:
        with open('admins.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"❌ file '{'admins.json'}' not found.")
        return []
    
def loadBookings():
    try:
        with open('bookings.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"❌ file '{'bookings.json'}' not found.")
        return []

def loadMovies():
    try:
        with open('movies.json', 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"❌ file '{'movies.json'}' not found.")
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
    users_data = loadUsers()
    emailFinded = False
    for user in users_data:
        if user['email'] == user_email:
            emailFinded = True
            console.print('[bold red]ً welcome back ! [/bold red]')
            continue
    if emailFinded == False:
        new_user_data = {
        "email": user_email,
        "movies": []
    }
        users_data.append(new_user_data)
        saveUsers(users_data)
        console.print('\n[bold blue] Welcome ! new account created [/bold blue]')
    

    msg = console.print('''\n[bold green]ًWelcome to Movie CLI Project ![/bold green]ً
            
Please choose an option:
''')
    user_choices = [
    "1) Search for movie by name",
    "2) Show available movies",
    "3) Book a movie",
    "4) Cancel a booking",
    "5) Show your booking history",
    "6) Smart search for a movie (AI-powered)" ,
    "7) Get AI-based movie recommendations (AI-powered)",
    "8) Smart chatbot: Ask about movies (AI-powered)",
    "9) Search for movie by name",
    "10) Rate & review a movie",
    "11) Exit",
]

    selected2 = questionary.select(
        " Please choose an option:",
        choices=user_choices,
        use_arrow_keys=True 
    ).ask()
    while selected2 != user_choices[10]:
       
        if selected2 == user_choices[0]:
            movie_title = console.input('Enter a movie name:')
            movies = loadMovies()
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
            movies = loadMovies()
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



        selected2 = questionary.select(
        "\n Please choose an option:",
        choices=user_choices,
        use_arrow_keys=True).ask()

elif selected == choices[1]:

    admin_email  = console.input("enter your email: ")
    admins_data = loadAdmins()
    emailFinded = False
    for admin in admins_data:
        if admin['email'] == admin_email:
            emailFinded = True
            console.print('[bold red]ً welcome back ! [/bold red]')
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
    "6) View customer Bookings",
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
   
        while selected3 != admin_choices[11]:
            if selected3 == admin_choices[0]:
                print("hi")
                
            selected3 = questionary.select(" Please choose an option:",
            choices=admin_choices,
            use_arrow_keys=True ).ask()
          
          
        