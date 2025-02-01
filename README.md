# Fetch - Receipt Processor Challenge

## Steps

1. Change to repo directory on terminal

2. Build docker image
   `docker build -t receipts-api .`

3. Run docker image
   `docker run -p 80:80 receipts-api`

4. Access swagger page at `http://0.0.0.0:80/docs`

5. Run PyTests

   a. Run built image interactively
   `docker run -it receipts-api /bin/bash`

   b. Change directory to `/code/app`

   c. Run tests
   `pytest test_main.py`
