import multiprocessing
from math import trunc

class MultiprocessStart():
    def __init__(self) -> None:
        pass
    
    def process_function_input_params(self, song_object_list, number_of_iteration):

        #formats the input params that the start_multiple_instances funtion below requires
        song = song_object_list[number_of_iteration]
        print(song)
        
        

        print(f"counter: {number_of_iteration}, song.name:{song.name}")

        return song

    def start_multiple_instances(self,amount_of_threads,target_function,song_object_list,amount_of_rounds_needed,additional_second_run):
        #requires the parameters 
        #amount_of_threads: how many processes should be run simultaneously, 
        #target_function: which target should the processes have, 
        #function_params: which params does the target function require
        #thread_list: list that stores all the process instances
        thread_list = []

        if additional_second_run:
            thread_list = []



        for iteration in range(amount_of_rounds_needed):

            for i in range(amount_of_threads):

                #number_of_iteration: rounds which includes an i which fits with the amounts of simultaneously running processes, plus the current i which we are in the round right now
                if additional_second_run is False:
                    number_of_iteration = (iteration*amount_of_threads) + i

                    #creates the function parameters for the target function
                    function_parameters = self.process_function_input_params(song_object_list,number_of_iteration)

                elif additional_second_run is True:
                    # this is because we are going to extract the songs from the back of the list [:-3] so that we can loop through the last few songs
                    pos_in_list_from_back = -amount_of_threads+i
                    #creates the function parameters for the target function
                    function_parameters = self.process_function_input_params(song_object_list,pos_in_list_from_back) 
                    number_of_iteration = i
                    print(f"additional_second_run:{number_of_iteration}")

                
                print(f"thread_list:{thread_list}; number of iteration {number_of_iteration}")
                thread_list.append(multiprocessing.Process(target=target_function, args=(function_parameters,)))
                thread_list[number_of_iteration].start()

            for i in range(amount_of_threads):
                thread_list[number_of_iteration].join()
                #print("thead joined")
                
                #additonal statement for second run
                if additional_second_run:
                    number_of_iteration = i
                
                if not thread_list[number_of_iteration].is_alive():
                    print("thread finished")
                    thread_list[number_of_iteration].terminate()

    def start_threaded_download(self,amount_of_threads,target_function,song_object_list):
        amount_of_rounds_needed = len(song_object_list)/amount_of_threads

        print(f"amount_of_rounds_needed:{amount_of_rounds_needed}")

        if type(amount_of_rounds_needed) is not int:
            # rounds the amounts_of_rounds_needed always down if the number is not even / not an integer
            amount_of_rounds_needed = trunc(amount_of_rounds_needed)
            additional_round = True

            how_many_threads = len(song_object_list)%amount_of_threads
        

        elif type(amount_of_rounds_needed) is int:
            additional_round = False

        self.start_multiple_instances(amount_of_threads,target_function,song_object_list,amount_of_rounds_needed,additional_second_run=False)
        
        if additional_round is True:
            self.start_multiple_instances(how_many_threads,target_function,song_object_list,amount_of_rounds_needed=1,additional_second_run=True)