modular inverse
long inv(long a, long b) { return 1 < a ? b - inv(b % a, a) * b / a : 1; }

gcd
long gcd(long a, long b) { return a == 0 ? b : gcd(b % a, a); }

pow mod
long powmod(long x, long pow) { if (pow == 0) return 1L;long temp = powmod(x,pow / 2);if (pow % 2 == 0) return (temp * temp) % MOD;return (((x * temp) % MOD) * temp) % MOD; }

lcm = ab/gcd(a,b)

