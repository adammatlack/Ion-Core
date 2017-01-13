DIST_SUBDIRS = secp256k1

AM_LDFLAGS = $(PTHREAD_CFLAGS) $(LIBTOOL_LDFLAGS)

EXTRA_LIBRARIES =

ION_CONFIG_INCLUDES=-I$(builddir)/config
ION_INCLUDES=-I$(builddir) -I$(builddir)/obj $(LEVELDB_CPPFLAGS) $(BOOST_CPPFLAGS) $(CRYPTO_CFLAGS) $(SSL_CFLAGS)

ION_INCLUDES += -I$(srcdir)/secp256k1/include

$(LIBSECP256K1): $(wildcard secp256k1/src/*) $(wildcard secp256k1/include/*)
	$(AM_V_at)$(MAKE) $(AM_MAKEFLAGS) -C $(@D) $(@F)

# Make is not made aware of per-object dependencies to avoid limiting building parallelization
# But to build the less dependent modules first, we manually select their order here:

LIBION_SERVER=libion_server.a
LIBION_WALLET=libion_wallet.a
LIBION_COMMON=libion_common.a
LIBION_CLI=libion_cli.a
LIBION_UTIL=libion_util.a
LIBION_CRYPTO=crypto/libion_crypto.a
LIBIONQT=qt/libionqt.a
LIBSECP256K1=secp256k1/libsecp256k1.la

if EMBEDDED_LEVELDB
include Makefile.leveldb.include
endif

EXTRA_LIBRARIES += \
  crypto/libion_crypto.a \
  libion_util.a \
  libion_common.a \
  libion_server.a \
  libion_cli.a
if ENABLE_WALLET
ION_INCLUDES += $(BDB_CPPFLAGS)
EXTRA_LIBRARIES += libion_wallet.a
endif

if BUILD_ION_LIBS
lib_LTLIBRARIES = libionconsensus.la
LIBION_CONSENSUS=libionconsensus.la
else
LIBION_CONSENSUS=
endif


bin_PROGRAMS =
TESTS =

if BUILD_IOND
  bin_PROGRAMS += iond
endif

if BUILD_ION_UTILS
  bin_PROGRAMS += ion-cli ion-tx
endif

.PHONY: FORCE
# ion core #
ION_CORE_H = \
  alert.h \
  allocators.h \
  addrman.h \
  base58.h \
  chainparams.h \
  chainparamsseeds.h \
  checkpoints.h \
  compat.h \
  coincontrol.h \
  sync.h \
  util.h \
  hash.h \
  uint256.h \
  kernel.h \
  pbkdf2.h \
  serialize.h \
  support/cleanse.h \
  core.h \
  main.h \
  miner.h \
  net.h \
  ecwrapper.h \
  protocol.h \
  ui_interface.h \
  key.h \
  pubkey.h \
  db.h \
  txdb.h \
  txmempool.h \
  walletdb.h \
  script.h \
  scrypt.h \
  pow.h \
  init.h \
  mruset.h \
  wallet.h \
  keystore.h \
  rpcclient.h \
  rpcprotocol.h \
  rpcserver.h \
  timedata.h \
  crypter.h \
  version.h \
  netbase.h \
  clientversion.h \
  threadsafety.h \
  tinyformat.h \
  stealth.h \
  masternode.h \
  darksend.h \
  darksend-relay.h \
  instantx.h \
  activemasternode.h \
  masternodeconfig.h \
  masternodeman.h \
  masternode-payments.h \
  spork.h \
  smessage.h

obj/build.h: FORCE
	@$(MKDIR_P) $(builddir)/obj
	@$(top_srcdir)/share/genbuild.sh $(abs_top_builddir)/src/obj/build.h \
	  $(abs_top_srcdir)
libion_util_a-clientversion.$(OBJEXT): obj/build.h

# server: shared between iond and ion-qt
libion_server_a_CPPFLAGS = $(ION_INCLUDES) $(MINIUPNPC_CPPFLAGS)
libion_server_a_SOURCES = \
  alert.cpp \
  chainparams.cpp \
  sync.cpp \
  txmempool.cpp \
  util.cpp \
  hash.cpp \
  netbase.cpp \
  ecwrapper.cpp \
  key.cpp \
  pubkey.cpp \
  script.cpp \
  scrypt.cpp \
  core.cpp \
  main.cpp \
  miner.cpp \
  init.cpp \
  net.cpp \
  checkpoints.cpp \
  addrman.cpp \
  keystore.cpp \
  pow.cpp \
  rpcclient.cpp \
  rpcprotocol.cpp \
  rpcserver.cpp \
  rpcmisc.cpp \
  rpcnet.cpp \
  rpcmining.cpp \
  rpcblockchain.cpp \
  rpcrawtransaction.cpp \
  timedata.cpp \
  crypter.cpp \
  protocol.cpp \
  noui.cpp \
  kernel.cpp \
  pbkdf2.cpp \
  support/cleanse.cpp \
  stealth.cpp \
  rpcdarksend.cpp \
  smessage.cpp \
  rpcsmessage.cpp \
  $(ION_CORE_H)

# wallet: shared between iond and ion-qt, but only linked
# when wallet enabled
libion_wallet_a_CPPFLAGS = $(ION_INCLUDES)
libion_wallet_a_SOURCES = \
  db.cpp \
  walletdb.cpp \
  wallet.cpp \
  rpcwallet.cpp \
  rpcdump.cpp \
  masternode.cpp \
  darksend.cpp \
  darksend-relay.cpp \
  instantx.cpp \
  activemasternode.cpp \
  masternodeman.cpp \
  masternode-payments.cpp \
  spork.cpp \
  masternodeconfig.cpp \
  $(ION_CORE_H)

# crypto primitives library
crypto_libion_crypto_a_CFLAGS = -fPIC
crypto_libion_crypto_a_CPPFLAGS = $(ION_CONFIG_INCLUDES)
crypto_libion_crypto_a_SOURCES = \
  crypto/common.h \
  crypto/aes.h \
  crypto/hmac_sha256.h \
  crypto/hmac_sha512.h \
  crypto/ripemd160.h \
  crypto/sha1.h \
  crypto/sha256.h \
  crypto/sha512.h \
  crypto/hmac_sha256.cpp \
  crypto/aes.cpp \
  crypto/hmac_sha512.cpp \
  crypto/ripemd160.cpp \
  crypto/sha1.cpp \
  crypto/sha256.cpp \
  crypto/sha512.cpp

# common: shared between iond, and ion-qt and non-server tools
libion_common_a_CPPFLAGS = $(ION_INCLUDES)
libion_common_a_SOURCES = \
  alert.cpp \
  txmempool.cpp \
  ecwrapper.cpp \
  key.cpp \
  pubkey.cpp \
  script.cpp \
  core.cpp \
  main.cpp \
  init.cpp \
  net.cpp \
  checkpoints.cpp \
  addrman.cpp \
  keystore.cpp \
  pow.cpp \
  timedata.cpp \
  crypter.cpp \
  protocol.cpp \
  kernel.cpp \
  stealth.cpp \
  smessage.cpp \
  $(ION_CORE_H)

# util: shared between all executables.
# This library *must* be included to make sure that the glibc
# backward-compatibility objects and their sanity checks are linked.
libion_util_a_CPPFLAGS = $(ION_INCLUDES)
libion_util_a_SOURCES = \
  allocators.cpp \
  clientversion.cpp \
  rpcprotocol.cpp \
  sync.cpp \
  uint256.cpp \
  util.cpp \
  utilstrencodings.cpp \
  $(ION_CORE_H)

if GLIBC_BACK_COMPAT
libion_util_a_SOURCES += compat/glibc_compat.cpp
libion_util_a_SOURCES += compat/glibcxx_compat.cpp
endif

# cli: shared between ion-cli and ion-qt
libion_cli_a_CPPFLAGS = $(ION_INCLUDES)
libion_cli_a_SOURCES = \
  rpcclient.cpp \
  $(ION_CORE_H)

nodist_libion_util_a_SOURCES = $(srcdir)/obj/build.h
#

# iond binary #
iond_LDADD = \
  $(LIBION_SERVER) \
  $(LIBION_COMMON) \
  $(LIBION_UTIL) \
  $(LIBION_CRYPTO) \
  $(LIBLEVELDB) \
  $(LIBMEMENV) \
  $(LIBSECP256K1)
  
if ENABLE_WALLET
iond_LDADD += libion_wallet.a
endif
iond_SOURCES = bitcoind.cpp
#

if TARGET_WINDOWS
iond_SOURCES += iond-res.rc
endif

iond_LDADD += $(BOOST_LIBS) $(BDB_LIBS) $(SSL_LIBS) $(CRYPTO_LIBS) $(MINIUPNPC_LIBS)
iond_CPPFLAGS = $(ION_INCLUDES)
iond_LDFLAGS = $(RELDFLAGS) $(AM_LDFLAGS) $(LIBTOOL_APP_LDFLAGS)

# ion-cli binary #
ion_cli_LDADD = \
  $(LIBION_CLI) \
  $(LIBION_UTIL) \
  $(BOOST_LIBS) \
  $(SSL_LIBS) \
  $(CRYPTO_LIBS)

ion_cli_SOURCES = \
  ion-cli.cpp

ion_cli_CPPFLAGS = $(ION_INCLUDES)
#

# ion-tx binary #
ion_tx_LDADD = \
  $(LIBION_COMMON) \
  $(LIBION_UTIL) \
  $(LIBION_CRYPTO) \
  $(LIBSECP256K1) \
  $(BOOST_LIBS) \
  $(CRYPTO_LIBS)

ion_tx_SOURCES = ion-tx.cpp
ion_tx_CPPFLAGS = $(ION_INCLUDES)
#
ion_tx_LDFLAGS = $(RELDFLAGS) $(AM_LDFLAGS) $(LIBTOOL_APP_LDFLAGS)

if TARGET_WINDOWS
ion_cli_SOURCES += ion-cli-res.rc
endif
ion_cli_LDFLAGS = $(RELDFLAGS) $(AM_LDFLAGS) $(LIBTOOL_APP_LDFLAGS)

if BUILD_ION_LIBS
#include_HEADERS = script/ionconsensus.h
libionconsensus_la_SOURCES = \
  allocators.cpp \
  main.cpp \
  crypto/hmac_sha512.cpp \
  crypto/sha1.cpp \
  crypto/sha256.cpp \
  crypto/sha512.cpp \
  crypto/ripemd160.cpp \
  ecwrapper.cpp \
  hash.cpp \
  pubkey.cpp \
  script.cpp \
  uint256.cpp \
  utilstrencodings.cpp

if GLIBC_BACK_COMPAT
  libionconsensus_la_SOURCES += compat/glibc_compat.cpp
  libionconsensus_la_SOURCES += compat/glibcxx_compat.cpp
endif

libionconsensus_la_LDFLAGS = -no-undefined $(RELDFLAGS)
libionconsensus_la_LIBADD = $(LIBSECP256K1)
libionconsensus_la_LIBADD += $(CRYPTO_LIBS) $(BOOST_LIBS)
libionconsensus_la_CPPFLAGS = $(CRYPTO_CFLAGS) -I$(builddir)/obj -DBUILD_ION_INTERNAL
endif

CLEANFILES = leveldb/libleveldb.a leveldb/libmemenv.a *.gcda *.gcno

DISTCLEANFILES = obj/build.h

EXTRA_DIST = leveldb

clean-local:
	-$(MAKE) -C leveldb clean
	-$(MAKE) -C secp256k1 clean
	-rm -f leveldb/*/*.gcda leveldb/*/*.gcno leveldb/helpers/memenv/*.gcda leveldb/helpers/memenv/*.gcno
	-rm -f config.h

.rc.o:
	@test -f $(WINDRES)
	$(AM_V_GEN) $(WINDRES) -DWINDRES_PREPROC -i $< -o $@

.mm.o:
	$(AM_V_CXX) $(OBJCXX) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) \
	  $(CPPFLAGS) $(AM_CXXFLAGS) $(QT_INCLUDES) $(CXXFLAGS)  -c -o $@ $<

%.pb.cc %.pb.h: %.proto
	@test -f $(PROTOC)
	$(AM_V_GEN) $(PROTOC) --cpp_out=$(@D) --proto_path=$(abspath $(<D) $<)

#if ENABLE_TESTS
#include Makefile.test.include
#endif

if ENABLE_QT
include Makefile.qt.include
endif

#if ENABLE_QT_TESTS
#include Makefile.qttest.include
#endif
