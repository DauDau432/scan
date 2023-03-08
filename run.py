import paramiko

def check_ssh_connection(ip_address, username, password, success_file):
    # Create a new SSH client
    ssh = paramiko.SSHClient()

    # Automatically add the server's host key
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server
        ssh.connect(ip_address, username=username, password=password)
        print("SSH connection successful for {}".format(ip_address))
        with open(success_file, "a") as f:
            f.write(ip_address + "\n")
    except Exception as e:
        print("Error connecting to {}: {}".format(ip_address, e))
    finally:
        # Close the SSH connection
        ssh.close()

# SSH credentials
username = "root"
password = "hqdata@9999"

# Read the list of IP addresses from a file
with open("ip.txt", "r") as f:
    ip_list = f.read().splitlines()

# Filename to store successful SSH connections
success_file = "success.txt"

# Check SSH connection for each IP address
for ip in ip_list:
    check_ssh_connection(ip, username, password, success_file)
