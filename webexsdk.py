from webexteamssdk import WebexTeamsAPI

# https://developer.webex.com/docs/getting-started --> To access the Your Personal Access Token
api = WebexTeamsAPI(
    access_token=#(password goes here)
)

##### GET TEAM INFO #####
teams = api.teams.list()

for team in teams:
    print(team)
    if getattr(team, 'name') != 'Python Team':
        new_team = api.teams.create('Python Team')
        teamId = getattr(new_team, 'id')
    else:
        teamId = team.id

##### PEOPLE #####
print(api.people.me())

##### ROOMS #####
rooms = api.rooms.list()
evaluator = False
is_running = True

for room in rooms:
    while is_running:
        if room.title == 'Python Room':
            evaluator = True
            roomId = room.id
        else:
            new_room = api.rooms.create('Python Room', teamId=teamId)
            roomId = new_room.id
            is_running = False

##### MESSAGES ##### 
api.messages.create(roomId, text='Text created with Python SDK')

##### CLEANUP #####
# for room in rooms:
#     if getattr(room, 'title') == 'Python Room':
#         api.rooms.delete(getattr(room, 'id'))

# for team in teams:
#     if getattr(team, 'name') == 'Python Team':
#         api.teams.delete(getattr(team, 'id'))


