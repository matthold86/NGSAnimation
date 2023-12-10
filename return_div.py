import sys
import os
import pandas as pd
from sqlconn import sqlConnect, sqlClose
from sqlquery import sqlQuery
from animate_vals import g
from plotly.offline import plot

def return_div(playId):

    gameId = 2022090800

    playId = int(playId)
    
    #### Uncomment after database is enabled 

    # cursor, status = sqlConnect()

    # if status != "Success":
    #     print('Error Occurred. Check error_log.txt.')
    #     sys.exit()

    # game_play_df = sqlQuery(cursor, 'nfl_La_vs_buf_20223', gameId, playId)

    # games_df = sqlQuery(cursor, 'nfl_games_2023', gameId, playId)

    # plays_df = sqlQuery(cursor, 'nflplays', gameId, playId)

    # player_info = sqlQuery(cursor, 'nfl_players_2023', gameId, playId)

    #Comment this out when connection to databricks is secured
    plays_df = pd.read_csv('plays.csv')

    games_df = pd.read_csv('games.csv')

    player_info = pd.read_csv('players.csv')

    game_df = pd.read_parquet('tracking_week_1.parquet')

    fig = g(plays_df, games_df, player_info, game_df, gameId, playId)

    return plot(fig, include_plotlyjs=False, output_type='div')

if __name__ == "__main__":
    print(return_div(56))
    