N = int(input())
M = N*3
mid = (N//2)+1
w = "WELCOME"
pattern = ".|."
count=1
for i in range(1,mid+1):
    
    if i==mid:
        r = (M - len(w))//2
        print('-'*r + w + '-'*r)
    else:
        rem = (M-(count*3))//2
        print('-'*rem + pattern*count + '-'*rem)
        count += 2
for i in range(mid,N):
    count -= 2
    rem = (M-(count*3))//2
    print('-'*rem + pattern*count + '-'*rem)
    

'''
ALTERNATE METHOD 
'''

N,M = map(int,(input().split()))
pattern = [(".|."*(2*i+1)).center(M,'-') for i in range(N//2)]
print ("\n".join(pattern) + "\n" + "WELCOME".center(M,'-') + "\n" + "\n".join(pattern[::-1]))
    