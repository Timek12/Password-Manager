#include <string.h>
#include <stdlib.h>
#include "blowfish.h"
#include "blowfish.c"

void encrypt_string(blowfish_cipher_t *blowfish_cipher, unsigned char* input_string, char* output_string)
{
    int len = strlen(input_string);
    int pad_len = (8 - (len % 8)) % 8; // calculate padding length
    int new_len = len + pad_len; // calculate new length with padding
    char* padded_string = malloc(new_len + 1); // allocate memory for padded string
    memset(padded_string, 0, new_len + 1); // initialize memory with zeros

    // copy input string to padded string
    memcpy(padded_string, input_string, len);

    // add padding
    for (int i = len; i < new_len; i++) {
        padded_string[i] = pad_len;
    }

    // encrypt padded string
    unsigned long xl, xr;
    for (int i = 0; i < new_len; i += 8) {
        // split 8-byte block into 2 32-bit words
        xl = *((unsigned long*)(&padded_string[i]));
        xr = *((unsigned long*)(&padded_string[i + 4]));

        // encrypt block
        blowfish_encrypt(blowfish_cipher, &xl, &xr);

        // copy encrypted block to output string
        *((unsigned long*)(&output_string[i])) = xl;
        *((unsigned long*)(&output_string[i + 4])) = xr;
    }

    free(padded_string);
}
