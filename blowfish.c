#include "blowfish.h"

// Define the function for computing a 32-bit output value y based on a 32-bit input value x using the Blowfish S-boxes.
unsigned long F(blowfish_cipher_t *blowfish_cipher, unsigned long x)
{
    unsigned short a, b, c, d;
    unsigned long y;

    // split 32-bit x words into 8-bit values a, b, c, d
    d = (unsigned short)(x & 0xFF);
    x >>= 8;
    c = (unsigned short)(x & 0xFF);
    x >>= 8;
    b = (unsigned short)(x & 0xFF);
    x >>= 8;
    a = (unsigned short)(x & 0xFF);

    // Calculate the output value y
    y = blowfish_cipher->s[0][a] + blowfish_cipher->s[1][b];
    y = y ^ blowfish_cipher->s[2][c];
    y = y + blowfish_cipher->s[3][d];

    return y;
}

// Define function for generating Blowfish key schedule
void blowfish_key_setup(blowfish_cipher_t *blowfish_cipher, unsigned char *key, int key_len)
{
    int i, j, k;
    unsigned long data, data_l, data_r;

    for (i = 0; i < 4; i++) {
        for (j = 0; j < 256; j++)
            blowfish_cipher->s[i][j] = my_cypher.s[i][j];
    }

// XOR the P-array with the key
    j = 0;
    for(i = 0; i < N + 2; i++){
        data = 0x00000000;
        for(k = 0; k < 4; k++){
            data = (data << 8) | key[j];  // concatenate 4 key bytes into a single 32-bit word
            j = j + 1;
            if(j >= key_len){  // if all key bytes have been used, start over from the beginning
                j = 0;
            }
        }
        blowfish_cipher->p[i] = blowfish_cipher->p[i] ^ data;  // XOR the word with the P-array element
    }

// Encrypt the P-array with the all-zero block
    data_l = 0x00000000;
    data_r = 0x00000000;

    for(i = 0; i < N + 2; i += 2){
        blowfish_encrypt(blowfish_cipher, &data_l, &data_r);  // encrypt the all-zero block
        blowfish_cipher->p[i] = data_l;  // update the P-array element with the left half of the encrypted block
        blowfish_cipher->p[i + 1] = data_r;  // update the P-array element with the right half of the encrypted block
    }

// Encrypt the 4 S-boxes with the updated P-array
    for(i = 0; i < 4; i++){
        for(j = 0; j < 256; j += 2){
            blowfish_encrypt(blowfish_cipher, &data_l, &data_r);  // encrypt the all-zero block again
            blowfish_cipher->s[i][j] = data_l;  // update the i-th S-box with the left half of the encrypted block
            blowfish_cipher->s[i][j + 1] = data_r;  // update the i-th S-box with the right half of the encrypted block
        }
    }
}

// Define function for encrypting data with Blowfish
void blowfish_encrypt(blowfish_cipher_t *blowfish_cipher, unsigned long *xl, unsigned long *xr)
{
    unsigned long Xl;
    unsigned long Xr;
    unsigned long temp;
    short i;

    Xl = *xl;
    Xr = *xr;

    for(i=0; i < N; i++){
        Xl = Xl ^ blowfish_cipher->p[i];
        Xr = F(blowfish_cipher, Xl) ^ Xr;

        temp = Xl;
        Xl = Xr;
        Xr = temp;
    }

    temp = Xl;
    Xl = Xr;
    Xr = temp;

    Xr = Xr ^ blowfish_cipher->p[N];
    Xl = Xl ^ blowfish_cipher->p[N + 1];

    *xl = Xl;
    *xr = Xr;
}

// Define function for decrypting data with Blowfish
void blowfish_decrypt(blowfish_cipher_t *blowfish_cipher, unsigned long *xl, unsigned long *xr)
{
    unsigned long Xl;
    unsigned long Xr;
    unsigned long temp;
    short i;

    Xl = *xl;
    Xr = *xr;

    for(i = N + 1; i > 1; i--){
        Xl = Xl ^ blowfish_cipher->p[i];
        Xr = F(blowfish_cipher, Xl) ^ Xr;

        // swap Xl and Xr for decryption (reverse order)
        temp = Xl;
        Xl = Xr;
        Xr = temp;
    }

    temp = Xl;
    Xl = Xr;
    Xr = temp;

    Xr = Xr ^ blowfish_cipher->p[1];
    Xl = Xl ^ blowfish_cipher->p[0];

    *xl = Xl;
    *xr = Xr;
}
