import tkinter
import math
import requests
import json
import threading
from time import sleep


# Start new window
master = tkinter.Tk()
master.wm_title("JumpJumpChess")
master.resizable(width=False, height=False)
master.geometry("900x700+50+50")


# Define Base URL
url = "http://A.B.C.D/jjcapi/api.php"


# Parameters
canvas_width = 800
canvas_height = 800
ground_x = 350
ground_y = 350
triangle_s = 200
triangle_h = math.sqrt(3)/2 * triangle_s
button_w = 20
button_h = 20
w = tkinter.Canvas(master, width=canvas_width, height=canvas_height)
move = {}

# Entries
startscreen_username_entry = tkinter.Entry(master, font="Helvetica 16")
startscreen_username_entry.place(x = 450, y = 150, width = 200, height = 50)
startscreen_gameid_entry = tkinter.Entry(master, font="Helvetica 16")


# Define Buttons
startscreen_button_newgame = tkinter.Button(master, text="Start New Game", font="Helvetica 16", command= lambda: start_new_game(startscreen_username_entry.get()))
startscreen_button_newgame.place(x = 250, y = 250, width = 200, height = 50)
startscreen_button_joingame = tkinter.Button(master, text="Join Game", font="Helvetica 16", command= lambda: join_new_game(startscreen_username_entry.get()))
startscreen_button_joingame.place(x = 450, y = 250, width = 200, height = 50)
startscreen_button_gameid = tkinter.Button(master, text="Join Game", font="Helvetica 16")
startscreen_button_2players = tkinter.Button(master, text="2 Players", font="Helvetica 16")
startscreen_button_3players = tkinter.Button(master, text="3 Players", font="Helvetica 16")
startscreen_button_4players = tkinter.Button(master, text="4 Players", font="Helvetica 16")
startscreen_button_6players = tkinter.Button(master, text="6 Players", font="Helvetica 16")


# Define Labels
startscreen_title1 = tkinter.Label(master, text="JumpJumpChess", font="Helvetica 36 bold")
startscreen_title1.place(x = 0, y = 0, width = 900, height = 80)
startscreen_title2 = tkinter.Label(master, text="A Python/Tkinter implementation of Chinese checkers", font="Helvetica 12")
startscreen_title2.place(x = 0, y = 60, width = 900, height = 60)
startscreen_username = tkinter.Label(master, text="Enter your Name:", font="Helvetica 16 bold")
startscreen_username.place(x = 250, y = 150, width = 200, height = 50)
startscreen_gameid = tkinter.Label(master, text="Enter Game ID:", font="Helvetica 16 bold")
startscreen_newgameid = tkinter.Label(master, font="Helvetica 14 bold")
startscreen_player1 = tkinter.Label(master, font="Helvetica 14")
startscreen_player2 = tkinter.Label(master, font="Helvetica 14")
startscreen_player3 = tkinter.Label(master, font="Helvetica 14")
startscreen_player4 = tkinter.Label(master, font="Helvetica 14")
startscreen_player5 = tkinter.Label(master, font="Helvetica 14")
startscreen_player6 = tkinter.Label(master, font="Helvetica 14")
startscreen_state = tkinter.Label(master, font="Helvetica 10")
startscreen_state.place(x = 700, y = 650, width = 200, height = 50)
startscreen_playstate = tkinter.Label(master, font="Helvetica 10")
startscreen_playstate.place(x = 700, y = 600, width = 200, height = 50)


# Playfield
ground_list01 = ["f113"]
ground_list02 = ["f212","f213"]
ground_list03 = ["f311","f312","f313"]
ground_list04 = ["f410","f411","f412","f413"]
ground_list05 = ["f505","f506","f507","f508","f509","f510","f511","f512","f513","f514","f515","f516","f517"]
ground_list06 = ["f605","f606","f607","f608","f609","f610","f611","f612","f613","f614","f615","f616"]
ground_list07 = ["f705","f706","f707","f708","f709","f710","f711","f712","f713","f714","f715"]
ground_list08 = ["f805","f806","f807","f808","f809","f810","f811","f812","f813","f814"]
ground_list09 = ["f905","f906","f907","f908","f909","f910","f911","f912","f913"]
ground_list10 = ["f1004","f1005","f1006","f1007","f1008","f1009","f1010","f1011","f1012","f1013"]
ground_list11 = ["f1103","f1104","f1105","f1106","f1107","f1108","f1109","f1110","f1111","f1112","f1113"]
ground_list12 = ["f1202","f1203","f1204","f1205","f1206","f1207","f1208","f1209","f1210","f1211","f1212","f1213"]
ground_list13 = ["f1301","f1302","f1303","f1304","f1305","f1306","f1307","f1308","f1309","f1310","f1311","f1312","f1313"]
ground_list14 = ["f1405","f1406","f1407","f1408"]
ground_list15 = ["f1505","f1506","f1507"]
ground_list16 = ["f1605","f1606"]
ground_list17 = ["f1705"]
ground_list = ground_list01 + ground_list02 + ground_list03 + ground_list04 + ground_list05 + ground_list06 +ground_list07 + ground_list08 + ground_list09 + ground_list10 + ground_list11 + ground_list12 + ground_list13 + ground_list14 + ground_list15 + ground_list16 + ground_list17


# Create playfield buttons
for cnt_buttons in ground_list:
    exec("button_" + cnt_buttons + " = tkinter.Button(master)")




def join_new_game(username):
    # Clear screen
    startscreen_username_entry.place_forget()
    startscreen_username.place_forget()
    startscreen_button_newgame.place_forget()
    startscreen_button_joingame.place_forget()

    # Create entry field for gameid
    startscreen_gameid.place(x = 250, y = 150, width = 200, height = 50)
    startscreen_gameid_entry.place(x = 450, y = 150, width = 200, height = 50)

    # Create button to continue
    startscreen_button_gameid.place(x = 450, y = 250, width = 200, height = 50)
    startscreen_button_gameid.config(command= lambda: join_new_game_step2(username, startscreen_gameid_entry.get()))


# Join new game - Step2
def join_new_game_step2(username,gameid):

    # Clear screen
    startscreen_title1.place_forget()
    startscreen_title2.place_forget()
    startscreen_gameid.place_forget()
    startscreen_button_2players.place_forget()
    startscreen_button_3players.place_forget()
    startscreen_button_4players.place_forget()
    startscreen_button_6players.place_forget()
    startscreen_button_gameid.place_forget()
    startscreen_gameid_entry.place_forget()

    # Find the game with the specified gameid
    url_findgame = url + "/games?filter=id,eq," + gameid + "&transform=1"
    response_findgame = requests.get(url_findgame)
    response_findgame_json = response_findgame.json()

    # Add myself to the game
    for cnt_response_findgame in response_findgame_json["games"]:
        if (cnt_response_findgame["players"] == "2" or cnt_response_findgame["players"] == "3" or cnt_response_findgame["players"] == "4" or cnt_response_findgame["players"] == "6") and cnt_response_findgame["player2"] == "":
            payload_entergame = {"player2":username}
            player = "player2"
        elif (cnt_response_findgame["players"] == "3" or cnt_response_findgame["players"] == "4" or cnt_response_findgame["players"] == "6") and cnt_response_findgame["player3"] == "":
            payload_entergame = {"player3":username}
            player = "player3"
        elif (cnt_response_findgame["players"] == "4" or cnt_response_findgame["players"] == "6") and cnt_response_findgame["player4"] == "":
            payload_entergame = {"player4":username}
            player = "player4"
        elif cnt_response_findgame["players"] == "6" and cnt_response_findgame["player5"] == "":
            payload_entergame = {"player5":username}
            player = "player5"
        elif cnt_response_findgame["players"] == "6" and cnt_response_findgame["player6"] == "":
            payload_entergame = {"player6":username}
            player = "player6"
        url_entergame = url + "/games/" + gameid
        response_entergame = requests.put(url_entergame,data=json.dumps(payload_entergame))

    # Prepare the game
    prepareplayground(player,gameid)


# Start new game - Step1
def start_new_game(username):

    # Clear screen
    startscreen_username_entry.place_forget()
    startscreen_username.place_forget()
    startscreen_button_newgame.place_forget()
    startscreen_button_joingame.place_forget()

    # Create buttons to choose the number of players
    startscreen_button_2players.config(command= lambda: start_new_game_step2(username, "2"))
    startscreen_button_2players.place(x = 250, y = 150, width = 200, height = 50)
    startscreen_button_3players.config(command= lambda: start_new_game_step2(username, "3"))
    startscreen_button_3players.place(x = 450, y = 150, width = 200, height = 50)
    startscreen_button_4players.config(command= lambda: start_new_game_step2(username, "4"))
    startscreen_button_4players.place(x = 250, y = 200, width = 200, height = 50)
    startscreen_button_6players.config(command= lambda: start_new_game_step2(username, "6"))
    startscreen_button_6players.place(x = 450, y = 200, width = 200, height = 50)


# Start new game - Step2
def start_new_game_step2(username, players):

    # Clear screen
    startscreen_title1.place_forget()
    startscreen_title2.place_forget()
    startscreen_button_2players.place_forget()
    startscreen_button_3players.place_forget()
    startscreen_button_4players.place_forget()
    startscreen_button_6players.place_forget()

    # Create game at Server
    url_startnewgame = url + "/games"
    payload_startnewgame = {"started":"0","players":players,"player1":username}
    response_startnewgame = requests.post(url_startnewgame,data=json.dumps(payload_startnewgame))

    # Check for newly created game
    url_checknewgame = url + "/games?filter=id,eq," + response_startnewgame.text + "&transform=1"
    response_checknewgame = requests.get(url_checknewgame)
    response_checknewgame_json = response_checknewgame.json()
    prepareplayground("player1",response_checknewgame_json["games"][0]["id"])


# Prepare the game
def prepareplayground(player,gameid):
    startscreen_newgameid.config(text="Game ID: " + gameid)
    startscreen_newgameid.place(x = 700, y = 0, width = 200, height = 50)

    # Check game for start
    create_playground(player)
    checkgamestartthread = threading.Thread(target=checkgamestart, args=(gameid,))
    checkgamestartthread.start()

    # Create game status
    checkgameplaythread = threading.Thread(target=play, args=(player,gameid,))
    checkgameplaythread.start()


# Check if game is launched
def checkgamestart(newgameid):
    while True:

        # Add the player list
        url_checkgamestart = url + "/games?filter=id,eq," + newgameid + "&transform=1"
        response_checkgamestart = requests.get(url_checkgamestart)
        response_checkgamestart_json = response_checkgamestart.json()
        if response_checkgamestart_json["games"][0]["players"] == "2":
            startscreen_player1.config(bg="blue", fg="white")
            startscreen_player2.config(bg="green", fg="black")
        elif response_checkgamestart_json["games"][0]["players"] == "3":
            startscreen_player1.config(bg="blue", fg="white")
            startscreen_player2.config(bg="black", fg="white")
            startscreen_player3.config(bg="red", fg="white")
        elif response_checkgamestart_json["games"][0]["players"] == "4":
            startscreen_player1.config(bg="blue", fg="white")
            startscreen_player2.config(bg="yellow", fg="black")
            startscreen_player3.config(bg="green", fg="black")
            startscreen_player4.config(bg="red", fg="white")
        elif response_checkgamestart_json["games"][0]["players"] == "6":
            startscreen_player1.config(bg="blue", fg="white")
            startscreen_player2.config(bg="yellow", fg="black")
            startscreen_player3.config(bg="black", fg="white")
            startscreen_player4.config(bg="green", fg="black")
            startscreen_player5.config(bg="red", fg="white")
            startscreen_player6.config(bg="white", fg="black")
        startscreen_player1.config(text = response_checkgamestart_json["games"][0]["player1"])
        startscreen_player1.place(x = 700, y = 50, width = 200, height = 50)
        startscreen_player2.config(text = response_checkgamestart_json["games"][0]["player2"])
        startscreen_player2.place(x = 700, y = 100, width = 200, height = 50)
        startscreen_player3.config(text = response_checkgamestart_json["games"][0]["player3"])
        startscreen_player3.place(x = 700, y = 150, width = 200, height = 50)
        startscreen_player4.config(text = response_checkgamestart_json["games"][0]["player4"])
        startscreen_player4.place(x = 700, y = 200, width = 200, height = 50)
        startscreen_player5.config(text = response_checkgamestart_json["games"][0]["player5"])
        startscreen_player5.place(x = 700, y = 250, width = 200, height = 50)
        startscreen_player6.config(text = response_checkgamestart_json["games"][0]["player6"])
        startscreen_player6.place(x = 700, y = 300, width = 200, height = 50)

        # Game is started by the server
        if response_checkgamestart_json["games"][0]["started"] == "1":
            break

        # Continue checking if the game is not yet started
        else:
            startscreen_playstate.config(text = "Waiting for other players ...")
            sleep(1)
            continue

# gamestarted = "0"
#
# def checkgamestart2(newgameid):
#     if gamestarted == "0":
#         url_checkgamestart = url + "/games?filter=id,eq," + newgameid + "&transform=1"
#         response_checkgamestart = requests.get(url_checkgamestart)
#         response_checkgamestart_json = response_checkgamestart.json()
#         print(response_checkgamestart_json)
#         for cnt_response_checkgamestart in response_checkgamestart_json["games"]:
#             startscreen_player1.config(text = cnt_response_checkgamestart["player1"])
#             startscreen_player1.place(x = 700, y = 50, width = 200, height = 50)
#             startscreen_player2.config(text = cnt_response_checkgamestart["player2"])
#             startscreen_player2.place(x = 700, y = 100, width = 200, height = 50)
#             startscreen_player3.config(text = cnt_response_checkgamestart["player3"])
#             startscreen_player3.place(x = 700, y = 100, width = 200, height = 50)
#             startscreen_player4.config(text = cnt_response_checkgamestart["player4"])
#             startscreen_player4.place(x = 700, y = 100, width = 200, height = 50)
#             startscreen_player5.config(text = cnt_response_checkgamestart["player5"])
#             startscreen_player5.place(x = 700, y = 250, width = 200, height = 50)
#             startscreen_player6.config(text = cnt_response_checkgamestart["player6"])
#             startscreen_player6.place(x = 700, y = 300, width = 200, height = 50)
#
#         if cnt_response_checkgamestart["started"] == "1":
#             global gamestarted
#             gamestarted = "1"
#     #master.after(1000, checkgamestart2(newgameid))
#
#
#     #print(response_checknewgame_json["games"]["player1"])


# # Start new game - Step2
# def start_new_game2():
#     window = tkinter.Toplevel(master)
#     window.wm_title("Start New Game")
#     startscreen_username = tkinter.Label(window, text="Name:")
#     startscreen_username.place(x = 0, y = 0, width=100, height=50)
#     line2 = tkinter.Canvas(window, width=100,height=100)
#     line2.create_line(10, 10, 100, 10)
#     line2.place(x = 0, y = 50, width=100, height=100)


# def blub(cnt_ground_fields, ground_x_base, ground_y_base):
#     b1 = tkinter.Button(master, bg="red", command= lambda: blub(cnt_ground_fields, ground_x_base, ground_y_base))
#     b1.place(x = ground_x_base, y = ground_y_base, width=button_w, height=button_h)


# Make a move
def buttonclick(cnt_ground_fields, player):
    if player + "src" in move:
        move[player + "dst"] = cnt_ground_fields.strip("f")
        exec("button_" + cnt_ground_fields + ".config(text='X')")
    else:
        move[player + "src"] = cnt_ground_fields.strip("f")
        exec("button_" + cnt_ground_fields + ".config(text='X')")


# Create buttons for playing field
def create_button(cnt_ground_fields, ground_x_base, ground_y_base, player):
    exec("button_" + cnt_ground_fields + ".config(command= lambda: buttonclick('" + cnt_ground_fields + "', '" + player + "'))")
    exec("button_" + cnt_ground_fields + ".place(x = ground_x_base, y = ground_y_base, width=button_w, height=button_h)")


# Create playing field
def create_playground(player):
    ground_fields_x = {}
    ground_fields_y = {}

    ground_x_base = ground_x - button_w/2
    ground_y_base = ground_y - button_h/2 - 8*triangle_h/4.5
    for cnt_ground_fields in ground_list01:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)

    ground_x_base = ground_x - button_w/2 - 1*triangle_s/9
    ground_y_base = ground_y - button_h/2 - 7*triangle_h/4.5
    for cnt_ground_fields in ground_list02:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 2*triangle_s/9
    ground_y_base = ground_y - button_h/2 - 6*triangle_h/4.5
    for cnt_ground_fields in ground_list03:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 3*triangle_s/9
    ground_y_base = ground_y - button_h/2 - 5*triangle_h/4.5
    for cnt_ground_fields in ground_list04:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 12*triangle_s/9
    ground_y_base = ground_y - button_h/2 - 4*triangle_h/4.5
    for cnt_ground_fields in ground_list05:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 11*triangle_s/9
    ground_y_base = ground_y - button_h/2 - 3*triangle_h/4.5
    for cnt_ground_fields in ground_list06:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 10*triangle_s/9
    ground_y_base = ground_y - button_h/2 - 2*triangle_h/4.5
    for cnt_ground_fields in ground_list07:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 9*triangle_s/9
    ground_y_base = ground_y - button_h/2 - 1*triangle_h/4.5
    for cnt_ground_fields in ground_list08:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 8*triangle_s/9
    ground_y_base = ground_y - button_h/2
    for cnt_ground_fields in ground_list09:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 9*triangle_s/9
    ground_y_base = ground_y - button_h/2 + 1*triangle_h/4.5
    for cnt_ground_fields in ground_list10:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 10*triangle_s/9
    ground_y_base = ground_y - button_h/2 + 2*triangle_h/4.5
    for cnt_ground_fields in ground_list11:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 11*triangle_s/9
    ground_y_base = ground_y - button_h/2 + 3*triangle_h/4.5
    for cnt_ground_fields in ground_list12:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 12*triangle_s/9
    ground_y_base = ground_y - button_h/2 + 4*triangle_h/4.5
    for cnt_ground_fields in ground_list13:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 3*triangle_s/9
    ground_y_base = ground_y - button_h/2 + 5*triangle_h/4.5
    for cnt_ground_fields in ground_list14:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 2*triangle_s/9
    ground_y_base = ground_y - button_h/2 + 6*triangle_h/4.5
    for cnt_ground_fields in ground_list15:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2 - 1*triangle_s/9
    ground_y_base = ground_y - button_h/2 + 7*triangle_h/4.5
    for cnt_ground_fields in ground_list16:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    ground_x_base = ground_x - button_w/2
    ground_y_base = ground_y - button_h/2 + 8*triangle_h/4.5
    for cnt_ground_fields in ground_list17:
        ground_fields_x[cnt_ground_fields] = ground_x_base
        ground_fields_y[cnt_ground_fields] = ground_y_base
        create_button(cnt_ground_fields, ground_x_base, ground_y_base, player)
        ground_x_base = ground_x_base + 2*triangle_s/9

    # Create star
    w.place(x = 0, y = 0, width=800, height=800)
    ground_points = [ground_x,ground_y - 2*triangle_h, ground_x + triangle_s/2,ground_y-triangle_h, ground_x + triangle_s/2 + triangle_s,ground_y-triangle_h, ground_x + triangle_s,ground_y, ground_x + triangle_s/2 + triangle_s,ground_y+triangle_h, ground_x + triangle_s/2,ground_y+triangle_h, ground_x,ground_y + 2*triangle_h, ground_x - triangle_s/2,ground_y+triangle_h, ground_x - triangle_s/2 - triangle_s,ground_y+triangle_h, ground_x - triangle_s,ground_y, ground_x - triangle_s/2 - triangle_s,ground_y-triangle_h, ground_x - triangle_s/2,ground_y-triangle_h ]
    w.create_polygon(ground_points, outline='black', fill='tan1', width=3)


# Play the game
def play(player,newgameid):
    while True:
        url_checkgameplay = url + "/games?filter=id,eq," + newgameid + "&transform=1"
        response_checkgameplay = requests.get(url_checkgameplay)
        response_checkgameplay_json = response_checkgameplay.json()
        startscreen_state.config(text = "Round: " + response_checkgameplay_json["games"][0]["round"])
        master.wm_title("JumpJumpChess - " + response_checkgameplay_json["games"][0][player] + " - Round: " + response_checkgameplay_json["games"][0]["round"])

        # Update the playing field
        for cnt_play in ground_list:
            if int(response_checkgameplay_json["games"][0][str(cnt_play)]) in range(10,20):
                exec("button_" + str(cnt_play) + ".config(bg='blue', fg='white')")
            elif int(response_checkgameplay_json["games"][0][str(cnt_play)]) in range(20,30):
                exec("button_" + str(cnt_play) + ".config(bg='yellow', fg='black')")
            elif int(response_checkgameplay_json["games"][0][str(cnt_play)]) in range(30,40):
                exec("button_" + str(cnt_play) + ".config(bg='black', fg='white')")
            elif int(response_checkgameplay_json["games"][0][str(cnt_play)]) in range(40,50):
                exec("button_" + str(cnt_play) + ".config(bg='green', fg='black')")
            elif int(response_checkgameplay_json["games"][0][str(cnt_play)]) in range(50,60):
                exec("button_" + str(cnt_play) + ".config(bg='red', fg='white')")
            elif int(response_checkgameplay_json["games"][0][str(cnt_play)]) in range(60,70):
                exec("button_" + str(cnt_play) + ".config(bg='white', fg='black')")
            else:
                exec("button_" + str(cnt_play) + ".config(bg='light gray', fg='black')")

        # Check if someone did win
        if response_checkgameplay_json["games"][0]["winner"] != "":
            startscreen_playstate.config(text = response_checkgameplay_json["games"][0]["winner"] + " WINS!", fg="red")
            break

        # Check if we can play
        url_checkmove = url + "/rounds?filter[]=gameid,eq," + newgameid + "&filter[]=round,eq," + response_checkgameplay_json["games"][0]["round"] + "&satisfy=all&transform=1"
        response_checkmove = requests.get(url_checkmove)
        response_checkmove_json = response_checkmove.json()
        if response_checkmove_json["rounds"] != []:
            if response_checkmove_json["rounds"][0][player + "src"] == "1":
                startscreen_playstate.config(text = "IT'S YOUR TURN!", fg="red")
                if player + "src" and player + "dst" in move:
                    url_play = url + "/rounds/" + response_checkmove_json["rounds"][0]["id"]
                    response_play = requests.put(url_play,data=json.dumps(move))
                    exec("button_f" + move[player + "src"] + ".config(text='')")
                    exec("button_f" + move[player + "dst"] + ".config(text='')")
                    move.clear()
            else:
                startscreen_playstate.config(text = "Waiting ...", fg="black")

        # Continue checking
        sleep(1)
        continue


w.place(x = 0, y = 500, width=800, height=800)
master.mainloop()