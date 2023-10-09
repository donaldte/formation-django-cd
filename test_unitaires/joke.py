import requests 



def len_joke() -> int:
    
    joke = get_joke()
    
    return len(joke)


def get_joke() -> str:
    
    response = requests.get('https://api.chucknorris.io/jokes/random')
    
    if response.status_code == 200:
        
        joke =  response.json()['value']
        
    
    else:
        
        joke = 'no joke'
    
    return joke




if __name__ == '__main__':
    
    print(get_joke())    
    print(len_joke())   