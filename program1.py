#string reversal of large text
s = "The younger son of veteran Telugu actor Krishna, Babu made his debut as a child artist in a cameo role in Needa (1979), at the age of four, and acted in eight other films as a child artist. He made his debut as a lead actor with Rajakumarudu (1999) which won him the Nandi Award for Best Male Debut. Babu achieved his breakthrough with the supernatural drama Murari (2001), and the action film Okkadu (2003). He went on to act in other commercially successful films such as Athadu (2005), Pokiri (2006), Dookudu (2011), Businessman (2012), Seethamma Vakitlo Sirimalle Chettu (2013), Srimanthudu (2015), Bharat Ane Nenu (2018), Maharshi (2019), Sarileru Neekevvaru (2020) and Sarkaru Vaari Paata (2022). Pokiri held the record of being the highest-grossing Telugu film while Sarileru Neekevvaru, his highest grosser, collected over ₹260 crore at the box office.[4][5]"
reverse_s = s[::-1]
print(reverse_s)

#string reversal
s = "sai supriya"
reverse_s = s[::-1]
print(reverse_s)

#time complexity
import time
start=time.time()
n=input()
print(n[::-1])
end=time.time()
print(end-start)

