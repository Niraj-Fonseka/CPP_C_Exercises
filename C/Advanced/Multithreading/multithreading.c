#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // Header file for sleep()
#include <pthread.h>


void *myThreadFun(void *vargp){
    sleep(1);
    printf("Printing the my thread function\n");
    return NULL;
}


int main(){
    pthread_t thread_id; 
    printf("Before Thread\n"); 

    /*
    First arg : pointer to a thread which is set by this function
    Second arg : Attributes , if the value == NULL , default will be used
    Third arg : name of the function to be executed
    Fourth arg : args to passed into the function
    */
    pthread_create(&thread_id, NULL, myThreadFun, NULL); 
    pthread_join(thread_id, NULL); 
    printf("After Thread\n"); 
    exit(0); 
}