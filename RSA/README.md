# RSA
Small exercise to understand the RSA algorithm. 

[!CAUTION]
DON´T USE THIS IN PRODUCTION!

Can only encript and decrypt integer values.

## Usage

```
generate_keys()
```

Returns a tuple of tuples. First element is the private, second the public key.

```
enc_msg(value, k_priv)
```

Takes a integer value and the private key.

```
dec_msg(crypt, k_pub)
```

Takes the encrypted value and the public key.