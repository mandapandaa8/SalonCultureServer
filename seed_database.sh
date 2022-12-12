rm db.sqlite3
rm -rf ./salonapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations salonapi
python3 manage.py migrate salonapi
python3 manage.py loaddata users
python3 manage.py loaddata hosts
python3 manage.py loaddata artists
python3 manage.py loaddata locations
python3 manage.py loaddata hostPhotos
python3 manage.py loaddata artistPhotos
python3 manage.py loaddata accommodations
python3 manage.py loaddata comments
python3 manage.py loaddata events
python3 manage.py loaddata tokens