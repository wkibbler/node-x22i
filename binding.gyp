{
    "targets": [
        {
            "target_name": "nodex21s",
            "sources": [
                "multihashing.cc",
		"sph/aes_helper.c",
		"sph/blake.c",
		"sph/bmw.c",
		"sph/cubehash.c",
		"sph/echo.c",
		"sph/extra.c",
		"sph/fugue.c",
		"sph/gost_streebog.c",
		"sph/groestl.c",
		"sph/hamsi.c",
		"sph/haval.c",
		"sph/jh.c",
		"sph/keccak.c",
		"sph/luffa.c",
		"sph/lyra2.c",
		"sph/sha2.c",
		"sph/shabal.c",
		"sph/shavite.c",
		"sph/simd.c",
		"sph/skein.c",
		"sph/sph_sha2big.c",
		"sph/sph_sha2.c",
		"sph/sponge.c",
		"sph/tiger.c",
		"sph/whirlpool.c",
	        "x21s.c",
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++11"
            ],
        }
    ]
}
