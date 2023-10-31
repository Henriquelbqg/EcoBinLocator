import subprocess
import concurrent.futures

def run_server():
    subprocess.run("python manage.py runserver", shell=True)

def run_tests():
    subprocess.run("python manage.py test", shell=True)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_server = executor.submit(run_server)
        future_tests = executor.submit(run_tests)

        # Aguarde o término do servidor e dos testes
        future_server.result()
        future_tests.result()
