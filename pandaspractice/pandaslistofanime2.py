 #!/usr/bin/python3
 
import pandas as pd
 
def main():

    csv_file = 'animelist.csv'
    anime  = pd.read_csv(csv_file)
  
    print(anime.head())
 
    animes = pd.read_csv(csv_file, index_col=0)

    print(animes.head())
    print(animes.shape)
 
    sorted_by_eps = animes.sort_values(["eps"], ascending=False)

    print(sorted_by_eps)
if __name__ == "__main__":
     main()

