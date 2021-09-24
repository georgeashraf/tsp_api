import json
def tsm (environ):
    if environ.get('REQUEST_METHOD') == "GET":
        input = [(0,0),(1,1),(2,9),(5,7),(3,10),(8,4),(7,6)]
    else:
        length=int(environ.get('CONTENT_LENGTH') or 0)
        body = environ['wsgi.input'].read(length)
        data = json.loads(body.decode('utf-8'))
        input = data['input']
        input = [tuple(i) for i in input]
    total_cost = 0
    starting_point = input.pop(0)
    route = [starting_point]
   
    
    while(starting_point != -1):
        dic={}
        for i in input:

            distance = ((i[0]-starting_point[0])**2 +(i[1] - starting_point[1])**2 )**0.5
            dic[i] = distance


        sorted_tuples = sorted(dic.items(), key=lambda item: item[1])
        print(input)
        print(sorted_tuples)
        if sorted_tuples[0] not in route:
            
            route.append(sorted_tuples[0][0])
            starting_point = sorted_tuples[0][0]
            total_cost = total_cost + sorted_tuples[0][1]
            input.remove(starting_point)
            if len(input) == 0:
                break
        else:
            starting_point = -1
    print('route')        
    print(route)        
    return route , total_cost

def app(environ, start_response):
    print(environ)
    route, cost = tsm(environ)
    a = {
        "route":route,
        "cost":cost
    }
    # data=[[word.encode("utf8") for word in sets] for sets in route]
    # data = route.encode('utf-8')
    data = json.dumps(a).encode('utf-8')
    start_response(
        f"200 OK",[
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(data)))
        ]
    )
    return iter([data])