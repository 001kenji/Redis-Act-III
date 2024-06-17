import redis,time
r = redis.StrictRedis(host='localhost',port=6379,db=0)

##-------------------------Redis - Backup
#1)For Synchronous Backup
r.save()
#2)For Asynchronous Backup
r.bgsave()
#3)  Restore Redis Data
val = r.config_get()
print('Directory for redis: ',val)
#Stop redis server, navigate to the directory and replace redis database file(dump.rdb) with the backup one, start redis server

##-------------------------Redis - Security
r.config_set('requirepass','your password for auth')
#this ensure before any person runs commands on the redis server they have to authenticate themselves 
#with the password set aboove, else " (error) NOAUTH Authentication required." will return if not authenticated

r.auth('your password for auth')


##--------------------------Redis - Benchmarks
#Redis benchmark is the utility to check the performance of Redis by running n commands simultaneously.
# Operation parameters

#this commands will test the time taken to "SET" 100 "string" in redis
num_operations = 100 
operation = 'SET'
key_prefix = 'benchmark_key_'

# Start timer
start_time = time.perf_counter()

# Perform operations
for i in range(num_operations):
    key = f"{key_prefix}{i}"
    value = f"value_{i}"
    r.set(key, value)

# Stop timer and calculate average latency
end_time = time.perf_counter()
total_time = end_time - start_time
average_latency = total_time / num_operations * 1000  # Convert to milliseconds

print(f"Average latency for {num_operations} {operation} operations: {average_latency:.2f} ms")


##Following example checks Redis by calling 100000 commands.
'''
redis-benchmark -n 100000  s
'''
