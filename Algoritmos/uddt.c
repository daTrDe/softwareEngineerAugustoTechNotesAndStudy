# include "stdlib.h"
# include "stdio.h"
# include "string.h"
// Tipos de datos definidos por el usuario (UDDT) en C
// Estructuras para almacenar información de un cliente
struct client {
    char Name[50];
    char Id [10];
    float Credit;
    char Address[100];
};

main (int argc, char const *argv[]) 
{
    struct client client1 = {0};
    strcpy(client1.Name, "Eragon Augusto");
    strcpy(client1.Id, "123456789");
    client1.Credit = 1000.50;
    strcpy(client1.Address, "123 Main St, Springfield");
    
    printf("CLient name is: %s /n", client1.Name);
    printf("\nClient ID is: %s /n", client1.Id);
    printf("\nClient Credit is: %.2f /n", client1.Credit);
    printf("\nClient Address is: %s\n", client1.Address);
    return 0;
}