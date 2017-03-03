/* showip.c -- takes a hostname, returns an ip. */

/* -- Preamble -- */
#include<stdio.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netdb.h>
#include<arpa/inet.h>
#include<netinet/in.h>

/* --- Main --- */
int main (int argc, char *argv[]) {
  
  struct addrinfo hints, *res, *p;
  int status;
  char ipstr[INET6_ADDRSTRLEN];

  //incase too few/many args given, raise error
  if (argc != 2) {
    fprintf(stderr, "usage: showip hostname\n");
    return 1;
  }
  
  /* sin_zero (which is included to pad the structure to the length of a 
  struct sockaddr) should be set to all zeros with the function memset()*/
  memset (&hints, 0, sizeof hints);

  hints.ai_family = AF_UNSPEC; // AF_INET or AF_INET6 to force version
  hints.ai_socktype = SOCK_STREAM;
  
  // case raise error
  if ((status = getaddrinfo(argv[1], NULL, &hints, &res)) != 0) {
    fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(status));
    return 2;
  }
  
  //
  printf("IP Addresses for %s:\n\n", argv[1]);
  //for address in sockaddr struct, print address and version of protocol
  for (p = res; p != NULL; p = p->ai_next) {
    void *addr;
    char *ipver; 
    // get the pointer to the address itself,
    // different fields in IPv4 and IPv6:
    
    //if IPv4
    if (p -> ai_family == AF_INET) {

      struct sockaddr_in *ipv4 = (struct sockaddr_in *) p -> ai_addr;
      addr = &(ipv4 -> sin_addr);
      ipver = "IPv4";
    }
    
    else {
      // IPv6
      struct sockaddr_in6 *ipv6 = (struct sockaddr_in6 *) p -> ai_addr;
      addr = &(ipv6 -> sin6_addr);
      ipver = "IPv6";
    }

    // convert IP to a string and print it.
    inet_ntop(p -> ai_family, addr, ipstr, sizeof ipstr);
    printf("[+] %s: %s\n", ipver, ipstr);
  }
  /* When all done with the linked list that getaddrinfo() allocated 
     for us, we should free it up with a call to freeaddrinfo().*/
  freeaddrinfo(res);

  return 0;
} 
