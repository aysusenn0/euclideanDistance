
def euclideanDistance(point1, point2):
    p = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
    return p

points=[(1,2),(3,4),(6,1),(4,2)]
distances=[]

for i in range(len(points)-1):
    temp=euclideanDistance(points[i],points[i+1])
    distances.append(temp)
enkucuk=distances[0]

for distance in distances:
    if distance<enkucuk:
        enkucuk=distance

print("Tum mesafeler: ",distances)
print("En küçük mesafe: ",enkucuk)


