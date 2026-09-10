print("\ntask 1------")
nums=[1,2,3,4,5,6,7,8,9,10]
print("even only")
for a in nums:
    if a%2==0:
        print(a)
rev_nums=nums[::-1]
print("this is first reversal using slicing",rev_nums)
reversed_nums=[]
for n in nums:
    reversed_nums.insert(0,n)
print("this is using insert",reversed_nums)

print("\nTask 2-----")
students={
    "Aman":87,
    "Anshu":98,
    "Mahek":89,
    "Riya" : 87,
    "Neha" : 76
}
for key,value in students.items():
    print(key,value)

print("\ntask 3----")
text="artificial intelligence"
print(text.upper())
count=0
vowel=["a","e","i","o","u","A","E","I","O","U"]
for v in text:
    if v in vowel:
        count=count+1
print(count)

print("\nTask 4------")
def square(n):
    return n * n

print("Square of 5 is:",square(5))
print("Square of 8 is:",square(8))
print("Square of 12 is:",square(12))


def average(numbers):
    total = 0
    for n in numbers:
        total =+ n
    return total / len(numbers)

nums = [10, 20, 30, 40]
print(average(nums))