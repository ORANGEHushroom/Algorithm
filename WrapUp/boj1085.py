x,y,a,b = map(int,input().split())
lo = [x,abs(x-a),y,abs(y-b)]
print(min(lo))