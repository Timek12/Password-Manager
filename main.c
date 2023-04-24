#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "blowfish.h"
#include "blowfish.c"

#define MAX_CIPHERTEXT_LEN 64


int main(int argc, char *argv[])
{
    if(argc != 2){
        printf("Failed");
        return 1;
    }

    unsigned char *password = argv[1];
    unsigned char ciphertext[sizeof(password)];
    memset(ciphertext, 0, sizeof(ciphertext));

    unsigned char key[] = "my_secret_key";



    blowfish_cipher_t *bfc = malloc(sizeof(blowfish_cipher_t));
    blowfish_key_setup(bfc, key, (int)strlen((const char*)key));
    unsigned long xl = 0;
    unsigned long xr = 0;

    // Copy the plaintext into the xl and xr variables
    memcpy(&xl, password, 4);
    memcpy(&xr, password + 4, 4);

    // Encrypt the xl and xr variables
    blowfish_encrypt(bfc, &xl, &xr);

    // Copy the encrypted xl and xr variables into the ciphertext buffer
    memcpy(ciphertext, &xl, 4);
    memcpy(ciphertext + 4, &xr, 4);

    char hex_ciphertext[MAX_CIPHERTEXT_LEN];
    memset(hex_ciphertext, 0, sizeof(hex_ciphertext));
    for(int i=0; i<sizeof(ciphertext); i++){
        sprintf(hex_ciphertext + i*2, "%02x", ciphertext[i]);
    }

    fprintf(stdout, "%s", hex_ciphertext); // print to stderr
    return 0;
}
