echo "build start"

pip install -r software.txt
python3.9 manage.py collectstatic --noinput --clear

echo "build end"