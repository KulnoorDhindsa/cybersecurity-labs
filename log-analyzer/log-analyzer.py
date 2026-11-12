from collections import Counter

failed_ips=Counter()
failed_users=Counter()

with open("auth_log.txt","r") as file:
    for line in file:
        if "Failed password" in line:
            parts=line.split()
            username=parts[8]
            ip_address=parts[10]
            failed_ips[ip_address]+=1
            failed_users[username]+=1

print("Failed login attempts by IP:")
for ip, count in failed_ips.items():
    print(f"{ip}: {count}")

print("\nSuspicious IP Addresses:")
for io, count in failed_ips.items():
    if count>=3:
        print(f"{ip}: {count} failed attempts")

for username, count in failed_users.items():
    print(f"{username}: {count}")           