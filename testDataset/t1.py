def liftoff( max: int , min : int) -> None :
    counter  =  max
    while counter >= min :
      print( f'--------- { counter}	')
      counter -=	1

      print( f'--------  FIRE	')

if __name__ == "__main__":
    liftoff (10 , 1)