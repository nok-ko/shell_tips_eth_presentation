python3 -c "print([n for n in range(2,1000) if all(n%d for d in range(2,int(n**0.5)+1))])"
