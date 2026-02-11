from lib.database_connection import DatabaseConnection

# Run this file to reset your database using the seeds
# ; pipenv run python seed_dev_database.py

connection = DatabaseConnection(test_mode=False)
connection.connect()
# Add your own seed lines below...
# E.g.connection.seed("seeds/your_seed.sql")

# I didn't add my seed to line 9 above - but I seeded it a different way so I think it's okay. I did it using psql in the terminal, but if I wanted to use this file I could add the relevant seed file to line 9 then just run this file - seed_dev_database.py - from the terminal.