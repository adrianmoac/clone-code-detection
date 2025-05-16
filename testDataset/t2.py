def launch_ship ( time : int , countdown : int) -> None :
    liftoff( countdown , time )

def liftoff( max: int , min : int) -> None :
    counter  =  max
    while counter >= min :
      print( f'--------- { counter}	')
      counter -=	1

      print( f'--------  FIRE	')

if __name__ == "__main__":
    launch_ship (1 , 10)