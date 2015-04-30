#include<stdio.h>
#include<fcntl.h>
#include<sys/mman.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<unistd.h>

#define PERI_BASE 0x20000000
#define GPIO_BASE (PERI_BASE + 0x200000)
#define BLK_SIZE (4*1024)

/**
 *Function to make portn as Input
 */

void setinp(volatile unsigned int *gpioptr ,int portn)
{
  *(gpioptr+(portn/10))&=~(7<<((portn%10)*3));  
}


/**
 *Function to make portn as output
 */
void setop(volatile unsigned int *gpioptr ,int portn)
{
  *(gpioptr+(portn/10))&=~(7<<((portn%10)*3));
  *(gpioptr+(portn/10))|=(1<<((portn%10)*3));  
}

/**
 *Function to set  portn 
 */
void gpioset(volatile unsigned int *gpioptr ,int portn)
{
  *(gpioptr+7+(portn/32))=1<<portn;  
}

/**
 *Function to clear portn 
 */
void gpioclr(volatile unsigned int *gpioptr ,int portn)
{
  *(gpioptr+10+(portn/32))=1<<portn;  
}

volatile unsigned int *initgpio(int *fd,void *ptr)
{
  
  *fd=open("/dev/mem",O_RDWR);
  if(*fd<1)
    {
      perror("open\n");
      return NULL;
    }
  ptr=mmap(NULL,BLK_SIZE,PROT_READ|PROT_WRITE,MAP_SHARED,*fd,GPIO_BASE);
  return((volatile unsigned int *)ptr);
}

void cleangpio(int fd,void *ptr1)
{
  munmap(ptr1,BLK_SIZE);
  close(fd);
}

int main()
{
  int fd=0;
  void *pr;
  volatile unsigned int * p;
  p=initgpio(&fd,pr);
  setop(p,4);
  cleangpio(fd,(void*)p);
  return 0;
}
