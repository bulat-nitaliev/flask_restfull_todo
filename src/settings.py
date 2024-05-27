from decouple import config

host = config('host')
user = config('user')
password = config('password')
database = config('database')
port = config('port')


test_host = config('test_host')
test_user = config('test_user')
test_password = config('test_password')
test_database = config('test_database')
test_port = config('test_port')
