"""Validate an IP Address
Write a program to Validate an IPv4 Address. According to Wikipedia, IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1. The generalized form of an IPv4 address is (0-255).(0-255).(0-255).(0-255). Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid. Your task is to returns 1 if the IP address is valid else returns 0.



Constraints:

1<=length of string <=50



Example 1:

Input:

ip = 222.111.111.111

Output: 1



Example 2:

Input:

ip = 5555..555

Output: 0

Explanation:

5555..555 is not a valid ip address, as the middle two portions are missing.

================================================================================"""
import ipaddress
ip= input()
try:
	ipaddress.ip_address(ip)
	print("Valid IP address")
except ValueError:
	print("Invalid IP address")
