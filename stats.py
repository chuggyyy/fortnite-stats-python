from pfaw import Fortnite, Mode



fortnite = Fortnite(fortnite_token='ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ=', launcher_token='MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE=',
                    password='yourpassword', email='youremail')


username = input("What is your Fortnite Name ? : ")

player = fortnite.player(username)

platform = input("pc / xb1 / ps4 : ")

print (player.name)
print (player.id)







stats = fortnite.battle_royale_stats(username , platform)

print(f'Solo Wins: {stats.solo.wins}')
print(f'Duo Wins: {stats.duo.wins}')
print(f'Squad Wins: {stats.squad.wins}')
print(f'Lifetime Wins: {stats.all.wins}')



while username != (''):
    username = input("What is your Fortnite Name ? : ")

    player = fortnite.player(username)

    platform = input("pc / xb1 / ps4 : ")

    print (player.name)
    print (player.id)







    stats = fortnite.battle_royale_stats(username , platform)

    print(f'Solo Wins: {stats.solo.wins}')
    print(f'Duo Wins: {stats.duo.wins}')
    print(f'Squad Wins: {stats.squad.wins}')
    print(f'Lifetime Wins: {stats.all.wins}')

else:
    print("Thx for using my Program")
