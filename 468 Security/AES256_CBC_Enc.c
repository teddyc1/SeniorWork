//Theodore Church
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
//OpenSSL includes
#include <openssl/evp.h>
#include <openssl/ssl.h>

int main(int argc, char *argv[]){
	if(argc != 9){
		printf("Too many, or not enough arguments. Use the following format: AES256_CBC_Enc –k <key file> -v <IV file> -i <input file> -o <output file>.\n");
		exit(0);
	}
	if (strcmp(argv[1],"-k")!=0){
		printf("First argument is not '-k', please change it to -k.\n");
		exit(0);
	}
	if (strcmp(argv[3],"-v")!=0){
		printf("Third argument is not '-v', please change it to -v.\n");
                exit(0);
	}
	if (strcmp(argv[5],"-i")!=0){
		printf("Fifth argument is not '-i', please change it to -i.\n");
                exit(0);
	}
	if (strcmp(argv[7],"-o")!=0){
		printf("Seventh argument is not '-o', please change it to -o.\n");
		exit(0);
	}
	FILE *fa;//key
	FILE *fb;//in
	FILE *fc;//out
	FILE *fd;//iv
	printf("Opening Key file:%s\n",argv[2]);
	fa = fopen(argv[2],"r");
	if(fa == NULL) {
      		printf("Error opening key file.\n");
      		return(-1);
   	}
	unsigned char key[33] = {};
	fgets(key,33,fa);
	fclose(fa);
	printf("Key: %s\n",key);
	if(isxdigit(key[0])!=0){
		printf("Key is valid.\n");
	}
	else{
		printf("Key is not valid. Exiting.\n");
		exit(0);
	}
	printf("Opening IV file:%s\n",argv[4]);
	fd = fopen(argv[4],"r");
	if(fd == NULL){
		printf("Error opening IV file.\n");
		return(-1);
	}
	unsigned char iv[17] = {};
	fgets(iv,17,fd);
	fclose(fd);
	printf("Key: %s\n",iv);
	if(isxdigit(iv[0])!=0){
		printf("IV is valid.\n");
	}
	else{
		printf("IV is not valid. Exiting.\n");
		exit(0);
	}	
	fb = fopen(argv[6],"r");
	if(fb == NULL){
		printf("Error opening input file.\n");
		return(-1);
	}	
	fc = fopen(argv[8],"w");
	if(fc == NULL){
		printf("Error opening output file.\n");
		return(-1);
	}
	// ~~~
	// Now for OpenSSL stuff
	// Note: Much of this is slightly modified from OpenSSL's own API example usage found here:
	// https://wiki.openssl.org/index.php/EVP
	// https://www.openssl.org/docs/man1.1.0/man3/EVP_EncryptInit.html
	// https://linux.die.net/man/3/evp_cipherinit
	// This is the AES-256 version 
	// ~~~
	unsigned char inbuf[1024], outbuf[1024 + EVP_MAX_BLOCK_LENGTH];
        int inlen, outlen;
	EVP_CIPHER_CTX *ctx; // Initialization of CTX is different than the documentation's example due to version
	ctx = EVP_CIPHER_CTX_new();
	EVP_CIPHER_CTX_init(ctx);
	EVP_CipherInit_ex(ctx, EVP_aes_256_cbc(), NULL, key, iv, 1);//1 encryption, 0 decryption
	for(;;){ // (;;) Learned about this from the API, it's essentially a While(1) that doesn't make the compiler grr angry.
		inlen = fread(inbuf, 1, 1024, fb);
                if(inlen <= 0) break;
                if(!EVP_CipherUpdate(ctx, outbuf, &outlen, inbuf, inlen)){
                        /* Error */
                        EVP_CIPHER_CTX_cleanup(ctx);
                        return 0;
                        }
                fwrite(outbuf, 1, outlen, fc);
                }
	 if(!EVP_CipherFinal_ex(ctx, outbuf, &outlen)){
                /* Error */
                EVP_CIPHER_CTX_cleanup(ctx);
                return 0;
                }
        fwrite(outbuf, 1, outlen, fc);
        EVP_CIPHER_CTX_cleanup(ctx);
	EVP_CIPHER_CTX_free(ctx); //making sure to free the ctx from memory
	exit(0);
}
