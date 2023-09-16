# Run docker-compose up -d command
docker-compose up -d

# Wait for a few seconds to make sure containers are up
Start-Sleep -Seconds 2

# Run the Main.py file using Python
python .\Main\Main.py
