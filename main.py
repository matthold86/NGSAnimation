import sys
import os
import pandas as pd
from sqlconn import sqlConnect, sqlClose
from sqlquery import sqlQuery
from animate_vals import g
from plotly.offline import plot

def main():

    #### Uncomment after database is enabled 

    # cursor, status = sqlConnect()

    # if status != "Success":
    #     print('Error Occurred. Check error_log.txt.')
    #     sys.exit()

    # gameId = int(input("Enter gameId \n"))

    # playId = int(input("Enter playId \n"))

    # game_play_df = sqlQuery(cursor, 'nfl_La_vs_buf_20223', gameId, playId)

    # games_df = sqlQuery(cursor, 'nfl_games_2023', gameId, playId)

    # plays_df = sqlQuery(cursor, 'nflplays', gameId, playId)

    # player_info = sqlQuery(cursor, 'nfl_players_2023', gameId, playId)

    # PLAYVAL = 2

    fig = g(PLAYVAL)

    plot(fig)


if __name__ == "__main__":
    main()