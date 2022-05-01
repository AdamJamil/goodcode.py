modular inverse
ll inv(ll a, ll b) { return 1 < a ? b - inv(b % a, a) * b / a : 1; }

gcd
ll gcd(ll a, ll b) { return a == 0 ? b : gcd(b % a, a); }

pow mod
ll powmod(ll x, ll pow) { if (pow == 0) return 1ll; ll temp = powmod(x,pow / 2); if (pow % 2 == 0) return (temp * temp) % MOD; return (((x * temp) % MOD) * temp) % MOD; }

lcm = ab/gcd(a,b)

sqrt factor
map<ll, ll> factor(ll x) {
    map<ll, ll> ret;
    for (ll p = 2; p * p <= x; ++p)
        while (x % p == 0) { x /= p; ret[p]++; }
    if (x != 1) ret[x]++;
    return ret;
}
